import maya.cmds as mc

'''
Add movable pivot on transform nodes
'''

def rig_addMovablePivot (transformNode, drivenNode):
    offGrp = mc.createNode ('transform', n = (transformNode+'Offset'))
    parConst = mc.parentConstraint (transformNode, offGrp)
    mc.delete (parConst)
    parentNode = mc.listRelatives (transformNode, p = True)
    pivotCtl = mc.circle (n = (transformNode+'Pivot'))
    parentLocator = mc.spaceLocator (n=(transformNode+'ParentLoc'))
    parConst = mc.parentConstraint (transformNode, pivotCtl[0])
    mc.delete (parConst)
    parConst = mc.parentConstraint (transformNode, parentLocator[0])
    mc.parent (transformNode, pivotCtl[0])
    mc.parent (pivotCtl[0], offGrp)
    mc.parent (parentLocator[0], offGrp)
    if parentNode:
        mc.parent (offGrp, parentNode)
    decMatrix = mc.shadingNode ('decomposeMatrix', asShader=True, n = (transformNode+'DecMatrix'))
    mc.connectAttr ((pivotCtl[0]+'.inverseMatrix'), (decMatrix+'.inputMatrix'))
    mc.connectAttr ((decMatrix+'.outputRotate'), (parConst[0]+'.target[0].targetOffsetRotate'))
    mc.connectAttr ((decMatrix+'.outputTranslate'), (parConst[0]+'.target[0].targetOffsetTranslate'))
    mc.parentConstraint (parentLocator[0], drivenNode)
rig_addMovablePivot ('transformNode', 'drivenNode')
