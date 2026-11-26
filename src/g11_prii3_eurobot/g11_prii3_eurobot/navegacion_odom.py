import time
import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator


def main():
    rclpy.init()
    nav = BasicNavigator()
    time.sleep(2.0)  # Espera a que Nav2 esté listo (sin AMCL en Eurobot)

    puntos = [
        (0.60, 0.60),
        (0.60, 1.40),
        (2.40, 1.40),
        (2.40, 0.60),
        (1.50, 1.00),
    ]

    for x, y in puntos:
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.header.stamp = nav.get_clock().now().to_msg()
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.orientation.w = 1.0

        nav.goToPose(goal)
        while not nav.isTaskComplete():
            time.sleep(0.1)

        nav.get_logger().info(f'Punto ({x}, {y}) completado.')

    rclpy.shutdown()


if __name__ == '__main__':
    main()