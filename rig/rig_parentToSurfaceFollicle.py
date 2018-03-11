import maya.cmds as mc

def rig_parentToSurfaceFollicle ( transformNode, meshOrSurface, parentType):
    shape = mc.listRelatives ( meshOrSurface, s=True )
    type = mc.objectType (shape)
    if type == 'mesh':
        closestPoint = mc.createNode ( 'closestPointOnMesh' )
        decMatrix = mc.createNode ( 'decomposeMatrix' )
        mc.connectAttr ( (transformNode+'.worldMatrix'), (decMatrix+'.inputMatrix') )
        mc.connectAttr ( (decMatrix+'.outputTranslate'),  closestPoint+'.inPosition')
        mc.connectAttr ( (shape[0]+'.outMesh'), (closestPoint+'.inMesh') )
    elif type == 'nurbsSurface':
        closestPoint = mc.createNode ( 'closestPointOnSurface' )
        decMatrix = mc.createNode ( 'decomposeMatrix' )
        mc.connectAttr ( (transformNode+'.worldMatrix'), (decMatrix+'.inputMatrix') )
        mc.connectAttr ( (decMatrix+'.outputTranslate'),  closestPoint+'.inPosition')
        mc.connectAttr ( (shape[0]+'.local'), (closestPoint+'.inputSurface') )


    u = mc.getAttr ( (closestPoint+'.result.parameterU') )
    v = mc.getAttr ( (closestPoint+'.result.parameterV') )
    #print ( 'U coordinate: '+u ) REFORMAT ??
    #print ( 'V coordinate: '+v ) REFORMAT ??
    mc.delete ( closestPoint )

    follicleShape = mc.createNode ( 'follicle' )
    follicle = mc.listRelatives ( follicleShape, p=True )
    mc.setAttr ( (follicle[0]+'.inheritsTransform'), 0 )
    #print follicle
    mc.connectAttr ( follicleShape+'.outRotate', (follicle[0]+'.rotate') )
    mc.connectAttr ( follicleShape+'.outTranslate', (follicle[0]+'.translate') )
    mc.setAttr ( follicleShape+'.parameterU', u )
    mc.setAttr ( follicleShape+'.parameterV', v )
    if type == 'mesh':
        mc.connectAttr ( shape[0]+'.worldMatrix', (follicleShape+'.inputWorldMatrix') )
        mc.connectAttr ( shape[0]+'.outMesh', (follicleShape+'.inputMesh') )
    elif type == 'nurbsSurface':
        mc.connectAttr ( shape[0]+'.worldMatrix', (follicleShape+'.inputWorldMatrix') )
        mc.connectAttr ( shape[0]+'.local', (follicleShape+'.inputSurface') )

    mc.setAttr ( transformNode+".tx" , l=False)
    mc.setAttr ( transformNode+".ty" , l=False)
    mc.setAttr ( transformNode+".tz" , l=False)
    mc.setAttr ( transformNode+".rx" , l=False)
    mc.setAttr ( transformNode+".ry" , l=False)
    mc.setAttr ( transformNode+".rz" , l=False)
    mc.setAttr ( transformNode+".sx" , l=False)
    mc.setAttr ( transformNode+".sy" , l=False)
    mc.setAttr ( transformNode+".sz" , l=False)
    if parentType == 'parent':
        mc.parent ( transformNode, follicle )
    elif parentType == 'constraint':
        mc.parentConstraint ( follicle, transformNode, mo=True )

rig_parentToSurfaceFollicle ( 'locator1', 'nurbsPlane1', 'parent')
