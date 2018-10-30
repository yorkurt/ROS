## *********************************************************
##
## File autogenerated for the image_view package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 292, 'description': 'Do dynamic scaling about pixel values or not', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'do_dynamic_scaling', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 292, 'description': 'colormap', 'max': 11, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'colormap', 'edit_method': "{'enum_description': 'colormap', 'enum': [{'srcline': 9, 'description': 'NO_COLORMAP', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': -1, 'ctype': 'int', 'type': 'int', 'name': 'NO_COLORMAP'}, {'srcline': 10, 'description': 'COLORMAP_AUTUMN', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'AUTUMN'}, {'srcline': 11, 'description': 'COLORMAP_BONE', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'BONE'}, {'srcline': 12, 'description': 'COLORMAP_JET', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'JET'}, {'srcline': 13, 'description': 'COLORMAP_WINTER', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'WINTER'}, {'srcline': 14, 'description': 'COLORMAP_RAINBOW', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'RAINBOW'}, {'srcline': 15, 'description': 'COLORMAP_OCEAN', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'OCEAN'}, {'srcline': 16, 'description': 'COLORMAP_SUMMER', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 6, 'ctype': 'int', 'type': 'int', 'name': 'SUMMER'}, {'srcline': 17, 'description': 'COLORMAP_SPRING', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 7, 'ctype': 'int', 'type': 'int', 'name': 'SPRING'}, {'srcline': 18, 'description': 'COLORMAP_COOL', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'COOL'}, {'srcline': 19, 'description': 'COLORMAP_HSV', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 9, 'ctype': 'int', 'type': 'int', 'name': 'HSV'}, {'srcline': 20, 'description': 'COLORMAP_PINK', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 10, 'ctype': 'int', 'type': 'int', 'name': 'PINK'}, {'srcline': 21, 'description': 'COLORMAP_HOT', 'srcfile': '/home/adam/catkin_ws/src/image_pipeline/image_view/cfg/ImageView.cfg', 'cconsttype': 'const int', 'value': 11, 'ctype': 'int', 'type': 'int', 'name': 'HOT'}]}", 'default': -1, 'level': 0, 'min': -1, 'type': 'int'}, {'srcline': 292, 'description': 'Minimum image value for scaling depth/float image.', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'min_image_value', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 292, 'description': 'Maximum image value for scaling depth/float image.', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_image_value', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

ImageView_NO_COLORMAP = -1
ImageView_AUTUMN = 0
ImageView_BONE = 1
ImageView_JET = 2
ImageView_WINTER = 3
ImageView_RAINBOW = 4
ImageView_OCEAN = 5
ImageView_SUMMER = 6
ImageView_SPRING = 7
ImageView_COOL = 8
ImageView_HSV = 9
ImageView_PINK = 10
ImageView_HOT = 11
