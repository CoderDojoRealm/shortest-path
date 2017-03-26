import json;
import math;
import operator;

# -----------------------------------------------
# Process an intersection
#
# Parameters
#
# name: the name of the current path
# data: a dictionary containing the following keys:
#       "driveTime": the time in seconds it takes to drive the segment
#       "stopLightTiming": how many seconds between stop light cycles
#       "stopLightStartTime": when the stop light started the cycle
#       "stopLightStartColour": the starting cycle colour (red, green)
#       "next": a dictionary of further segments we can take
# timer: the current time in seconds
#
def processIntersection(name, data, timer=0):

    print("");
    print("Path:", name)
    print("  - Current timer:", timer, "seconds")
    print("  - Drive Time:", data["driveTime"])


    # drive the road
    timer = timer + data["driveTime"]

    # if the stop light is red, wait until the next cycle
    timer = timer + calculateTimeWaitingAtLights(timer, data)

    # if there is a "next" element in data, parse it as well
    # (this uses recursion to call the same function again)
    if "next" in data.keys():
        for key, value in data["next"].items():
            subName = name + " > " + key
            print ("  - Next:", subName)
            processIntersection(subName, value, timer)
    else:
        print("  - End of the line reached:", name, "=", timer, "seconds")
        timings[name] = timer

# end def ----------------------------------------


# -----------------------------------------------
#
# Work out the colour of the stop light, and, if red,
# return the number of seconds we need to wait until
# it turns green.
#
# This takes the intesection data and the current timer
# to work out whether the light will be red (false) or
# green (true).
#
# Bug: this should take into account "stopLightStartTime"
#
# Parameters:
#
# timer: The current time of the simulation (in secs)
# data: the dictionary of one intersection
#
# Returns:
#
# number of seconds to wait at the lights
def calculateTimeWaitingAtLights(timer, data):

    cycles = timer / data["stopLightTiming"]
    completeCycles = math.floor(cycles)

    print("  - Timer at end of segment:", timer)
    print("  - Traffic Light Cycle:", cycles)

    if isLightRed(completeCycles, data["stopLightStartColour"]):
        # light is red
        # wait time is the percentage o the stop light timing remaining
        waitTime = math.ceil(cycles - completeCycles) * data["stopLightTiming"]
        print("  - Light is RED, waiting", waitTime, "seconds for light to change green")
    else:
        # light is green, no wait time
        waitTime = 0
        print("  - Light is GREEN, can drive through without waiting")

    return waitTime

# end def ----------------------------------------


# -----------------------------------------------
#
# Is the stop light red or green?
#
# Based on the cycle number and starting colour,
# returns the current colour of the light.
#
# Note: % is the "modulus" operator, which returns
# the remainder of a division.
# e.g. 5 / 2 = 2r1, so 5 % 2 returns 1
#
# completeCycles: the last cycle number
# startingColour: "red" or "green"
# returns: boolean
def isLightRed(completeCycles, startingColour):

    # is it the starting colour?
    # this checks whether completeCycles divided by 2
    # has a remainder of 0
    if (completeCycles % 2 == 0):
        # yes
        if startingColour == "red":
            return True
        else:
            return False
    else:
        # no
        if startingColour == "red":
            return False
        else:
            return True

# end def ----------------------------------------


# ------------------------------------------------
# Main Program
# ------------------------------------------------

# Open the data file and reads the contents into a list
file = open("data.json", "r")
fileContents = file.read()
intersectionData = json.loads(fileContents)
print ("File loaded")

# a variable created to track all timings
timings = {};

# Start processing from the first node in the tree
processIntersection("start", intersectionData)

# Print a summary of all timings
print("")
print("Summary of all paths, sorted shortest to longest")
sortedTimings = sorted(timings.items(), key=operator.itemgetter(1))

for name, time in sortedTimings:
    print(time, ":", name)
