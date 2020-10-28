import maya.cmds as cmds

def assign_mat(Scone):
	
	if cmds.objExists('lambertA'):
				
		shaderSG = cmds.sets(name = 'lambertASG', em = 1, renderable = 1, noSurfaceShader = 1)
		
		cmds.connectAttr('lambertA.outColor', '%s.surfaceShader' % shaderSG)
		
		cmds.sets(Scone, e=1, forceElement = shaderSG)
	
		
	else:

		myshade = cmds.shadingNode('lambert', name = 'lambertA', asShader = True)
		
		shaderSG = cmds.sets(name = '%sSG' % myshade, em = 1, renderable = 1, noSurfaceShader = 1)
		
		cmds.connectAttr('%s.outColor' % myshade, '%s.surfaceShader' % shaderSG)
		
		cmds.sets(Scone, e=1, forceElement = shaderSG)


sele = cmds.ls(selection = True) [0]
assign_mat(sele)

cmds.setAttr(('lambertA.color'), 1,0,1, type = 'double3')
