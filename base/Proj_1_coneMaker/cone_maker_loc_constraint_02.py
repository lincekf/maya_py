import maya.cmds as cmds 

selection_list = cmds.ls(orderedSelection = True)

#first_loc = selection_list[0]


cone_grp = cmds.group(em = True, name = 'cone_group', parent = 'group1')

for obj in selection_list:
	
	cone_new = cmds.polyCone(r = 1, h = 3.3, name = '%s_%s' % (obj, 'Cone') )
	
	cmds.parent( '%s_%s' % (obj, 'Cone'), cone_grp)
	
	cone_vtx = cmds.ls('%s_%s.vtx[*]' % (obj, 'Cone'), fl=True)
	
	cone_tip = cone_vtx[-1]
	
	vtx_pos = cmds.xform(cone_tip, ws = 1, q = 1, t = 1)
	
	cmds.move( vtx_pos[0], vtx_pos[1], vtx_pos[2], ['%s_%s.scalePivot' % (obj, 'Cone'), '%s_%s.rotatePivot' % (obj, 'Cone')], relative=True )
	
	cmds.rotate(0,0,180)
	
	cmds.pointConstraint(obj, cone_new)
	
	cmds.select(clear = True)
	
