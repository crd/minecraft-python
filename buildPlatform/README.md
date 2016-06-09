# BuildPlatform

This super simple script was created to ensure python could be written that would execute on Raspbian's minecraft-pi as well as Spigot servers augmented with RaspberryJuice.

This script will watch to see if the player has moved. If so, it will check the nine tiles directly beneath the player. If any are air, it will set them to the specified material.

## Prerequisites

### On a Mac

1. Download and execute BuildTools.jar installer from the Spigot site: https://www.spigotmc.org/

2. Download and install the RaspberryJuice mod and drop the .jar in the plugins directory in the root of the directory where you installed BuildTools: http://dev.bukkit.org/bukkit-plugins/raspberryjuice/

3. Download this modded mcpi directory and drop it in the same location where you'll be executing your minecraft python scripts: https://github.com/zhuowei/RaspberryJuice/tree/master/src/main/resources/mcpi/api/python

4. Start Spigot:

````
$ java -Xms512M -Xmx1G -XX:+UseConcMarkSweepGC -jar spigot-1.9.4.jar
````

### On Minecraft Pi

1. If your pi isn't currently up to date, take care of that first:

````
$ sudo apt-get update && sudo apt-get dist-upgrade
$ reboot 
````

2. Next, if you don't have minecraft-pi install it:

````
$ sudo apt-get install minecraft-pi
````

## How to Use

Download and execute this script from the commandline:

````
$ python buildPlatform.py
````