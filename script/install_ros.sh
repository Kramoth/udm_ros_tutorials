#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
sudo apt update

install="full"
shell="sh"

while getopts "fdbz" opt; do
	case $opt in
		f)
			install="full"
			;;
		d)
			install="desktop"
			;;
		b)
			install="bare"
			;;	
		z)
			shell="zsh"
			;;
		\?)
			echo "invalid option"
			exit 1
			;;
	esac
done


echo "$shell"
echo "$install"
if [[ "$install" = "full" ]]; then
	echo "full"
	sudo apt -y install ros-melodic-desktop-full
elif [[ "$install" = "desktop" ]];then
	echo "desktop"
	sudo apt -y install ros-melodic-desktop
elif [[ "$install" = "bare" ]]; then
	echo "bare"
	sudo apt -y install ros-melodic-ros-base
fi

if [[ "$shell" = "sh" ]]; then
	echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
elif [[ "$shell" = "zsh"  ]]; then
	echo "source /opt/ros/melodic/setup.zsh" >> ~/.zshrc
fi
sudo apt -y install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt -y install python-rosdep

sudo rosdep init
rosdep update

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install python-catkin-tools
