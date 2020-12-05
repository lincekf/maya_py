*********************************************
* LINCE FRANCIS								*
* LINCEKF@GMAIL.COM							*
* Poly_ON/OFF Tool 							*
*********************************************

import maya.cmds as cmds

def togglepolygon():


    myPanel = cmds.getPanel(withFocus = True)

    
    if(cmds.modelEditor(myPanel, query = True, pm = True)):
        cmds.modelEditor(myPanel, edit = True,pm = False)
        print "polygon hidden"
    else:
        cmds.modelEditor(myPanel, edit = True, pm = True)
        print "polygon visible"
        
togglepolygon()