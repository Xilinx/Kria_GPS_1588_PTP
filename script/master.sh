#!/bin/bash
#
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT

mv /dev/ttyULR0 /dev/tty16
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
systemctl start chrony
timedatectl
sleep 120
chronyc sources
chronyc tracking
echo "************** System Clock Syncronized****************"
timedatectl
phc_ctl /dev/ptp1 get
phc2sys -c /dev/ptp1 -s CLOCK_REALTIME -O 0 &
sleep 5
phc_ctl /dev/ptp1 get
timedatectl
echo "*************** PHC_HW clock Syncronized ***************"
#sleep 1
ptp4l -i eth0  &
echo "******** ptp4l application running**********"



