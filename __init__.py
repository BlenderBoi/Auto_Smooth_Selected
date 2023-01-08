

bl_info = {
    "name": "Auto Smooth Selected",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "description": "",
    "warning": "",
    "location": "Object > Auto Smooth Selected",
    "wiki_url": "",
    "category": "Utility",
}

import bpy
from . import Auto_Smooth_Selected


modules = [Auto_Smooth_Selected]

def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
