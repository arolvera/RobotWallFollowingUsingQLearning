# Reinforcment Learning for Robot Navigation

In thiswork we implement multiple
reinforcement learning algorithms for the purpose of teaching
a robot to learn how to autonomously follow along a wall
with no need for human intervention. Using ROS a Triton
robot is utilized inside the gazebo simulator and trained using
both q and SARSA reinforcement learning policies. The robot
is equipped with a 3D laser scanning Li-DAR sensor which
provides 360 degree range data that allows us to construct
a state model in terms of the distances to the surrounding
walls. This state model is used for both algorithms. We define
a set or actions the robot can take and a set of rewards
given for taking the appropriate action. The robot was able
to learn how to follow along the wall using both algorithms.
The robot was also able to turn corners of both 90 and 180
degrees while moving along the wall. We found that the SARSA
method converges faster, needing fewer episodes for training
than the traditional off-policy q-learning method. We also found
that the SARSA method outperforms the q-learning method
in terms of robot performance while following along a wall,
finding the wall faster and moving along a straighter path. 
More information can be found in the PDF.

Instructions on running the code can be found in the README for 
each package under catkin_ws/src/"package_name"