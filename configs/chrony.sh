#!/bin/bash
#
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT
#

FILE=/dev/$(dmesg |  grep axi:pps_axi_gpio_0 | grep -o "pps.:" | sed s'/.$//'| tail -1)
if [ ! -c "$FILE" ]; then
    echo "Error: pps device not found. please load kr260-gps-1588-ptp firmware"
    exit
fi
cat << EOF > /etc/chrony/chrony.conf
# Include configuration files found in /etc/chrony/conf.d.
confdir /etc/chrony/conf.d

# About using servers from the NTP Pool Project in general see (LP: #104525).
pool ntp.ubuntu.com        iburst maxsources 4
pool 0.ubuntu.pool.ntp.org iburst maxsources 1
pool 1.ubuntu.pool.ntp.org iburst maxsources 1
pool 2.ubuntu.pool.ntp.org iburst maxsources 2

# Use time sources from DHCP.
sourcedir /run/chrony-dhcp

# Use NTP sources found in /etc/chrony/sources.d.
sourcedir /etc/chrony/sources.d

# This directive specify the location of the file containing ID/key pairs for
# NTP authentication.

keyfile /etc/chrony/chrony.keys


refclock PPS /dev/$(dmesg |  grep axi:pps_axi_gpio_0 | grep -o "pps.:" | sed s'/.$//' | tail -1) lock NMEA refid GPS trust prefer
refclock SHM 0 offset 0.15 delay 0.2 refid NMEA trust prefer

# This directive specify the file into which chronyd will store the rate
# information.

driftfile /var/lib/chrony/chrony.drift

# Save NTS keys and cookies.
ntsdumpdir /var/lib/chrony

# Log files location.
logdir /var/log/chrony

# Stop bad estimates upsetting machine clock.
maxupdateskew 100.0

# real-time clock. Note that it can’t be used along with the 'rtcfile' directive.

rtcsync

# Step the system clock instead of slewing it if the adjustment is larger than
# one second, but only in the first three clock updates.

makestep 1 3

leapsectz right/UTC

EOF
