#!/usr/bin/env python
import rospy
import math
import random
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Pose2D 

# Initialize qtable of all zeros df of shape (actions, states)
regions = ["left", "front", "right", "orientation"] # where each consists of 3-5 distance zones except orientation
distances = ["close","medium","far"]
actions = ["forward", "left", "right"]

region_distance = []
region_distance3 = []
q_states = []
for region in range(len(regions)):
    for distance in range(len(distances)):
        region_distance.append(regions[region] + "-" + distances[distance])

for rd in region_distance:
    for rd_rd in region_distance:
        for rd_rd_rd in region_distance:
            if rd[0] != rd_rd[0] and rd[0] != rd_rd_rd[0] and rd_rd[0] != rd_rd_rd[0]:
                region_distance3.append(rd + "-" + rd_rd + "-" + rd_rd_rd)

for rd_rd_rd in region_distance3:
    for action in actions:
        q_states.append(rd_rd_rd + "-" + action)

Q_table = dict.fromkeys(q_states , 0)

# Define discount factor
discount_factor = 0.9

msg = Pose2D() # Initialize a Pose2D message
# Publish Pose2D messages on vel_cmd topic to triton_lidar node 
pub = rospy.Publisher('/triton_lidar/vel_cmd', Pose2D, queue_size=10)

def Q(state, action):
    pass

def scan_callback(data): # Get state from here 
    rospy.loginfo("data: %s", data)

    # rosservice call /gazebo/get_model_state '{model_name: triton_lidar}'

def execute_random_action(duration):
    action = random.randint(0,2)
    if action == 0:           # Forward case
        msg.x = 0.3
    elif action == 1:         # Left case
        msg.x = 0.3
        msg.theta = math.pi/4
    else:                     # Right case
        msg.x = 0.3
        msg.theta = -math.pi/4
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
    timestep_duration = rospy.Duration(1) # One second
    while not rospy.is_shutdown():
        action = execute_random_action(timestep_duration) # Take action
        # Get state
        reward = Q(state, action)

        #state = rosservice call /gazebo/get_model_state '{model_name: triton_lidar}'
        #read_sensors()
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass