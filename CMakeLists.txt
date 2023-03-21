#
#copyright 2019 Xilinx Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

cmake_minimum_required(VERSION 3.5)

project(gps-ptp-application)

find_package(Python3 REQUIRED)

SET(INSTALL_PATH "opt/xilinx/kr260_gps_1588_ptp")



install(PROGRAMS src/main.py DESTINATION ${INSTALL_PATH}/bin)


install(PROGRAMS
    script/01.mipi-rtsp.sh
    script/02.mipi-dp.sh
    script/03.file-file.sh
    script/04.file-ssd-dp.sh
    script/smartcam-install.py
    DESTINATION ${INSTALL_PATH}/bin)

install(FILES
    README
    DESTINATION ${INSTALL_PATH}/
    )

install(DIRECTORY
    notebook/
    DESTINATION ${INSTALL_PATH}/share/notebooks/)

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

