#!/bin/bash
#
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT
#

FILE=/dev/$(dmesg |  grep axi:pps_axi_gpio_0 | grep -o "pps.:" | sed s'/.$//'| tail -1)
if [ ! -c "$FILE" ]; then
    echo "please load kr260-gps-1588-ptp  firmware"
    exit
fi
echo "refclock PPS /dev/$(dmesg |  grep axi:pps_axi_gpio_0 | grep -o "pps.:" | sed s'/.$//') lock NMEA refid GPS trust prefer" >> /etc/chrony/chrony.conf
echo "refclock SHM 0 offset 0.15 delay 0.2 refid NMEA trust prefer" >> /etc/chrony/chrony.conf

