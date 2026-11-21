import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point, PoseStamped

class PuenteNavegacion(Node):
    def __init__(self):
        super().__init__('puente_navegacion')
        self.sub = self.create_subscription(Point, '/mis_coordenadas', self.callback, 10)
        self.pub = self.create_publisher(PoseStamped, '/goal_pose', 10)

    def callback(self, msg):
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.header.stamp = self.get_clock().now().to_msg()
        goal.pose.position.x = msg.x
        goal.pose.position.y = msg.y
        goal.pose.orientation.w = 1.0
        self.pub.publish(goal)
        self.get_logger().info(f'Moviendo robot a X: {msg.x}, Y: {msg.y}')

def main(args=None):
    rclpy.init(args=args)
    nodo = PuenteNavegacion()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()