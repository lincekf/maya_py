# We need 2 object for this. select 2 objects one by one.. 
# First selection will be the one used for instances 
# Second selection will be used to drive the instances


import maya.cmds as cd 
import random 

random.seed(123445)

#Identify the the selection order
result = cd.ls(orderedSelection = True )

# Identify the first and second selection
transformname1 = result[0]
transformname2 = result[1]

# Create one Empty Group
GROUP = cd.group(empty = True, name = transformname1 + "_Maingrp#" )

    
for i in range(1,25):
    
    # Create the 25 instance of first selected object 
    instanceresult = cd.instance(transformname1, name = transformname1 + "_instance#")
    
    # add the instance objects in to the empty group created earlier
    cd.parent(instanceresult, GROUP)  
    
    # Pick the random values for move, rotate & scale
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
    
  
# detect all the instances created with name includes 'instance"
instance_select = cd.ls("*_instance*")

# select all the detected objects
cd.select(instance_select)

#detect the selection order
sele_list = cs.ls(orderedSelection = True)

# Aim constrain the instances one by one to the second selection 
for obj in sele_list:
	cs.aimConstraint (transformname2,obj, aimVector = [0,1,0])


