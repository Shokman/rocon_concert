#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_concert/license/LICENSE
#
##############################################################################
# Imports
##############################################################################

import rospy
import yaml
import rocon_utilities

##############################################################################
# Methods
##############################################################################

INVALID_PARAM = ['name', 'description', 'uuid']


def load_parameters_from_file(parameter_file, namespace, name, load):

    filepath = rocon_utilities.find_resource_from_string(parameter_file)

    with open(filepath) as f:
        params = yaml.load(f)
        for k, v in params.items():
            if k in INVALID_PARAM:
                rospy.logwarn("Service Manager: %s%s [%s]" % (str(k), ' is prohibitted parameter. Ignoring...', name))
            param_name = namespace + '/' + k
            if load:
                rospy.set_param(param_name, v)
            else:
                rospy.delete_param(param_name)