import maya.cmds as cmds
import random
import functools

def createUI(pWindowTitle, pApplyCallback):

    windowID = 'myWindowID'

    if cmds.window( windowID, exists=True):
        cmds.deleteUI (windowID)

    cmds.window( windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True)

    cmds.rowColumnLayout (numberOfColumns=3, columnWidth=[ (1,75), (2,60), (3, 60)], columnOffset=[ (1,'right', 3) ] )

    cmds.text( label='Random Seed:')

    seedNumber = cmds.intField( minValue=0, maxValue=10000, value=100 )

    cmds.separator (h=10, style='none')

    cmds.text( label='Shield Amount:')

    shieldAmount = cmds.intField( minValue=0, maxValue=1000, value=0 )

    cmds.separator (h=10, style='none')

    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')
    cmds.separator (h=10, style='none')

    cmds.separator (h=10, style='none')

    cmds.button( label='Apply', command=functools.partial( pApplyCallback,
                                                  seedNumber,
                                                  shieldAmount) )

    def cancelCallback(*pArgs):
        if cmds.window( windowID, exists=True):
            cmds.deleteUI (windowID)

    cmds.button( label='Cancel', command=cancelCallback)

    cmds.showWindow()

def ShieldCreation (pSeedNumber, pShieldAmount, seedNumber):

    #seed

    random.seed (seedNumber)

    result = cmds.ls( selection = True)

    seedNumber = cmds.intField( pSeedNumber, query=True, value=True)

    #shields

    shieldAmount = cmds.intField( pShieldAmount, query=True, value=True)

    #print 'result: %s' % (result)

    transformName = result[0]

    instanceGroupName = cmds.group( empty=True, name = transformName + '_instance_grp#')

    for i in range(0, shieldAmount):

        instanceResult = cmds.instance( transformName, name = transformName + '_instance#')

        cmds.parent ( instanceResult, instanceGroupName )

        #print 'instanceResult:' + str( instanceResult )

        x = random.uniform(-10, 10)
        y = random.uniform(0, 20)
        z = random.uniform(-10, 10)

        cmds.move( x, y, z, instanceResult)

        xRot = random.uniform(0, 360)
        yRot = random.uniform(0, 360)
        zRot = random.uniform(0, 360)

        cmds.rotate( xRot, yRot, zRot, instanceResult)

        scalingFactor = random.uniform (0.3, 1.5)

        cmds.scale( scalingFactor, scalingFactor, scalingFactor, instanceResult)

    cmds.hide (transformName)

    cmds.xform( instanceGroupName, centerPivots = True)

def applyCallback ( pSeedNumber, pShieldAmount, *Args):
    
    #print 'Apply button pressed.'

    seedNumber = cmds.intField( pSeedNumber, query=True, value=True)

    shieldAmount = cmds.intField( pShieldAmount, query=True, value=True)

    selectionList  = cmds.ls( selection = True, type = 'transform' )

    for objectName in selectionList:

        ShieldCreation (pSeedNumber, pShieldAmount, seedNumber)

createUI( 'Shield Generator', applyCallback)
