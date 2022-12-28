#!/bin/bash

CAPACITY=$(cat /sys/class/power_supply/BAT0/capacity)
STATUS=$(cat /sys/class/power_supply/BAT0/status)

if [ "$STATUS" == "Discharging" ] && [ "$CAPACITY" -lt 15 ]
then
    notify-send -u critical -i $HOME/.config/i3/scripts/icons/battery-level-0-symbolic.svg "LOW BATTERY" "You are running low on battery, please plug in the charger.\nBAT: $CAPACITY%"
fi


