import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from std_msgs.msg import String

class AutonomousNavigation(Node):
    def __init__(self):
        super().__init__('autonomous_navigation')
        
        self.goal_pub = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.amcl_callback, 10)
        self.create_subscription(String, '/aruco_topic', self.aruco_callback, 10)
        
        self.puerta = {'x': 3.522, 'y': 1.098, 'z': 0.701, 'w': 0.713}
        
        self.destinos = {
            '5': {'x': 3.522, 'y': 3.500, 'z': 0.701, 'w': 0.713},
        }
        
        self.estado = 'YENDO_A_PUERTA'
        self.timer = self.create_timer(2.0, self.iniciar_ruta)

    def publicar_meta(self, coords):
        msg = PoseStamped()
        msg.header.frame_id = 'map'
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose.position.x = coords['x']
        msg.pose.position.y = coords['y']
        msg.pose.orientation.z = coords['z']
        msg.pose.orientation.w = coords['w']
        self.goal_pub.publish(msg)

    def iniciar_ruta(self):
        self.publicar_meta(self.puerta)
        self.get_logger().info('Fase 1: Yendo hacia la puerta del laboratorio...')
        self.timer.cancel()

    def amcl_callback(self, msg):
        if self.estado == 'YENDO_A_PUERTA':
            dx = msg.pose.pose.position.x - self.puerta['x']
            dy = msg.pose.pose.position.y - self.puerta['y']
            if math.hypot(dx, dy) < 0.35:
                self.estado = 'ESPERANDO_ARUCO'
                self.get_logger().info('Llegada a la puerta. Esperando lectura del ArUco 5...')

    def aruco_callback(self, msg):
        if self.estado == 'ESPERANDO_ARUCO':
            aruco_id = msg.data.strip()
            if aruco_id in self.destinos:
                self.publicar_meta(self.destinos[aruco_id])
                self.estado = 'YENDO_A_DESTINO'
                self.get_logger().info(f'ArUco ID {aruco_id} detectado -> Yendo al destino final dentro del laboratorio.')

def main(args=None):
    rclpy.init(args=args)
    nodo = AutonomousNavigation()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()