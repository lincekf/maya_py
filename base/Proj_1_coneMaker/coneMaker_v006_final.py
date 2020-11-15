import maya.cmds as cmds

# -- BackEnd Code -- #

# A function to apply red material for the cones .
def assign_mat(Scone):
	    
	def mat():
		R,G,B = 1,0,0

		shaderSG = cmds.sets(name = 'lambertA_matSG', em = 1, renderable = 1, noSurfaceShader = 1)
		
		cmds.connectAttr('lambertA_mat.outColor', '%s.surfaceShader' % shaderSG)
		
		cmds.sets(Scone, e=1, forceElement = shaderSG)
		
		cmds.setAttr(('lambertA_mat.incandescence'),R,G,B, type = 'double3')
		cmds.setAttr(('lambertA_mat.color'), R,G,B, type = 'double3')
	
	
	if cmds.objExists('lambertA_mat'):
		mat()			
		
		
	else:

		cmds.shadingNode('lambert', name = 'lambertA_mat', asShader = True)
		mat()


# This function will be used for changing the colors of the cones			
def edit_mat(R,G,B):
	
	cmds.setAttr(('lambertA_mat.incandescence'),R,G,B, type = 'double3', edit = True)
	cmds.setAttr(('lambertA_mat.color'), R,G,B, type = 'double3')
	
	

cmds.ls(selection=True)

locator_sele = cmds.listRelatives(cmds.listRelatives(type="locator"),p=True)  #Picking only locators from selection

#Picking the first locator from selected locators. If no selection we raise a ValueError
if locator_sele:
	first_loc = locator_sele[0]
else:
	raise ValueError("Please Select one or more Locators. I can work only with locators.")


loc_parent_grp = cmds.listRelatives(first_loc, p=True)

if loc_parent_grp:
	root_grp = loc_parent_grp[0]
	cone_grp = cmds.group(em=True, name='%s_cone' % root_grp, parent=root_grp)
else:
	cone_grp = cmds.group(em = True, name = 'cone_Group#')

conet = [] # Empty Lists to add transform nodes of the cones
cones = []  # Empty Lists to add shape nodes of the cones

# loop all the selected locator and place a cone on op of it
for obj in locator_sele:

	# Creating a cone and adding that under the cone_group
	cone_new_t,cone_new_s  = cmds.polyCone(r = 1, h = 3.3, name = '%s_%s' % (obj, 'Cone#') )
	cmds.parent(cone_new_t, cone_grp)
	conet.append(cone_new_t)
	cones.append(cone_new_s)

	# Bringing the pivot of the cone in to its own tip
	cone_vtx = cmds.ls('%s.vtx[*]' % (cone_new_t), fl=True)
	cone_tip = cone_vtx[-1]
	vtx_pos = cmds.xform(cone_tip, ws = 1, q = 1, t = 1)
	cmds.move( vtx_pos[0], vtx_pos[1], vtx_pos[2], ['%s.scalePivot' % (cone_new_t), '%s.rotatePivot' % (cone_new_t)], relative=True )
	
	cmds.rotate(0,0,180)
	
	assign_mat(cone_new_t)
	
	cmds.pointConstraint(obj, cone_new_t)
	
	cmds.select(clear=True)

# - # - # -# - # - # -# - # - # -# - # - # -# - # - # -# - # - # -# - # - # -# - # - # -# - # - # -# - # - # -# - # - # -

# -- FrontEnd Code -- #

# to adjust the radius of the cone
def radius(*args):
	
	val = cmds.floatSliderGrp(R_slider, q = True, value = True)
	for cs in cones:
		cmds.setAttr('%s.r' %cs, val, edit = True)

# to adjust the height of the cone	
def height(*args):
	
	val = cmds.floatSliderGrp(S_slider, q = True, value = True)
	for ct in conet:
		cmds.setAttr('%s.scaleY' %ct, val, edit = True)


window_name = 'Lince_cone_maker:v01'

# this below 'If condition' will close the previously opened window if there are any. 
if cmds.window(window_name, query = True, exists = True):
	cmds.deleteUI(window_name)

# Below line will make a window with No minimize/maximize option. Scaling disabled. 
# Fixed a position on the screen where the window supposed to open. 
cmds.window(window_name, tlc = [200,200], mnb = False, mxb = False, s = False)

cmds.columnLayout()

#Creating the slider to adjust the radius
cmds.separator(h = 10)
R_slider = cmds.floatSliderGrp(label = 'radius', min = 0.1, max = 100, value = 1, dragCommand = radius, field = True)

cmds.separator(h = 10)

#Creating the slider to adjust the height
S_slider = cmds.floatSliderGrp(label = 'height', min = 0.1, max = 100, value = 1, dragCommand = height, field = True)
cmds.separator(h = 10)

# below set of codes will be used to pick the color for the cone.
cmds.rowLayout(numberOfColumns = 8)
cmds.separator(style = 'none', w = 105)
cmds.text(l = 'Color')
cmds.button(l = '', bgc = [1,0,0], c = 'edit_mat(1,0,0)')
cmds.button(l = '', bgc = [0,1,0], c = 'edit_mat(0,1,0)')
cmds.button(l = '', bgc = [0,0,1], c = 'edit_mat(0,0,1)')
cmds.button(l = '', bgc = [1,0,1], c = 'edit_mat(1,0,1)')
cmds.button(l = '', bgc = [0,1,1], c = 'edit_mat(0,1,1)')
cmds.button(l = '', bgc = [1,1,0], c = 'edit_mat(1,1,0)')





cmds.showWindow()
