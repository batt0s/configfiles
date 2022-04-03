#!/bin/sh
xrandr --output eDP --primary --mode 1280x720 --pos 0x0 --rotate normal --output HDMI-A-0 --off --output DisplayPort-0 --off --output DisplayPort-1 --off &
nitrogen --restore &
dunst &
picom -b &
volumeicon &
nm-applet --no-agent &
