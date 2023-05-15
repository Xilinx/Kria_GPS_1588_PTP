#!/bin/bash
#
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT
#
echo "refclock PPS /dev/$(dmesg |  grep axi:pps_axi_gpio_0 | grep -o "pps.:" | sed s'/.$//') lock NMEA refid GPS trust prefer" >> /etc/chrony/chrony.conf
echo "refclock SHM 0 offset 0.15 delay 0.2 refid NMEA trust prefer" >> /etc/chrony/chrony.conf

