from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='g11_prii3_nav_turtlebot',
            executable='aruco_detector',
            name='aruco_detector',
            output='screen',
            emulate_tty=True
        ),
        Node(
            package='g11_prii3_nav_turtlebot',
            executable='autonomous_navigation',
            name='autonomous_navigation',
            output='screen',
            emulate_tty=True
        )
    ])