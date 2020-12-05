import maya.cmds as cmds

# this function returns the camera focal, sensor height & width. This will be later used to comapre 2 cameras. 
# '.2f' will pick only 2 decimal, eg - incase if attribute value 12.356487, will pick only 12.35
def cam_settings(cam):
	fl = format((cmds.getAttr('%s.fl' %cam)), '.2f') 
	cw = format((cmds.getAttr('%s.hfa' %cam)), '.2f')
	ch = format((cmds.getAttr('%s.vfa' %cam)), '.2f')
	return fl, cw, ch

# this function will be used to parent, scale & delete its constraint after use.
def constrain_delete(target, source, constrain = True, scale = False):
	constrain = cmds.parentConstraint(target, source, mo=False)
	scale = cmds.scaleConstraint(target, source, mo=False)
	cmds.select(source)
	cmds.delete(cn=True)

def type_check(sele):
	for sel in sele:
		cam1 = cmds.listRelatives(sel, fullPath = True, type = 'camera')
		if not cam1:
			raise ValueError('Select 2 CAMERAS.')
		else:
			pass



sele = cmds.ls(orderedSelection=True)

# check if selection is exactly 2
if len(sele) != 2:
	raise ValueError('Select 2 cameras. Parent & Child !')

# we will makesure user selected only cameras.
type_check(sele)

# defining the first and second cameras in order.
parent_camera = sele[0]
child_camera = sele[1]			


# to pick the camera shape 
parent_camera_shape = cmds.listRelatives(parent_camera,fullPath = True, type = 'camera')[0]
child_camera_shape = cmds.listRelatives(child_camera, fullPath = True,type = 'camera')[0]

# checking if both camera shape has same properties and warn user if any change
if cam_settings(parent_camera_shape) != cam_settings(child_camera_shape):
    cmds.warning("Camera settings are not matching. Constrain was successful anyways !")


loc = cmds.spaceLocator(n = 'track_camera_loc')[0]
constrain_delete( child_camera, loc)

# finding the parent group of the cameras
parent_camera_Grp = cmds.listRelatives(parent_camera, parent=True)
child_camera_Grp = cmds.listRelatives(child_camera, parent = True)

# Condition to check if the camera has any parent group
if not child_camera_Grp:
	cmds.parent(child_camera, loc)
else:
	cmds.parent(child_camera_Grp, loc)

# bringing child camera to the parent cam position
constrain_delete(parent_camera, loc)

# matching the scale of the parent camera
if not parent_camera_Grp:
	constrain_delete(parent_camera, loc, constrain = False, scale = True)

cmds.select(loc)