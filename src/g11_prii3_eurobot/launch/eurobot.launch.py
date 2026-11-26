from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def generate_launch_description():
    modo = LaunchConfiguration('modo')

    return LaunchDescription([
        DeclareLaunchArgument(
            'modo',
            default_value='vision',
            description='Modo de demostracion: "vision" o "odom"'
        ),

        Node(
            package='g11_prii3_eurobot',
            executable='overhead_aruco_detector',
            name='overhead_aruco_detector',
            output='screen',
            emulate_tty=True,
            condition=IfCondition(PythonExpression(["'", modo, "' == 'vision'"]))
        ),

        Node(
            package='g11_prii3_eurobot',
            executable='navegacion_vision',
            name='navegacion_vision',
            output='screen',
            emulate_tty=True,
            condition=IfCondition(PythonExpression(["'", modo, "' == 'vision'"]))
        ),

        Node(
            package='g11_prii3_eurobot',
            executable='navegacion_odom',
            name='navegacion_odom',
            output='screen',
            emulate_tty=True,
            condition=IfCondition(PythonExpression(["'", modo, "' == 'odom'"]))
        ),
    ])