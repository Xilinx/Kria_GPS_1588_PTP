# GPS-1588-PTP

## Introduction
  This app demonstrates how to use Open Source Software stack for local clock grandmaster role between 2 or more KR260 boards 
  GPS-1588-PTP Application built on KR260 Robotics starter kit to Synchronize the linux platform System Time with GPS Time and distribute the system time to an another KR260 board using linux PTP tools. The application uses gpsd, chrony deamons and linux ptp utilities.this Application using two KR260 Robotics starter kits for master and slave communicaton. Digilent pmod-gps receiver is connected to the master board. The master board captures the gps data which is in NMEA format through uart lite interface and one pps input through GPIO for systemtime correction .
 
  For more details refer [KR260 SOM GPS-1588-PTP App Start Page](https://xilinx.github.io/kria-apps-docs/kr260/build/html/docs/gps_1588_ptp/gps_1588_ptp_precision_time_mgmt.html)

## Setting up the Board and Application Deployment

  A step by step tutorial and details on how to setup the board and run this application is given in the [GPS-1588-PTP](https://xilinx.github.io/kria-apps-docs/kr260/build/html/docs/gps_1588_ptp/docs/app_deployment.html). Please visit the documentation page for more details.

## License
Copyright (C) 2023 Advanced Micro Devices, Inc.

SPDX-License-Identifier: MIT
