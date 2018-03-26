import maya.cmds as mc

def namingConv ( side = '', part = '', desc = '', node = '', conv = ''):

    name = 'side_part_desc__node'

    if conv == 'A':
        name = 'side_part_desc__node'
    if conv == 'B':
        name = 'node__part_desc_side'
    if conv == 'C':
        name = 'side_partdesc__node'
    if conv == 'D':
        name = 'side_partdesc__node'

    if side:
        name = name.replace ( 'side', side)
    if part:
        name = name.replace ( 'part', part)
    if desc:
        name = name.replace ( 'desc', desc)
    if node:
        name = name.replace ( 'node', node)

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

'''
name = namingConv ( 'L',  'FFF', 'AAA', '','A')
print name
'''
