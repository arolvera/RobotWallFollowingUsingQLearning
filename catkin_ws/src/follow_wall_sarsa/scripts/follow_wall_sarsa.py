#!/usr/bin/env python
import sys
import rospy
import math
import random
from qlearn import q_table
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
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

# Define discount factor
discount_factor = 0.9

class State:
    def __init__(self, left=None, right=None, front=None):
        self.left = left
        self.front = front
        self.right = right

# Define initial state
state = State()

msg = Pose2D() # Initialize a Pose2D message
# Publish Pose2D messages on vel_cmd topic to triton_lidar node 
pub = rospy.Publisher('/triton_lidar/vel_cmd', Pose2D, queue_size=10)

def Q(state, action):
    pass

def Q_lookup(state):
    if state.left != None and state.right != None and state.right != None:
        state_index = "left-" + str(state.left) + "-front-" + str(state.front) + "-right-" + str(state.right)
        return max(q_table[state_index], key=q_table[state_index].get) # return action with highest reward
    return "State does not exist"

def scan_callback(data): # Get state from here 

    left = min(data.ranges[45:134])
    front = min(data.ranges[315:360] + data.ranges[0:44])
    right = min(data.ranges[225:314])

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
                        
    if  right < 0.7:
        state.right = "close"
    elif 0.7 <= right <= 1.2:
        state.right = "medium"
    else:
        state.right = "far"
    
    # crosservice call /gazebo/get_model_state '{model_name: triton_lidar}'

def execute_action(duration, action):
    if action == "forward":   # Forward case
        msg.y = 0.3
    elif action == "left":    # Left case
        msg.y = 0.3
        msg.theta = -math.pi/2
    else:                     # Right case
        msg.y = 0.3
        msg.theta = math.pi/2
    current_timestep = rospy.Time.now()
    future_timestep = current_timestep + duration
    while rospy.Time.now() < future_timestep:
        pub.publish(msg) # Take action for one timestep
    msg.y = 0
    msg.theta = 0
    pub.publish(msg)

def execute_random_action(duration):
    action = random.randint(0,2)
    if action == 0:           # Forward case
        msg.x = 0.3
    elif action == 1:         # Left case
        msg.x = 0.3
        msg.theta = math.pi/2
    else:                     # Right case
        msg.x = 0.3
        msg.theta = -math.pi/2
    current_timestep = rospy.Time.now()
    future_timestep = current_timestep + duration
    while rospy.Time.now() < future_timestep:
        pub.publish(msg) # Take action for one timestep
    msg.x = 0
    msg.theta = 0
    pub.publish(msg)
    return action
    
def main():
    rospy.init_node('execute_action', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    timestep_duration = rospy.Duration(0.5) # One half second
    # Observe initial state

    while not rospy.is_shutdown():
        
        action = Q_lookup(state)
        execute_action(timestep_duration, action)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass