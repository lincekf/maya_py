import maya.cmds as cmds 

selection_list = cmds.ls(orderedSelection = True, type = "transform")

new_grp = cmds.group(em = True, name = "locator_group")
  
for obj in selection_list:
 	
	target_position = cmds.getAttr( '%s.translate' % (obj)) [0]
		
	new_locator = cmds.spaceLocator( position = target_position, name = "%s_loc#" %(obj))
		
	cmds.xform(new_locator, centerPivots = True)
		
	cmds.parent(new_locator, new_grp)
		
 	