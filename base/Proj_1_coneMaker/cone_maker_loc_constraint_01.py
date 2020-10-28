# This line of codes are just very basic. beta version i say. 

# Select the locators and run this code. 

import maya.cmds as cmds 

# This will detect the selection order .
selection_list = cmds.ls(orderedSelection = True)

# then loop one by one selected locators to add the cones in it
for obj in selection_list:
	
	# Creates a new cone 
	new_cone = cmds.polyCone(r = 5, h = 20, name = '%s_cone' % (obj))
	cmds.move(0,10,0)
	cmds.rotate(0,0,180)

	# moved the cone pivot to the tip of the cone ( considering cone is in by default at the origin )
	cmds.move( 0,-10,0, ['%s_cone.scalePivot'% (obj), '%s_cone.rotatePivot'% (obj)], relative=True )

	# constrain the each created cone with the locator by selection order. 
	cmds.pointConstraint(obj, new_cone)
	
	# deselct any selected object . 
	cmds.select(clear = True)