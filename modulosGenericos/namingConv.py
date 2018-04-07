# @Date:   2018-04-07T11:03:42-03:00
# @Last modified time: 2018-04-07T13:10:31-03:00



import maya.cmds as mc

def namingConv ( side = 'L', part = 'BODY', desc = 'ARM'):
    '''
    side(String) : Side part
    part(String) : part mesh
    desc(String) : description object
    node(String) : type node resume
    '''
    name = 'side_part_desc__node'
    obj = mc.ls ( sl = 1 )
    if len ( obj ) == 1:
        shape = mc.listRelatives ( obj, s = 1)
        if shape:
            node = mc.nodeType ( shape[0] )
        else:
            node = mc.nodeType ( obj )
        name = name.replace ( 'node', node )
        obj = mc.rename ( obj, name)

    return name

def nameingSuf(node = 'MSH'):




'''
name = namingConv ( 'L',  'FFF', 'AAA', '','A')
print name
'''
