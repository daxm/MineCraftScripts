#!/usr/bin/python3

from mcpi.minecraft import Minecraft
import datetime

################
# Changeable Variables
serverip = '127.0.0.1'
recursives = 6  # Remember each new recursion is 27 times larger than the previous one!
# Note: There is a "ceiling" on max build height (default of 256).
# Change it in the minecraft server.properties file before using recursives > 3.
x = 0
y = 0
z = 0

# Do you want to fill the area prior to building on it?
fillBlockType = 0    # AIR
filler = 1

# Do you want to be teleported there when it is done being built?
teleportPlayer = 0
################

# Main Program
programStartTime = datetime.datetime.now()

# Connect to server.
mc = Minecraft.create(address=serverip)

#Fill the area with "fillBlockType".
if filler == 1:
    mc.setBlocks(x,y,z,x+3**recursives,y+3**recursives,z+3**recursives,fillBlockType)

programEndTime = datetime.datetime.now()

# Print info.
print("The program started at ", programStartTime, "\n")
print("The program ended at ", programEndTime, "\n")
diff = programEndTime - programStartTime
print("The program took ", diff, "\n")
print("\n")
print("The program is done.\n")
mc.postToChat("Test is Done")
