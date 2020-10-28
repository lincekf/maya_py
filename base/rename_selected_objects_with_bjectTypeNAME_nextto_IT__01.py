import maya.cmds as cmds

sele = cmds.ls(selection = True)

for obj in sele:
	typp = cmds.listRelatives(obj,children = True, fullPath = True) or []

	if len(typp) == 1:
		typp2 = typp[0] 
		typp3 = cmds.objectType(typp2)
		print typp3
	else:
		typp3 = cmds.objectType(obj)
		print typp3
	
	cmds.rename(obj, obj + '__' + typp3)





