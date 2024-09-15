from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
package_name = 'my_pkg'
param_file = os.path.join(
            get_package_share_directory(package_name), 'config', 'params_joy.yaml')

def generate_launch_description():
    joy = Node(
        package='joy',
        executable= 'joy_node',
        output='screen'
    )

    teleop = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        output='screen',
        parameters=[param_file],
        remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]
    )

    ld = LaunchDescription([
        joy,
        teleop
    ]
    )
    
    return ld
    