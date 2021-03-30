# SARSA
## The following package uses the triton robot simulated in gazebo and SARSA reinforcment learning to follow a wall 

To compile and run the code complete the following steps:

1.  Follow Singray-Simulation installation according to: https://gitlab.com/HCRLab/stingray-robotics/Stingray-Simulation
2.  $ cd ~/Stingray-Simulation/catkin_ws/src 
3.  Extract the folder in your ~/Stingray-Simulation/catkin_ws/src directory (The stingray_sim package must also be here)
4.  $ cd ~/Stingray-Simulation/catkin_ws/src/follow_wall/scripts
5.  Give run permissions for the executable using the following command $ chmod +x follow_wall_sarsa.py
6.  $ cd ~/Stingray-Simulation/catkin_ws
7.  $ source /opt/ros/melodic/setup.bash
8.  $ source devel/setup.bash
9.  $ source ~/Stingray-Simulation/stingray_setup.bash (Make sure this file specifies the correct resource, model and plugin paths)
10. $ catkin_make
11. $ roslaunch follow_wall_sarsa follow_wall_sarsa.launch train:=False 
12. ## By default the robot will use the pre-trained policy (In this case it may take a few moments for the robot to find the wall) set train to True to retrain the robot, this will take a few hours) 
13. Once triton finds a wall you should see it follow along the wall on the right side.