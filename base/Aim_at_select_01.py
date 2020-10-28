#aim at select 

import maya.cmds as cs

sele_list = cs.ls(orderedSelection = True)

if len(sele_list) >2:
	
	target_item = sele_list[0]
	
	sele_list.remove(target_item)
	
	for obj in sele_list:
		
		cs.aimConstraint (target_item,obj, aimVector = [0,1,0])

else:
	print " please select minimum 2 objects"