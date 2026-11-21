import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class PredefinedNavigation(Node):
    def __init__(self):
        super().__init__('predefined_navigation')
        self.goal_pub = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.timer = self.create_timer(2.0, self.enviar_ruta_fija)

    def enviar_ruta_fija(self):
        goal_msg = PoseStamped()
        goal_msg.header.frame_id = 'map'
        goal_msg.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.position.x = 3.165
        goal_msg.pose.position.y = 13.638
        goal_msg.pose.orientation.z = 0.983
        goal_msg.pose.orientation.w = 0.183
        self.goal_pub.publish(goal_msg)

        self.get_logger().info('Ruta predefinida enviada: Pasillo -> Laboratorio F1L3')
        self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    nodo = PredefinedNavigation()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()