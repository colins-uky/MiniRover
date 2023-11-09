# Minibot

Minibot is a ROS2 package that uses the ROS2 NAV2 stack and slam_toolbox to perform Simultaneous Localization and Mapping. This package was created in coordination by members of the Kentucky Organization of Robotics and Automation (KORA).

## Contents

1. [Materials](#materials)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Launch Minibot](#launch-minibot)
5. [Credits](#credits)

## Materials

We will be using the following materials for this minibot:




## Prerequisites


### 1. Install Ubuntu 20.04

This package requires ROS2 Foxy Fitzroy, which can only be installed on **Ubuntu 20.04 (Focal Fossa)**.


#### For x86_64:

* An installation guide provided by Ubuntu can be found [here](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

#### For Nvidia Jetson Nano (ARM):



* A precompiled Ubuntu 20.04 image for the Nvidia Jetson Nano can be found [here](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image).
    * (We will be using the barebones version)
    * Note: Normally Nvidia does not support Ubuntu versions past 18.04 (Bionic Beaver) for the Jetson Nano, but up to 20.04 has been used with success.


### 2. Install ROS2 Foxy Fitzroy

An installation guide for ROS2 Foxy Fitzroy can be found [here](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)

## Installation

### 1. Clone the Repo
Clone the repository package to your ROS2 workspace /src/ directory.

```bash
cd ~/Desktop/ros2_ws/src/
git clone https://github.com/colins-uky/minibot.git
```

### 2. Install Dependencies

Minibot borrows a few ROS2 nodes from other packages for publishing raw sensor data. Many of these packages are built by the creators of the sensors themselves.

#### rplidar_ros

```bash
sudo apt install blahblahblah
```

## Launch Minibot

Run the following command the verify the package was installed correctly:

```bash
source ./install/setup.bash
ros2 run minibot brb 
```



## Credits

- [Colin S.](https://github.com/colins-uky)
    * Package Creator