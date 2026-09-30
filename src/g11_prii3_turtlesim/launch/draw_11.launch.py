from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlesim', executable='turtlesim_node', name='sim'),
        Node(package='g11_prii3_turtlesim', executable='control_node', name='control_node')
    ])
