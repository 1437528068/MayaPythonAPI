#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@version: python3
@author: XiaZhao
@contact: 143528068@qq.com
@software: PyCharm
@file: PrintSelect.py
@time: 2018/2/26 23:26
"""

import maya.api.OpenMaya as om


def maya_useNewAPI():
    """
	The presence of this function tells Maya that the plugin produces, and
	expects to be passed, objects created using the Maya Python API 2.0.
	"""
    pass


# command
class PrintSelect(om.MPxCommand):
    kPluginCmdName = "xzPrintSelect"

    def __init__(self):
        om.MPxCommand.__init__(self)

    @staticmethod
    def cmdCreator():
        return PrintSelect()

    def doIt(self, *args):
        selList = om.MGlobal.getActiveSelectionList()
        for i in range(0, om.MSelectionList.length(selList)):
            dagPath = om.MSelectionList.getDagPath(selList, i)
            print om.MDagPath.fullPathName(dagPath)


# Initialize the plug-in
def initializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.registerCommand(
            PrintSelect.kPluginCmdName, PrintSelect.cmdCreator
        )
    except:
        raise Exception(
            "Failed to register command: %s\n" % PrintSelect.kPluginCmdName
        )


# Uninitialize the plug-in
def uninitializePlugin(plugin):
    pluginFn = om.MFnPlugin(plugin)
    try:
        pluginFn.deregisterCommand(PrintSelect.kPluginCmdName)
    except:
        raise Exception(
            "Failed to unregister command: %s\n" % PrintSelect.kPluginCmdName
        )
