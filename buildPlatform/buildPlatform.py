#!/usr/bin/env python

from mcpi.minecraft import Minecraft
from mcpi import block
import time

""" Minecraft Python Proof of Concept: BuildPlatform v0.1

    This script was created to ensure python could be written that would
    execute on Raspbian's minecraft-pi as well as Spigot servers augmented
    with RaspberryJuice.

    This script will watch to see if the player has moved. If so, it will
    check the nine tiles directly beneath the player. If any are air, it will
    set them to the specified material.

    @author: Cory Donnelly
    """

if __name__ == "__main__":

    # Define the bridge material
    bridgeMaterial = block.GOLD_BLOCK

    #Create connection to minecraft server
    mc = Minecraft.create()

    #Get the player's position
    lastPlayerPos = mc.player.getTilePos()

    while (True):

        #Get the player's position
        playerPos = mc.player.getTilePos()

        #If the player has moved since we last checked
        if (playerPos != lastPlayerPos):

            #Update the type of each block around the player's current position
            #Iterate through the integers (-1, 0, 1)
            for x in range (-1, 2):
                for z in range (-1, 2):
                    if mc.getBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z) == block.AIR:
                        mc.setBlock(playerPos.x + x, playerPos.y - 1, playerPos.z + z, block.GOLD_BLOCK)

        #Store player's current position for the next time we check
        lastPlayerPos = playerPos
