#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

# Launch bars
echo "---" | tee -a /tmp/polybar.log
polybar top >> /tmp/polybar.log 2>&1 &

echo "Bars launched."
