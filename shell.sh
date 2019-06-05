#!/bin/bash
# cd ../darknet
# ./darknet detect cfg/yolov3.cfg yolov3.weights /home/cpu11436/Documents/YOLO/input.jpg
# cp /home/cpu11436/Documents/darknet/predictions.jpg /home/cpu11436/Documents/YOLO/static/output.jpg
# $SHELL

gnome-terminal --command="bash -c 'cd /home/cpu11436/Documents/darknet; ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights $1; cp /home/cpu11436/Documents/darknet/predictions.jpg $2; exit; $SHELL'"
