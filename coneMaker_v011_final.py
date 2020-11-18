

import maya.cmds as cmds

cmds.ls(selection=True)

# detect locator from selection
locator_sele = cmds.listRelatives(cmds.listRelatives(type="locator"),p=True)  #Picking only locators from selection

if not locator_sele:
	raise ValueError("Please Select one or more Locators. I can work only with locators.")
else:
    first_loc = locator_sele[0]

# Finds which group that locator belongs
loc_parent_grp = cmds.listRelatives(first_loc, p=True)

if loc_parent_grp:
	root_grp = loc_parent_grp[0]
	cone_grp = cmds.group(em=True, name='%s_cone' % root_grp, parent=root_grp)
else:
	cone_grp = cmds.group(em = True, name = 'cone_Group#')

cone_transform = [] # Empty Lists to add transform nodes of the cones
cone_shape = []  # Empty Lists to add shape nodes of the cones


new_shade = cmds.shadingNode('lambert', asShader = True)

def assign_mat(Scone):
    R, G, B = 1, 0, 0
    
    shaderSG = cmds.sets(name = 'lambertA_matSG', em = 1, renderable = 1, noSurfaceShader = 1)
    
    cmds.connectAttr('%s.outColor' % new_shade, '%s.surfaceShader' % shaderSG)
    
    cmds.sets(Scone, e=1, forceElement = shaderSG)
    
    edit_mat(R,G,B)


# we need to keep args here so that any additional arguments other than R,G & B will go and stores inside args.
def edit_mat(R,G,B, *args):
		
	cmds.setAttr(('%s.incandescence' % new_shade),R,G,B, type = 'double3', edit = True)
	cmds.setAttr(('%s.color' % new_shade), R,G,B, type = 'double3')
	


# loop all the selected locator and place a cone on op of it
for obj in locator_sele:

	# Creating a cone and adding that under the cone_group
	cone_new_t,cone_new_s  = cmds.polyCone(r = 1, h = 3.3, sa = 3, name = '%s_%s' % (obj, 'Cone#') )
	cmds.parent(cone_new_t, cone_grp)
	cone_transform.append(cone_new_t)
	cone_shape.append(cone_new_s)

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


class Cone_maker(object):


    window_name = 'Lince_cone_maker:v01'

    def show(self):
        
        if cmds.window(self.window_name, query = True, exists = True):
            cmds.deleteUI(self.window_name)
        
        # Below line will make a window with No minimize/maximize option. Scaling disabled. 
        # Fixed a position on the screen where the window supposed to open. 
        cmds.window(self.window_name, tlc = [200,200], mnb = False, mxb = False, s = True)

        self.BuildconeUI()

        cmds.showWindow()

    def BuildconeUI(self):

        column = cmds.columnLayout(adjustableColumn=True)

        cmds.separator(h = 10)
        self.R_slider = cmds.floatSliderGrp(label = 'radius', min = 0.1, max = 100, value = 1, dragCommand = self.radius, field = True)

        cmds.separator(h = 10)

        self.S_slider = cmds.floatSliderGrp(label = 'height', min = 0.1, max = 100, value = 1, dragCommand = self.height, field = True)
        cmds.separator(h = 10)

        row = cmds.rowLayout(numberOfColumns = 8)
        cmds.separator(style = 'none', w = 105)
        cmds.text(l='Color')
        
        #Using lambda for storing *args
        cmds.button(l = '', bgc = [1,0,0], command=lambda *args: edit_mat(1,0,0)) 
        cmds.button(l = '', bgc = [0,1,0], command=lambda *args: edit_mat(0,1,0))
        cmds.button(l = '', bgc = [0,0,1], command=lambda *args: edit_mat(0,0,1))
        cmds.button(l = '', bgc = [1,0,1], command=lambda *args: edit_mat(1,0,1))
        cmds.button(l = '', bgc = [0,1,1], command=lambda *args: edit_mat(0,1,1))
        cmds.button(l = '', bgc = [1,1,0], command=lambda *args: edit_mat(1,1,0))

    def radius(self, *args):
    
        val = cmds.floatSliderGrp(self.R_slider, q = True, value = True)
        for cs in cone_shape:
            cmds.setAttr('%s.r' %cs, val, edit = True)

    def height(self, *args):
        
        val = cmds.floatSliderGrp(self.S_slider, q = True, value = True)
        for ct in cone_transform:
            cmds.setAttr('%s.scaleY' % ct, val, edit=True)
            





