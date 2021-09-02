import bpy
from .export_tools import ExportTools

bl_info = {
    "author": "Marcin Musiałek",
    "name": "Export all to fbx",
    "version": (0, 0, 7),
    "blender": (2, 80, 0),
    "category": "All",
    "description": "Exports all objects to fbx file as single object.",
}


class ExportToolsRuner(bpy.types.Operator):
    """Export all to fbx"""
    bl_idname = "scene.export_all_objects_to_fbx"
    bl_label = "Export all to fbx"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        et = ExportTools()
        et.run(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ExportToolsRuner.bl_idname)

def register():
    bpy.utils.register_class(ExportToolsRuner)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ExportToolsRuner)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()