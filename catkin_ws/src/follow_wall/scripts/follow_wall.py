#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs import Odometry
from nav_msgs import Path
from sensor_msgs import PointCloud2
from geometry_msgs.msg import Pose2D 

def path_callback(data):
    # Implement call to q learning 
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def odom_callback(data):
    # Implement call to q learning 
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def point_callback(data):
    # Implement call to q learning 
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def read_senors():

    rospy.init_node('read_sensors', anonymous=True)

    rospy.Subscriber("/triton/path", Path, path_callback)
    rospy.Subscriber("/triton/odom", Odometry, odom_callback)
    rospy.Subscriber("/camera/depth/points", PointCloud2, point_callback)
    
    rospy.spin()

def robot_control():
    pub = rospy.Publisher('/triton/vel_cmd geometry_msgs/Pose2D', Pose2D, queue_size=10)
    rospy.init_node('robot_control', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        # Control code goes here
        # pub.publish(hello_str)
        rate.sleep()

def main():
    pass

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass