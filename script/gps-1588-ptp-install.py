#!/usr/bin/python3
# Copyright (C) 2023 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT


import argparse
import pathlib
import os
import sys
import shutil

def main(appname):
    note_dir="/opt/xilinx/kr260-"+appname+"/share/notebooks/"
    parser = argparse.ArgumentParser(prog=appname+'-install',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='Script to copy {} Jupyter notebook to user directory'.format(appname))
    parser.add_argument('-d', '--dir', type=pathlib.Path, help='Install the Jupyter notebook to the specified directory.', default=os.path.join("/notebooks") )
    parser.add_argument('-f', '--force', action='store_true', help='Force to install the Jupyter notebook even if the destination directory exists.')
    args = parser.parse_args()
    destdir = os.path.abspath(args.dir)

    if os.path.exists(destdir):
        if os.path.isfile(destdir):
                sys.exit("Error: Destination directory {} is an existing file.".format(destdir))
        else:
            if not args.force:
                sys.exit("Error: Destination directory {} already exists, please use another dirname or use '--force' option.".format(destdir))
            else:
                print("Info: Destination directory "+destdir+" already exists, force removing it.")
                shutil.rmtree(destdir)

    ignore = shutil.ignore_patterns('.ipynb_checkpoints','*.pyc','*~')
    srcdir = os.path.abspath(note_dir)

    if os.path.isdir(srcdir):
        try:
            shutil.copytree(srcdir, destdir, ignore=ignore, symlinks=True)
            print("Info: Notebook files under {} are copied to {}.".format(srcdir, destdir))
        except BaseException as error:
            sys.exit("Error: An exception occurred: {}".format(error))
    else:
        sys.exit("Error: Predefined system notebook directory %s doesn't exist." % srcdir)

if __name__ == "__main__":
    main("gps-1588-ptp")
