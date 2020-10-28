# This Cone_maker code will create cones on top of the selected locator and place it under the same locator group if available. 
# you just have to select your locator where you wanted the cones and run this code. 

import maya.cmds as cmds

# A function to apply red material for the cones . 
def assign_mat(Scone):
	
	if cmds.objExists('lambertA'):
				
		shaderSG = cmds.sets(name = 'lambertASG', em = 1, renderable = 1, noSurfaceShader = 1)
		
		cmds.connectAttr('lambertA.outColor', '%s.surfaceShader' % shaderSG)
		
		cmds.sets(Scone, e=1, forceElement = shaderSG)
		
		cmds.setAttr(('lambertA.incandescence'), 1,0,0, type = 'double3')
		cmds.setAttr(('lambertA.color'), 1,0,0, type = 'double3')
	
		
	else:

		myshade = cmds.shadingNode('lambert', name = 'lambertA', asShader = True)
		
		shaderSG = cmds.sets(name = '%sSG' % myshade, em = 1, renderable = 1, noSurfaceShader = 1)
		
		cmds.connectAttr('%s.outColor' % myshade, '%s.surfaceShader' % shaderSG)
		
		cmds.sets(Scone, e=1, forceElement = shaderSG)
		
		cmds.setAttr(('lambertA.incandescence'), 1,0,0, type = 'double3')
		cmds.setAttr(('lambertA.color'), 1,0,0, type = 'double3')



maya.cmds.ls(selection = True)
locator_sele = cmds.listRelatives(cmds.listRelatives(type="locator"),p=True)

x = 1
cone_list = []
    

first_loc = locator_sele[0]

try:
	find_loc_parent_grp = cmds.listRelatives(first_loc, p=True)
	root_grp = find_loc_parent_grp[0]
	x = x + 1
except:
	pass

if x == 2:
	cone_grp = cmds.group(em=True, name='%s_cone' % root_grp, parent=root_grp)
else:
	cone_grp = cmds.group(em = True, name = 'cone_Group')


for obj in locator_sele:
	cone_new = cmds.polyCone(r = 1, h = 3.3, name = '%s_%s' % (obj, 'Cone') )
	cmds.parent('%s_%s' % (obj, 'Cone'), cone_grp)
	
	cone_vtx = cmds.ls('%s_%s.vtx[*]' % (obj, 'Cone'), fl=True)
	cone_tip = cone_vtx[-1]
	vtx_pos = cmds.xform(cone_tip, ws = 1, q = 1, t = 1)
	cmds.move( vtx_pos[0], vtx_pos[1], vtx_pos[2], ['%s_%s.scalePivot' % (obj, 'Cone'), '%s_%s.rotatePivot' % (obj, 'Cone')], relative=True )
	
	cone_list.append(cone_new)
	cmds.rotate(0,0,180)
	
	cmds.pointConstraint(obj, cone_new)
	
	assign_mat(cone_new)
	
	cmds.select(clear = True)
	