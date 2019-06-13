#!/bin/bash
gnome-terminal --command="bash -c 'cd /home/cpu11436/Documents/darknet; ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights $1; cp /home/cpu11436/Documents/darknet/predictions.jpg $2; exit; $SHELL'"
