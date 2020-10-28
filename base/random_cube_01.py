import maya.cmds as cd 
import random 

random.seed(1234)

mylist = cd.ls("lince*")

if len(mylist) > 0:
    cd.delete (mylist)
    
result = cd.polyCube( w = 1, h = 1, d = 1, name = "linceCube#" )
    
transformname = result[0]

GROUP = cd.group(empty = True, name = transformname + "_instancegrp#" )
    
for i in range(1,25):
    
    instanceresult = cd.instance(transformname, name = transformname + "_instance#")
    
    cd.parent(instanceresult, GROUP)  
    
    x = random.uniform(-10,10)
    y = random.uniform(0, 20)
    z = random.uniform(-10, 10)
       
    cd.move (x, y, z, instanceresult )
    
    xrot = random.uniform(0,360)
    yrot = random.uniform(0,360)
    zrot = random.uniform(0,360)
    
    cd.rotate(xrot, yrot, zrot, instanceresult)
    
    scFactor = random.uniform ( .8, 1.8 )
    
    cd.scale( scFactor, scFactor, scFactor, instanceresult )
    
#cd.hide(transformname)

