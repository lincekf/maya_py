# This Cone_maker code will create cones on top of the selected locator and place it under the same locator group if available. 
			# you just have to select your locator where you wanted the cones and run this code. 

import maya.cmds as cmds 

			# detecting only locators from selection
maya.cmds.ls(selection = True)
locator_sele = cmds.listRelatives(cmds.listRelatives(type="locator"),p=True)

x = 1

			# Finding which groups these locators belongs to. So we can create the cones under the same group
			# OR
			# This code will ignore the group search if the locators are not in part of any group.
first_loc = locator_sele[0]
try:
	find_loc_parent_grp = cmds.listRelatives(first_loc, p=True)
	root_grp = find_loc_parent_grp[0]
	x = x + 1
except:
	pass

			# Creates group for the newly created cones inside the locator parent group & Making a child of the parent group.
			# OR
			# Creates a free group in outliner if there are no parent group available for locator
if x == 2:
	cone_grp = cmds.group(em=True, name='%s_cone' % root_grp, parent=root_grp)
else:
	cone_grp = cmds.group(em = True, name = 'cone_Group')

			
			# loop all the selected locator and place a cone on op of it
for obj in locator_sele:
	
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