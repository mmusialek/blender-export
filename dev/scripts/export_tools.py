import bpy
import datetime
import os


class ExportTools():
    # ------------------------------------------
    # config
    # ------------------------------------------

    base_path = None

    def _traverse_tree(self, t):
        yield t
        for child in t.children:
            yield from self._traverse_tree(child)

    # diselect all
    def unselect_all(self):
        bpy.ops.object.select_all(action='DESELECT')

    def export_obj_exp(self, objects, target_dir):

        #  TODO: check if any of the object is visible
        if not os.path.isdir(target_dir) and objects:
            os.makedirs(target_dir)

        for obj in objects:
            if not  obj.visible_get():
                continue

            print("saving name: {0}, target: {1}".format(obj.name, target_dir))

            obj.select_set(True)
            bpy.ops.object.select_hierarchy(direction='CHILD', extend=True)

            # Export the selected object as fbx
            bpy.ops.export_scene.fbx(check_existing=False,
                                     filepath=target_dir + "\\" + obj.name + ".fbx",
                                     filter_glob="*.fbx",
                                     use_selection=True,
                                     object_types={'MESH', 'ARMATURE'},
                                     bake_anim=True,
                                     bake_anim_use_all_bones=True,
                                     bake_anim_use_nla_strips=True,
                                     bake_anim_use_all_actions=True,
                                     bake_anim_force_startend_keying=True,
                                     bake_anim_simplify_factor=1,
                                     use_armature_deform_only=False,
                                     bake_space_transform=True,
                                     mesh_smooth_type="OFF",
                                     add_leaf_bones=False,
                                     path_mode='ABSOLUTE')

            obj.select_set(False)
            bpy.ops.object.select_all(action='DESELECT')


    # support only 1 deep collection!
    def export_objects_tree(self, collection, target_dir):

        if collection.hide_viewport:
            print("Colleciton {} is hidden ".format(collection.name))
            return

        if collection.has_objects():
            self.export_obj_exp(collection.collection.objects, target_dir)
        else:
            print("No objects for colleciton: " + collection.name)

        for child in collection.children:
            self.export_objects_tree(child, target_dir + child.name + "\\")

    def export_flat(self, collection):

        target_dir = self.base_path

        for coll in self._traverse_tree(collection):
            self.export_obj_exp(coll.objects, target_dir + coll.name + "\\")

    def run(self, context):
        start_time = datetime.datetime.now()
        print("-----------------------------------")
        print("Starting: " + str(start_time))
        print("-----------------------------------")

        filepath = bpy.data.filepath
        directory = os.path.dirname(filepath)
        self.base_path = directory + "\\model-export\\"

        print("saving to:" + self.base_path)

        master_collection = context.view_layer.layer_collection

        self.unselect_all()
        self.export_objects_tree(master_collection, self.base_path)
        end_time = datetime.datetime.now()
        print("Export took: " + str(end_time-start_time))
        print("Finished!!!")
