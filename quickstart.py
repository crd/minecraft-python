from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x,y,z = mc.player.getPos()

mc.player.setPos(x, y+10, z)

blockType = mc.getBlock(x, y, z)

print (blockType)

blockType = block.GOLD_BLOCK.id

mc.setBlock(x, y, z, blockType)
