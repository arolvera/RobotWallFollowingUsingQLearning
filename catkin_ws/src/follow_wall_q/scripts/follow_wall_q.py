#!/usr/bin/env python
import sys
import rospy
import math
import random
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from gazebo_msgs.msg import ModelState, ModelStates
from geometry_msgs.msg import Pose2D

sys.dont_write_bytecode = True

args = rospy.myargv(argv=sys.argv)
if str(args[1]) == "True":
    train = True
else:
    train = False

if train:
    states_left = [
        "left-close", 
        "left-far"
    ] 

    states_front = [ 
        "front-tooclose", 
        "front-close", 
        "front-medium", 
        "front-far"
    ] 

    states_rightfront = [
        "rightfront-close", 
        "rightfront-far"
    ]

    states_right = [
        "right-tooclose",
        "right-close",  
        "right-medium", 
        "right-far", 
        "right-toofar"
    ]

    states_orientation = [
        "orientation-approaching",
        "orientation-parallel",
        "orientation-leaving",
        "orientation-undefined"
    ]

    q_table = {}

    for statel in states_left: # Make q_table initialized with all zeros
        for statef in states_front:
            for staterf in states_rightfront:
                for stater in states_right:
                    for stateo in states_orientation:
                        q_table[statel + "-" + statef + "-" + staterf + "-" + stater + "-" + stateo] = {"left": 0, "forward": 0, "right": 0}

else:
    from qtable_q import q_table

class State:
    def __init__(self, left=None, front=None, rightfront = None, right = None, orientation = None):
        self.left = left
        self.front = front
        self.rightfront = rightfront
        self.right = right
        self.orientation = orientation

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

def rew():  # Return immediate reward for the state the robot is in
    if state.right == "tooclose" or state.right == "toofar" or state.front == "tooclose" or state.left == "close":
        reward = -1
    else:
        reward = 0
    return reward

def update_q_table(discount_factor, learning_rate, action, reward, prior_state): 
    if prior_state.left != None and prior_state.front != None and prior_state.rightfront != None and prior_state.right != None and prior_state.orientation != None:
        state_index_prior = "left-" + str(prior_state.left) + "-front-" + str(prior_state.front) + "-rightfront-" + str(prior_state.rightfront) + "-right-" + str(prior_state.right) + "-orientation-" + str(prior_state.orientation)
        state_index_current = "left-" + str(state.left) + "-front-" + str(state.front) + "-rightfront-" + str(state.rightfront) + "-right-" + str(state.right) + "-orientation-" + str(state.orientation)        
        q_table[state_index_prior][action] = q_table[state_index_prior][action] + learning_rate * (reward + discount_factor * max(q_table[state_index_current].values()) - q_table[state_index_prior][action])
        
def Q_lookup_action(prior_state):
    if prior_state.left != None and prior_state.right != None  and prior_state.rightfront != None and prior_state.right != None and prior_state.orientation != None:
        state_index =  "left-" + str(prior_state.left) + "-front-" + str(prior_state.front) + "-rightfront-" + str(prior_state.rightfront) + "-right-" + str(prior_state.right) + "-orientation-" + str(prior_state.orientation)
        if q_table[state_index]["left"] != q_table[state_index]["forward"] != q_table[state_index]["right"]:
            return max(q_table[state_index], key=q_table[state_index].get) # return action with highest reward
        else:
            return random.choice(list(q_table[state_index].keys()))
    return "State does not exist"

def Q_lookup_reward(prior_state):
    if prior_state.left != None and prior_state.right != None and prior_state.rightfront != None and prior_state.right != None and prior_state.orientation != None:
        state_index = "left-" + str(prior_state.left) + "-front-" + str(prior_state.front) + "-rightfront-" + str(prior_state.rightfront) + "-right-" + str(prior_state.right) + "-orientation-" + str(prior_state.orientation)
        if q_table[state_index]["left"] != q_table[state_index]["forward"] != q_table[state_index]["right"]:
            return max(q_table[state_index].values())  # return highest reward for a given state
        else:
            return random.choice(list(q_table[state_index].values()))
    return "State does not exist"

def scan_callback(data):  # Get state from here
    left = min(data.ranges[150:210]) 
    front = min(data.ranges[60:120])
    rightfront = min(data.ranges[30:60])
    right = min(data.ranges[345:360] + data.ranges[0:15])
    min_range_angle = data.ranges.index(min(data.ranges))

    if left <= 0.5:
        state.left = "close"
    else:
        state.left = "far"

    if front < 0.5:
        state.front = "tooclose"
    elif 0.5 <= front < 0.6:
        state.front = "close"
    elif 0.6 <= front < 1.2:
        state.front = "medium"
    else:
        state.front = "far"

    if rightfront <= 1.2:
        state.rightfront = "close" 
    else:
        state.rightfront = "far"

    if right < 0.5:
        state.right = "tooclose"
    elif 0.5 <= right < 0.6:
        state.right = "close"
    elif 0.6 <= right <= 0.8:
        state.right = "medium"
    elif 0.8 <= right <= 1.2:
        state.right = "far"
    else:
        state.right = "toofar"

    if  180 > min_range_angle > 5:
        state.orientation = "approaching"
    elif 180 < min_range_angle < 355:
        state.orientation = "leaving"
    elif 0 <= min_range_angle <=5 or 355 <= min_range_angle <= 360:
        state.orientation = "parallel"
    else:
        state.orientation = "undefined"

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
        msg_vel_cmd.theta = math.pi / 4
    else:  # Right case
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = -math.pi / 4
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
        msg_vel_cmd.theta = math.pi / 4
    else:  # Right case
        action = "right"
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = -math.pi / 4
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
        msg_vel_cmd.theta = math.pi / 4
    else:  # Right case
        msg_vel_cmd.y = 0.3
        msg_vel_cmd.theta = -math.pi / 4
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
    epsilon_0 = 0.99
    d = 0.99
    episode_number = 0
    time_step = 0
    stuck_buffer_size = 3
    training_complete = False
    prior_state = State()
    rospy.init_node("follow_wall_q", anonymous=True)
    rate = rospy.Rate(20)  # 20hz
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    rospy.Subscriber("/gazebo/model_states", ModelStates, pose_callback)
    timestep_duration = rospy.Duration(0.5)  # One half second
     
    i = 0
    while i < 100: # Need a short delay
        i += 1
        rate.sleep()

    while not rospy.is_shutdown() and not training_complete:  # Main loop
        terminate = False
        reset_robot()  # Reset robot pose
        prior_poses_y = [0, 0, 0]
        prior_poses_x = [0, 0, 0]
        timesteps_since_terminate = 0
        r1 = random.uniform(0, 1)
        while not terminate and not training_complete:  # Episode loop    
            if train:        
                r = random.uniform(0, 1)
                print "\n"
                print "Timestep is:", time_step, "Episode is:", episode_number
                print "\n"
                print "Current state is:", " left =", state.left, ", front =", state.front, ", rightfront = ", state.rightfront, ", right =", state.right, ", orientation =", state.orientation
                prior_state.left = state.left
                prior_state.right = state.right
                prior_state.front = state.front
                prior_state.rightfront = state.rightfront
                prior_state.orientation = state.orientation
                prior_poses_x[time_step % stuck_buffer_size] = pose_x
                prior_poses_y[time_step % stuck_buffer_size] = pose_y
                epsilon = epsilon_0 * (d ** episode_number)
                if r > epsilon:  # Exploit
                    action = execute_exploited_action(timestep_duration, prior_state)
                    timesteps_since_terminate += 1
                else:            # Explore
                    action = execute_random_action(timestep_duration)
                    timesteps_since_terminate += 1
                reward = rew()   # Receive immediate reward r
                update_q_table(discount_factor, learning_rate, action, reward, prior_state)
                print "\n"
                print "Epsilon is", epsilon
                if timesteps_since_terminate > max_timestep:
                    max_timestep = timesteps_since_terminate
                print "\n"
                print "Max timestep since terminate:", max_timestep
                if (max(prior_poses_x) - min(prior_poses_x)) < 0.05 and (max(prior_poses_y) - min(prior_poses_y)) < 0.05 or pose_z > 0.05:  # Robot is stuck x, y havent moved past some threshold across past three timesteps
                    terminate = True
                elif time_step > 30000:  # 30000 timesteps is sufficient
                    training_complete = True
                    f = open("/home/anthony/Mines/CSCI573/project2/catkin_ws/src/follow_wall_q/scripts/qtable_q.py","w")  # Write learned policy to file
                    f.write("q_table = " + str(q_table))
                    f.close()
                    print "Training Complete, qtable_q.py saved"

                time_step += 1
            else:
                execute_exploited_action(timestep_duration, state)

        episode_number += 1
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass