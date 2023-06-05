#!/bin/bash
#
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT

FILE=/dev/$(dmesg |  grep axi:pps_axi_gpio_0 | grep -o "pps.:" | sed s'/.$//'| tail -1)
if [ ! -c "$FILE" ]; then
    echo "please load kr260-gps-1588-ptp firmware"
    exit
fi
if [  -c "/dev/ttyUL0" ]; then
    mv /dev/ttyUL0 /dev/tty16
fi
killall -9 gpsd
systemctl disable gpsd.socket
sleep 1
systemctl stop gpsd.service
sleep 3
systemctl start gpsd.service
killall -9 gpsd
sleep 1
echo "gpsd service started"
gpsd  -n -N /dev/tty16 &
echo "starting chrony"
systemctl restart chrony
timedatectl
sleep 180
chronyc sources
chronyc tracking
echo "************** System Clock Syncronized****************"
timedatectl
echo "*********** Before triggering phc2sys *************"
phc_ctl /dev/ptp1 get
phc2sys -c /dev/ptp1 -s CLOCK_REALTIME -O 0 &
sleep 5
echo "***** After triggering phc2sys the PHC time is updated with system time ******"
phc_ctl /dev/ptp1 get
ptp4l -i eth0  &
echo "******** ptp4l application running**********"



