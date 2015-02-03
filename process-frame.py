#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

GridPP and DIRAC: processing CERN@school frames on the grid.

"""

#..for the operating system commands.
import os

#...for parsing the arguments.
import argparse

#...for the logging.
import logging as lg

# Import the JSON library.
import json

if __name__ == "__main__":

    print("*")
    print("*=========================================================*")
    print("* GridPP and CVMFS - CERN@school frame processing example *")
    print("*=========================================================*")

    # Get the datafile path from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("inputPath",  help="Path to the input dataset.")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
    args = parser.parse_args()

    ## The path to the data file.
    datapath = args.inputPath

    # Set the logging level to DEBUG.
    if args.verbose:
        level=lg.DEBUG
    else:
        level=lg.INFO

    # Configure the logging.
    lg.basicConfig(filename='log_process-frames.log', filemode='w', level=level)

    print("*")
    print("* Input file          : '%s'" % (datapath))
    print("*")

    ## The data file to read in.
    df = open(datapath, "r")

    # Read the data file and close it.
    lines = df.readlines()
    df.close()

    lg.info(" *===============================================*")
    lg.info(" * GridPP and CVMFS: remote data processing test *")
    lg.info(" *===============================================*")
    lg.info(" *")
    lg.info(" * Input file          : '%s'" % (datapath))
    lg.info(" *")

    lg.info(" * Number of lines (pixels) in the file: %d" % (len(lines)))
    lg.info(" *")

    ## A dictionary of pixels {X:C}.
    pixels = {}

    for l in lines:

        ## The pixel values extracted from the data file.
        vals = l.strip().split("\t")

        ## The pixel x coordniate.
        x = int(vals[0])

        ## The pixel y coordinate.
        y = int(vals[1])

        # The pixel count value.
        C = int(vals[2])

        X = (256 * y) + x

        # Assign the pixel to the dictionary.
        pixels[X] = C

        lg.info(" *--> Found pixel at (% 3d, % 3d) -> (% 5d) = % 10d [counts]." % (x, y, X, C))

    # Write the JSON file containing information about the data.

    ## The file information JSON (for writing).
    file_info = {
        'file_name' : '%s' % (datapath),
        'n_pixel'   : len(pixels),
        'max_count' : max(pixels.values())
        }

    with open("file-info.json", "w") as jf:
        json.dump(file_info, jf)
