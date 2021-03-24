#!/usr/bin/env python
import sys
import rospy
import math
import random
from qlearn_undef import q_table
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from gazebo_msgs.msg import ModelState, ModelStates
from geometry_msgs.msg import Pose2D

sys.dont_write_bytecode = True

# Initialize qtable of all zeros df of shape (actions, states)
# regions = ["left", "front", "right"] # where each consists of 3-5 distance zones except orientation
# distances = ["close","medium","far"]
# actions = ["forward", "left", "right"]

# region_distance = []
# region_distance3 = []
# q_states = []
# for region in regions:
#     for distance in distances:
#         region_distance.append(region + "-" + distance)

# for rd in region_distance:
#     for rd_rd in region_distance:
#         for rd_rd_rd in region_distance:
#             if rd[0] != rd_rd[0] and rd[0] != rd_rd_rd[0] and rd_rd[0] != rd_rd_rd[0]:
#                 region_distance3.append(rd + "-" + rd_rd + "-" + rd_rd_rd)

# for rd_rd_rd in region_distance3:
#     for action in actions:
#         q_states.append(rd_rd_rd + "-" + action)

# Q_table = dict.fromkeys(q_states , 0)

class State:
    def __init__(self, left=None, right=None, front=None):
        self.left = left
        self.front = front
        self.right = right


pose_x = 0
pose_y = 0
pose_z = 0

# Define initial state
state = State()

msg_vel_cmd = Pose2D()  # Initialize a Pose2D message
msg_set_model_state = ModelState(model_name="triton_lidar")  # Initialize a ModelState message

# Publish Pose2D messages on vel_cmd topic to triton_lidar node
pub_vel_cmd = rospy.Publisher("/triton_lidar/vel_cmd", Pose2D, queue_size=10)
# Publish ModelState messages on set_model_state topic to gazebo node
pub_set_model_state = rospy.Publisher("/gazebo/set_model_state", ModelState, queue_size=10)

def reset_robot():
    print "\n"
    print "Stuck... Resetting"
    msg_set_model_state.pose.position.x = 0
    msg_set_model_state.pose.position.y = 0
    msg_set_model_state.pose.position.z = 0
    msg_set_model_state.pose.orientation.x = 0
    msg_set_model_state.pose.orientation.y = 0
    msg_set_model_state.pose.orientation.z = 0
    msg_set_model_state.pose.orientation.w = 1
    pub_set_model_state.publish(msg_set_model_state)

def rew(prior_state):  # return imediate reward for the state the robot is in
    reward = 0
    if prior_state.left == "close" or prior_state.front == "close" or prior_state.right == "close":
        reward = 0
    elif prior_state.left == "far" and prior_state.right == "far":
        reward = 0
    else:
        reward = 100
    return reward


def update_q_table(discount_factor, learning_rate, action, reward, prior_state):
    if prior_state.left != None and prior_state.front != None and prior_state.right != None:
        state_index = "left-" + str(prior_state.left) + "-front-" + str(prior_state.front) + "-right-" + str(prior_state.right)
        # if action == 0:
        #     action = "forward"
        # elif action == 1:
        #     action = "left"
        # else:
        #      action = "right"
        q_table[state_index][action] = q_table[state_index][action] + learning_rate * (reward + discount_factor * max(q_table[state_index].values()) - q_table[state_index][action])


def Q_lookup_action(state):
    if state.left != None and state.right != None and state.right != None:
        state_index =  "left-" + str(state.left) + "-front-" + str(state.front) + "-right-" + str(state.right)
        if q_table[state_index]["left"] != q_table[state_index]["forward"] != q_table[state_index]["right"]:
            return max(q_table[state_index], key=q_table[state_index].get) # return action with highest reward
        else:
            return random.choice(list(q_table[state_index].keys()))
    return "State does not exist"


def Q_lookup_reward(state):
    if state.left != None and state.right != None and state.right != None:
        state_index = "left-" + str(state.left) + "-front-" + str(state.front) + "-right-" + str(state.right)
        if q_table[state_index]["left"] != q_table[state_index]["forward"] != q_table[state_index]["right"]:
            return max(q_table[state_index].values())  # return highest reward for a given state
        else:
            return random.choice(list(q_table[state_index].values()))
    return "State does not exist"


def scan_callback(data):  # Get state from here
    left = min(data.ranges[158:202]) 
    front = min(data.ranges[68:112])
    right = min(data.ranges[338:360] + data.ranges[0:22])
    if left < 0.7:
        state.left = "close"
    elif 0.7 <= left <= 1.2:
        state.left = "medium"
    else:
        state.left = "far"

    if front < 0.7:
        state.front = "close"
    elif 0.7 <= front <= 1.2:
        state.front = "medium"
    else:
        state.front = "far"

    if right < 0.7:
        state.right = "close"
    elif 0.7 <= right <= 1.2:
        state.right = "medium"
    else:
        state.right = "far"
    state_index = "left-" + str(state.left) + "-front-" + str(state.front) + "-right-" + str(state.right)

def pose_callback(data):
    global pose_x
    global pose_y
    global pose_z
    pose_x = data.pose[1].position.x
    pose_y = data.pose[1].position.y
    pose_z = data.pose[1].position.z


def execute_action(duration, action):
    if action == "forward":  # Forward case
        msg_vel_cmd.y = 0.3
    elif action == "left":  # Left case
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = math.pi / 2
    else:  # Right case
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = -math.pi / 2
    current_timestep = rospy.Time.now()
    future_timestep = current_timestep + duration
    while rospy.Time.now() < future_timestep:
        pub_vel_cmd.publish(msg_vel_cmd)  # Take action for one timestep
    msg_vel_cmd.y = 0
    msg_vel_cmd.theta = 0
    pub_vel_cmd.publish(msg_vel_cmd)

def execute_random_action(duration):
    action = random.randint(0, 2)
    if action == 0:
        action = "forward"  # Forward case
        msg_vel_cmd.y = 0.3
    elif action == 1:  # Left case
        action = "left"
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = math.pi / 2
    else:  # Right case
        action = "right"
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = -math.pi / 2
    current_timestep = rospy.Time.now()
    future_timestep = current_timestep + duration
    while rospy.Time.now() < future_timestep:
        pub_vel_cmd.publish(msg_vel_cmd)  # Take action for one timestep
    msg_vel_cmd.x = 0
    msg_vel_cmd.theta = 0
    pub_vel_cmd.publish(msg_vel_cmd)
    return action


def execute_exploited_action(duration, prior_state):
    action = Q_lookup_action(prior_state)
    if action == "forward":  # Forward case
        msg_vel_cmd.y = 0.3
    elif action == "left":  # Left case
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = math.pi / 2
    else:  # Right case
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = -math.pi / 2
    current_timestep = rospy.Time.now()
    future_timestep = current_timestep + duration
    while rospy.Time.now() < future_timestep:
        pub_vel_cmd.publish(msg_vel_cmd)  # Take action for one timestep
    msg_vel_cmd.x = 0
    msg_vel_cmd.theta = 0
    pub_vel_cmd.publish(msg_vel_cmd)
    return action


def main():
    max_timestep = 0
    discount_factor = 0.8
    learning_rate = 0.2
    epsilon_0 = 0.95
    d = 0.995
    episode_number = 0
    time_step = 0
    stuck_buffer_size = 3
    training_complete = False
    prior_state = State()
    prior_poses_y = [0, 0, 0]
    prior_poses_x = [0, 0, 0]
    rospy.init_node("follow_wall_q", anonymous=True)
    rate = rospy.Rate(20)  # 20hz
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.Subscriber("/gazebo/model_states", ModelStates, pose_callback)
    timestep_duration = rospy.Duration(0.5)  # One half second
     
    # need a short delay
    i = 0
    while i < 100:
        i += 1
        rate.sleep()

    while not rospy.is_shutdown() and not training_complete:  # Main loop
        terminate = False
        reset_robot()  # Reset robot pose
        timesteps_since_terminate = 0
        while not terminate and not training_complete:  # Episode loop
            
            r = random.uniform(0, 1)
            print "\n"
            print "Timestep is:", time_step
            print "\n"
            print "Current state is:", " left =", state.left, ", front =", state.front, ", right =", state.right
            prior_state.left = state.left
            prior_state.right = state.right
            prior_state.front = state.front
            prior_poses_x[time_step % stuck_buffer_size] = pose_x
            prior_poses_y[time_step % stuck_buffer_size] = pose_y
            epsilon = epsilon_0 * d ** episode_number
            if r > epsilon:  # Exploit
                action = execute_exploited_action(timestep_duration, prior_state)
                timesteps_since_terminate += 1
            else:  # Explore
                action = execute_random_action(timestep_duration)
                timesteps_since_terminate += 1
            reward = rew(prior_state)  # Receive imediate reward r
            update_q_table(discount_factor, learning_rate, action, reward, prior_state)
            print "\n"
            print "Epsilon is", epsilon
            if timesteps_since_terminate > max_timestep:
                max_timestep = timesteps_since_terminate
            print "\n"
            print "Max timestep since terminate:", max_timestep
            if (max(prior_poses_x) - min(prior_poses_x)) < 0.05 and (max(prior_poses_y) - min(prior_poses_y)) < 0.05 or pose_z > 0.05:  # Robot is stuck x, y havent moved past some threshold across past three timesteps
                terminate = True
            elif time_step > 10000:  # No terminate in past 1000 timesteps
                training_complete = True
                f = open("/home/anthony/Mines/CSCI573/project2/catkin_ws/src/follow_wall_q/q_table.py","w")  # Write learned policy to file
                f.write("q_table = " + str(q_table))
                f.close()
                print "Training Complete, q_table.py saved"

            time_step += 1

        episode_number += 1
        rate.sleep()
        
    f = open("/home/anthony/Mines/CSCI573/project2/catkin_ws/src/follow_wall_q/q_table.py","w")  # Write learned policy to file
    f.write("q_table = " + str(q_table))
    f.close()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass