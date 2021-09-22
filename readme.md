# Blender addon - info
Addon for exporting all objects from all visible collections in active scene.


# Installation
* Download zip file 
* Open Blender and navigate to _Edit -> Preferences_. Press _install_ button and choose your downloaded file.
* Activate addon: **Export all to fbx**

# Usage
Plugin is located when in the **Object** mode in the **Object** menu.
After clicking export all objects will be exported from all collections.

## Limitations
* Only objects from the visible collections will be exported.
* 1 deep down collection support
* _.fbx_ files are saved in the fixed location. In the _.blend_ file directory in the _model-export_ subdirectory.


## Change log
Changes in given versions:

### version 0.0.9
* do not export not visible objects when collection is visible
* select children of the selected object

### version 0.0.8
* export separate objects in all collections to the separate *.fbx files
* export only objects from visible collections