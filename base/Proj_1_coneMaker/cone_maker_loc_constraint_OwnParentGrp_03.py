# This lines of code will create cones on top of the selected locator and place it under the same locator group. 

import maya.cmds as cmds 

selection_list = cmds.ls(orderedSelection = True)

# Finding which groups these locators belongs to. So we can create the cones under the same group
first_loc = selection_list[0]
loc_parent_grp = cmds.listRelatives( first_loc, p=True )[0]

# Making cone group and making it child of the locator group
cone_grp = cmds.group(em = True, name = '%s_cone' % loc_parent_grp, parent = loc_parent_grp)

for obj in selection_list:
	
	# Making a cone and adding that under the cone_group
	cone_new = cmds.polyCone(r = 1, h = 3.3, name = '%s_%s' % (obj, 'Cone') )
	cmds.parent( '%s_%s' % (obj, 'Cone'), cone_grp)
	
	# Bringing the pivot of the cone in to its own tip
	cone_vtx = cmds.ls('%s_%s.vtx[*]' % (obj, 'Cone'), fl=True)
	cone_tip = cone_vtx[-1]
	vtx_pos = cmds.xform(cone_tip, ws = 1, q = 1, t = 1)
	cmds.move( vtx_pos[0], vtx_pos[1], vtx_pos[2], ['%s_%s.scalePivot' % (obj, 'Cone'), '%s_%s.rotatePivot' % (obj, 'Cone')], relative=True )
	
	cmds.rotate(0,0,180)
	
	cmds.pointConstraint(obj, cone_new)
	
	cmds.select(clear = True)
	
