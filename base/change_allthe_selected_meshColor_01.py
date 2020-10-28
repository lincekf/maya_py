import maya.cmds as cmds

selections = cmds.ls(sl=True)

for sel in selections:
    # get shape of selection:
    sel_shape = cmds.ls(o=True, shapes=True)
    
    # get shading groups from shape:
    shadingGrps = cmds.listConnections(sel_shape,type='shadingEngine')
    
    # get the shaders:
    shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=True)
    
    # change the color of the material to red
    cmds.setAttr(shaders[0]+".color", 0, 1, 0, type="double3")