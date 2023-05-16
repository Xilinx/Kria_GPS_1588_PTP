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
cat << EOF > /etc/default/gpsd
START_DAEMON="true"
USBAUTO="false"
DEVICES="/dev/tty16 /dev/$(dmesg |  grep axi:pps_axi_gpio_0 | grep -o "pps.:" | sed s'/.$//')"
GPSD_OPTIONS="-n"
EOF
