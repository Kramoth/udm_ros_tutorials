# udm_ros_tutorials

Ce package contient plusieurs noeuds qui sont des subcribers et des publishers.

Pour que subscriber et publisher communiquent, il faut les lancer par pair correspondantes (publisher.py avec subscriber_d.py,publisher.py avec subscriber_d.py, publisher_clean.py avec subscriber_clean.py )

# Installation

Pour installer ce noeud il faut le cloner dans le dossier src de votre catkin workspace (catkin_ws)

```sh
cd catkin_ws/src
git clone https://github.com/Kramoth/udm_ros_tutorials.git
catkin build
cd ..
source devel/setup.bash
```

# Execution

Pour excuter les noeuds, il y a plusieurs facon de proceder:

# rosrun

Ouvrez deux terminaux sourcer le devel/setup.bash qui se situe dans le dossier catkin_ws dans chaque terminal.

Puis dans un terminal,

```sh
rosrun udm_ros_tutorials publisher.py
```
Dans l'autre terminal

```sh
rosrun udm_ros_tutorials subscriber.py
```
Normalement les noeuds seront lancer mais aucune communication ne se fait.

Pour palier a ce probleme, arreter le subscriber et faites:

```sh
rosrun udm_ros_tutorials subscriber.py /subscribed_topic:=/published_topic
```
sinon modifier les script pour que les noms de topic concordent.
# roslaunch

Ouvrir un terminal

```sh
cd catkin_ws
source devel/setup.bash
roslaunch udm_ros_tutorials tuto.launch
```
