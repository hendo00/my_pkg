from launch import LaunchDescription
from launch_ros.actions import Node
param_file = "home/robo/ahmed_ws/src/my_pkg/config/params.yaml"
def generate_launch_description():
    param_reader_cmd = Node(
        package='my_pkg',
        executable='param_reader',
        parameters=[
        # Manaul
        #     {
        #     'particles':300,
        #     'topics': ['scan', 'image'],
        #     'topic_types': ['sensor_msgs/msg/LaserScan', 'sensor_msgs/msg/Image']
        # }
        param_file
        ],
        output='screen'

    )
    ld = LaunchDescription()
    ld.add_action(param_reader_cmd)
    return ld

