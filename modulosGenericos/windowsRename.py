# -*- encoding: utf-8 -*-
# @Date:   2018-03-17T11:57:09-03:00
# @Last modified time: 2018-03-17T12:52:40-03:00
#-------------------------------------------------------------------------
# UI functions
#-------------------------------------------------------------------------
import maya.cmds as cmds

# Window NameToRename
def windowRename(nWin='NameToRename', nota='Niko Rename', nota2='Rename'):

    if cmds.window(nWin, ex=True):
        cmds.deleteUI(nWin)
    cmds.window(nWin, title=nota, s=False, width=300,
                height=100, bgc=(0.25, 0.27, 0.29))
    cmds.columnLayout(adjustableColumn=True)
    cmds.textFieldGrp(nWin + 'FieldsN', label='Name Objects:',
                      ann='Here you put the name of the object')
    cmds.textFieldGrp(nWin + 'FieldS', label='Suffix Objets:',
                      ann='Here you put the name of the suffix')
    cmds.columnLayout(adjustableColumn=True)
    cmds.button(nWin + 'btn', label=nota2, command=rename,
                annotation=nota2, w=50, h=50)
    cmds.showWindow(nWin)


def rename(arg):

    if len(cmds.ls(sl=True)) == 0:
        print 'Selecciona algo porfa.'
        return

    nameObject = str(cmds.textFieldGrp(
        'NameToRenameFieldsN', q=True, text=True))
    suffixObjects = str(cmds.textFieldGrp(
        'NameToRenameFieldS', q=True, text=True))
    if nameObject != "" and suffixObjects != "":
        funcionRename(nameObject, suffixObjects.upper())
        print 'new names of the objects are:'
        print 'The Object is: ' + nameObject
        print 'The Suffix is: ' + suffixObjects
    else:
        print 'You need write something.'


#-------------------------------------------------------------------------
# Funcion para renombrar y colocar sufijo
def funcionRename(nameObj, sufijoObj):
    lista = cmds.ls(sl=True, r=True)
    contador = 00
    for obj in lista:
        try:
            cmds.rename(obj, nameObj + str(contador) + '_' + sufijoObj)
            contador += 01
        except:
            print ('I can not rename the object')
