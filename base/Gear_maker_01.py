import maya.cmds as cmds

def createGear(teeth = 10, length = 0.3):
    
    sele = cmds.select("gearpipe")

    cmds.delete()

    print "creating gear", teeth, length

    span = teeth * 2
    #global span
    transfo_node , shape_node = cmds.polyPipe(subdivisionsAxis=span, n = "gearpipe")

    print transfo_node

    print shape_node
    
    sideface = range(span * 2, span * 3, 2)
    
    cmds.select(clear=True)
    
    for face in sideface:
        cmds.select('%s.f[%s]' % (transfo_node, face ), add = True)
    
    extrude = cmds.polyExtrudeFacet(localTranslateZ=length)[0]
    print extrude

    cmds.select(clear=True)

    return transfo_node, shape_node, extrude


#def changeTeeth(shape_node, extrude, teeth=12, length=0.6):
    #cmds.polyPipe(shape_node, edit = True, subdivisionsAxis = 11)




