# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "Eevee Opacity Panel",
    "author": "Dyo-Anima and CDMJ",
    "version": (2, 2, 0),
    "blender": (4, 3, 0),
    "location": "Toolbar > Misc Tab > Opacity",
    "description": "Helper panel for multiple object opacity assignment",
    "warning": "",
    "doc_url": "https://github.com/Dyo-Anima/opacity_helper_updatefix",
    "category": "Object"
}

import bpy

class OBJECT_OT_set_alpha_blend(bpy.types.Operator):
    """Set Alpha Blended"""
    bl_idname = "object.set_alpha_blend"
    bl_label = "Set Alpha Blended"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.active_material:
                obj.active_material.blend_method = 'BLEND'
        return {'FINISHED'}

class OBJECT_OT_set_alpha_hashed(bpy.types.Operator):
    """Set Alpha Dithered (Hashed)"""
    bl_idname = "object.set_alpha_hashed"
    bl_label = "Set Alpha Dithered"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.active_material:
                obj.active_material.blend_method = 'HASHED'
        return {'FINISHED'}

class OBJECT_OT_set_opaque(bpy.types.Operator):
    """Set Opaque"""
    bl_idname = "object.set_opaque"
    bl_label = "Set Opaque"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.active_material:
                obj.active_material.blend_method = 'OPAQUE'
        return {'FINISHED'}

class PANEL_PT_opacity_panel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_idname = "PANEL_PT_opacity_panel"
    bl_space_type = 'VIEW_3D'
    bl_label = "Opacity Settings"
    bl_region_type = "UI"
    bl_category = "Opacity Helper"

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        col.label(text="Change Selected Opacity")
        col.operator("object.set_alpha_blend", text="Alpha Blended")
        col.operator("object.set_alpha_hashed", text="Alpha Dithered")
        col.operator("object.set_opaque", text="Opaque")

classes = (
    OBJECT_OT_set_alpha_blend,
    OBJECT_OT_set_alpha_hashed,
    OBJECT_OT_set_opaque,
    PANEL_PT_opacity_panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
