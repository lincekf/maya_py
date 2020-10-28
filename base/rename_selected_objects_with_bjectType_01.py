# Auto rename the selected object / group based on its type

from maya import cmds

# Detect the selections
content_list = cmds.ls(orderedSelection = True)

# pick the object type of the children of the selected object / group 
for obj in content_list:
	type = cmds.listRelatives(obj, children = True, fullPath = True) or []
	
	# choose the object type depends the length of type.
	if len(type) == 1:
		child = type[0]
		objtype = cmds.objectType(child)  
	else:
		objtype = cmds.objectType(obj)
	print objtype
	# assign suffix to every type that we want	
	if objtype == 'mesh':
		suffix = objtype
		
	elif objtype == 'joint':
		suffix = 'bone'
		
	elif objtype == 'nurbsCurve':
		suffix = 'curve'
		
	elif objtype == 'nurbsSurface':
		suffix = 'curve'
			 
	elif objtype == 'ambientLight':
		suffix = 'light'
	
	elif objtype == 'camera':
		suffix = 'render_camera'
			
	else:
		suffix = 'GRP'
	
	# This will avoid renaming it multiple times.
	if obj.endswith(suffix):
		continue
		
		
	#add that suffix to every object/ group selected along with its own name
	newName = obj + '__' + suffix
	cmds.rename(obj, newName)