import math
import rclpy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


def main():
    rclpy.init()
    node = rclpy.create_node('vision_navigation')

    ROBOT_ID = 51 #CAMBIAR ESTA ID, NO OLVIDAR, NO OLVIDAR, NO OLVIDAR
    CENTRO = (320.0, 240.0)
    pos = {}
    yaw = 0.0
    ruta = [20, 21, 22, 23, 'CENTRO']
    paso = 0

    pub = node.create_publisher(Twist, '/cmd_vel', 10)

    def odom_cb(msg):
        nonlocal yaw
        q = msg.pose.pose.orientation
        yaw = math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y * q.y + q.z * q.z))

    def aruco_cb(msg, m_id):
        partes = msg.data.split(',')
        pos[m_id] = (float(partes[1].split(':')[1]), float(partes[2].split(':')[1]))

    node.create_subscription(Odometry, '/odom', odom_cb, 10)
    for m_id in [ROBOT_ID, 20, 21, 22, 23]:
        node.create_subscription(String, f'/overhead_camera/aruco_{m_id}', lambda m, i=m_id: aruco_cb(m, i), 10)

    def loop():
        nonlocal paso
        if paso >= len(ruta) or ROBOT_ID not in pos:
            pub.publish(Twist())
            return

        obj = ruta[paso]
        if obj != 'CENTRO' and obj not in pos:
            pub.publish(Twist())
            return

        tx, ty = CENTRO if obj == 'CENTRO' else pos[obj]
        rx, ry = pos[ROBOT_ID]
        dx, dy = tx - rx, -(ty - ry)

        if math.hypot(dx, dy) < 25.0:
            pub.publish(Twist())
            node.get_logger().info(f'Alcanzado: {obj}')
            paso += 1
            return

        err = math.atan2(math.sin(math.atan2(dy, dx) - yaw), math.cos(math.atan2(dy, dx) - yaw))
        cmd = Twist()
        if abs(err) > 0.25:
            cmd.angular.z = max(-0.8, min(0.8, 1.5 * err))
        else:
            cmd.linear.x = 0.12
            cmd.angular.z = max(-0.5, min(0.5, 1.2 * err))
        pub.publish(cmd)

    node.create_timer(0.1, loop)
    rclpy.spin(node)
    pub.publish(Twist())
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()