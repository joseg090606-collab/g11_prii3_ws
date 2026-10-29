import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry, Path
from std_srvs.srv import SetBool
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
import math

class DrawNumberSim(Node):
    def __init__(self):
        super().__init__('draw_number')

        if not self.has_parameter('use_sim_time'):
            self.declare_parameter('use_sim_time', True)

        self.is_running, self.obstacle_detected = True, False
        self.step, self.start_time = 0, None

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.path_pub = self.create_publisher(Path, '/robot_path', 10)
        self.path_msg = Path()
        self.path_msg.header.frame_id = 'odom'

        self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        qos = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, history=HistoryPolicy.KEEP_LAST, depth=10)
        self.create_subscription(LaserScan, '/scan', self.scan_callback, qos)
        self.create_service(SetBool, '/control_draw', self.control_callback)

        # TRADUCCIÓN DE LA SECUENCIA DE TURTLESIM A TIEMPOS Y VELOCIDADES DE GAZEBO
        # Formato: (vel_lineal [m/s], vel_angular [rad/s], duracion [s])
        self.sequence = [
            # ================= PRIMER 1 =================
            (-0.15, 0.0, 1.5),    # 1. Base (atrás)
            (0.15, 0.0, 3.0),     # 2. Base (adelante)
            (-0.15, 0.0, 1.5),    # 3. Volver al centro
            (0.0, 0.0, 0.5),      # Pausa
            (0.0, 0.5, 3.1416),   # 4. Giro 90° a la izquierda (mira hacia ARRIBA)
            (0.0, 0.0, 0.5),      # Pausa
            (0.15, 0.0, 5.0),     # 5. Sube tronco vertical
            (0.0, 0.0, 0.5),      # Pausa
            (0.0, 0.5, 4.712),    # 6. Giro 135° a la izquierda (apunta ABAJO-IZQUIERDA)
            (0.0, 0.0, 0.5),      # Pausa
            (0.15, 0.0, 1.8),     # 7. Visera diagonal hacia abajo

            # ============= TRANSICIÓN A LA BASE =============
            (-0.15, 0.0, 1.8),    # 8. Retrocede la visera (vuelve a la cima del tronco)
            (0.0, 0.0, 0.5),      # Pausa
            (0.0, 0.5, 1.571),    # 9. Giro 45° a la izquierda (apunta recto hacia ABAJO)
            (0.0, 0.0, 0.5),      # Pausa
            (0.15, 0.0, 5.0),     # 10. Baja por el tronco de regreso a la base
            (0.0, 0.0, 0.5),      # Pausa
            (0.0, 0.5, 3.1416),   # 11. Giro 90° a la izquierda (mira al frente, orientacion inicial)
            (0.0, 0.0, 0.5),      # Pausa
            (0.15, 0.0, 3.5),     # 12. Desplazamiento lateral hasta el punto de inicio del 2° "1"
            (0.0, 0.0, 0.5),      # Pausa

            # ================= SEGUNDO 1 (RÉPLICA EXACTA) =================
            (-0.15, 0.0, 1.5),    # 13. Base (atrás)
            (0.15, 0.0, 3.0),     # 14. Base (adelante)
            (-0.15, 0.0, 1.5),    # 15. Volver al centro
            (0.0, 0.0, 0.5),      # Pausa
            (0.0, 0.5, 3.1416),   # 16. Giro 90° a la izquierda (mira hacia ARRIBA)
            (0.0, 0.0, 0.5),      # Pausa
            (0.15, 0.0, 5.0),     # 17. Sube tronco vertical
            (0.0, 0.0, 0.5),      # Pausa
            (0.0, 0.5, 4.712),    # 18. Giro 135° a la izquierda (apunta ABAJO-IZQUIERDA)
            (0.0, 0.0, 0.5),      # Pausa
            (0.15, 0.0, 1.8)      # 19. Visera diagonal hacia abajo
        ]

        self.create_timer(0.05, self.control_loop)
        self.get_logger().info("=== Nodo draw_number (Secuencia Turtlesim Adaptada) Activo ===")

    def odom_callback(self, msg):
        pose = PoseStamped(header=msg.header, pose=msg.pose.pose)
        self.path_msg.header.stamp = msg.header.stamp
        self.path_msg.poses.append(pose)
        self.path_pub.publish(self.path_msg)

    def scan_callback(self, msg):
        front = [r for r in (msg.ranges[0:20] + msg.ranges[340:360]) if 0.20 < r < msg.range_max and not math.isnan(r)]
        self.obstacle_detected = bool(front and min(front) < 0.30)

    def control_callback(self, req, res):
        self.is_running = req.data
        self.start_time = None
        res.success, res.message = True, f"Ejecución: {self.is_running}"
        return res

    def control_loop(self):
        if not self.is_running or self.obstacle_detected or self.step >= len(self.sequence):
            self.cmd_pub.publish(Twist())
            return

        now = self.get_clock().now()
        if self.start_time is None:
            self.start_time = now

        v_lin, v_ang, duration = self.sequence[self.step]
        if (now - self.start_time).nanoseconds / 1e9 < duration:
            msg = Twist()
            msg.linear.x, msg.angular.z = v_lin, v_ang
            self.cmd_pub.publish(msg)
        else:
            self.cmd_pub.publish(Twist())
            self.step += 1
            self.start_time = None

def main(args=None):
    rclpy.init(args=args)
    node = DrawNumberSim()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()