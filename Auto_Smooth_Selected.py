
import bpy



class ASS_OT_Auto_Smooth_Selected(bpy.types.Operator):
    """Auto Smooth Selected"""
    bl_idname = "object.auto_smooth_selected"
    bl_label = "Auto Smooth Selected"

    use_auto_smooth: bpy.props.BoolProperty()
    auto_smooth_angle: bpy.props.FloatProperty(subtype="ANGLE")


    def draw(self, context):
        layout = self.layout
        layout.prop(self, "use_auto_smooth", text="Use Auto Smooth")
        layout.prop(self, "auto_smooth_angle", text="Auto Smooth Angle")


    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):

        for object in context.selected_objects:
            if object.type == "MESH":
                object.data.use_auto_smooth = self.use_auto_smooth
                object.data.auto_smooth_angle = self.auto_smooth_angle


        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ASS_OT_Auto_Smooth_Selected.bl_idname, text=ASS_OT_Auto_Smooth_Selected.bl_label)


def register():
    bpy.utils.register_class(ASS_OT_Auto_Smooth_Selected)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ASS_OT_Auto_Smooth_Selected)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
