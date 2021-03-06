[![Build Status](https://travis-ci.org/tahteche/BLA.svg?branch=master)](https://travis-ci.org/tahteche/BLA)

# BLA
Barren Land Analysis: Measure the area of patches of fertile land on a field.

## Problem Statement:

You have a farm of 400m by 600m where coordinates of the field are from (0, 0) to (399, 599). A portion of the farm is barren, and all the barren land is in the form of rectangles. Due to these rectangles of barren land, the remaining area of fertile land is in no particular shape. An area of fertile land is defined as the largest area of land that is not covered by any of the rectangles of barren land. 
Read input from STDIN. Print output to STDOUT

### Input 
You are given a set of rectangles that contain the barren land. These rectangles are defined in a string, which consists of four integers separated by single spaces, with no additional spaces in the string. The first two integers are the coordinates of the bottom left corner in the given rectangle, and the last two integers are the coordinates of the top right corner. 

### Output 
Output all the fertile land area in square meters, sorted from smallest area to greatest, separated by a space. 

### Examples:

**Input**:  `{"0 292 399 307"}`  
**Output**: `116800  116800`

**Input:** `{"48 192 351 207", "48 392 351 407", "120 52 135 547", "260 52 275 547"}`  
**Output:** `22816 192608`

## Running the Code:

After cloning the repo, navigate to the directory of the repo from within your CLI and run the following code - substitute the text in braces accordingly:

`python - m bla < {path/to/file/with/input}`

The input file should contain the input data in the same format as the inputs described in the examples section of the problem statement above and nothing else. Take a look at the  `bla_input.txt` file in the repo for a refernece.
 
 ## Testing:
 
 To run the unit test of the program run the following command in the CLI from within the folder of the repo:
 
 `python -m unittest tests`
 
## Optimizations:

Following is a list of optimizations that were done to make the program more efficient with memory:

 1. Used iteration along with a stack for the implementation of depth-first search in place of recursion.
 2. Used an array as a stack instead of a heavier stack object.
 3. The same grid used to represent the land field was used to keep track of points visited by the DFS instead of using a second grid to keep track of visited points. The later approach would have consumed double the memory.
