#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

export GAZEBO_RESOURCE_PATH=${SCRIPT_DIR}/catkin_ws/src/stingray_sim
export GAZEBO_MODEL_PATH=${SCRIPT_DIR}/catkin_ws/src/stingray_sim/models
export GAZEBO_PLUGIN_PATH=${SCRIPT_DIR}/catkin_ws/src/stingray_sim/plugins/build