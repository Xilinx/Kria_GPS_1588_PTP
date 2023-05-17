#
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT
#

cmake_minimum_required(VERSION 3.5)

project(gps-ptp-application)

#find_package(Python3 REQUIRED)

SET(INSTALL_PATH "/opt/xilinx/kr260-gps-1588-ptp")



install(PROGRAMS 
	src/master_gui.py
	src/slave_gui.py		
	DESTINATION ${INSTALL_PATH}/bin)


install(PROGRAMS
	script/slave.sh
	script/master.sh
	script/gps-1588-ptp-install.py
	script/gps-1588-ptp-master
	script/gps-1588-ptp-slave
	DESTINATION ${INSTALL_PATH}/bin)

install(FILES
	README.md
	DESTINATION ${INSTALL_PATH}/)

install(DIRECTORY
	notebook/
	DESTINATION ${INSTALL_PATH}/share/notebooks/)

install (DIRECTORY
	images/
	DESTINATION ${INSTALL_PATH}/share/images)

install (DIRECTORY
        configs/
        DESTINATION ${INSTALL_PATH}/configs/)

set(VERSION "1.0.1")
set(CPACK_PACKAGE_VERSION ${VERSION})
set(CPACK_GENERATOR "RPM")
set(CPACK_PACKAGE_NAME "${CMAKE_PROJECT_NAME}")
set(CPACK_PACKAGE_RELEASE 1)
set(CPACK_PACKAGE_CONTACT "chandrasekhar.chaduvula@amd.com")
set(CPACK_PACKAGE_VENDOR "AMD")
set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "arm64")
set(CPACK_RPM_PACKAGE_ARCHITECTURE ${CMAKE_SYSTEM_PROCESSOR})
set(CPACK_PACKAGING_INSTALL_PREFIX "/")
set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_PACKAGE_RELEASE}.${CMAKE_SYSTEM_PROCESSOR}")
set(CPACK_RPM_SPEC_MORE_DEFINE "%define _build_id_links none")
include(CPack)

