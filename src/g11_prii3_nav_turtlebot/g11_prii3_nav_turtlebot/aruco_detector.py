import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2

class ArucoDetector(Node):
    def __init__(self):
        super().__init__('aruco_detector')
        
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )
        
        self.publisher_ = self.create_publisher(String, '/aruco_topic', 10)
        self.bridge = CvBridge()
        
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
        self.aruco_params = cv2.aruco.DetectorParameters_create()
        
        self.get_logger().info('Nodo detector de ArUcos (DICT_4X4_100) iniciado.')

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        corners, ids, _ = cv2.aruco.detectMarkers(
            frame, self.aruco_dict, parameters=self.aruco_params
        )
        
        if ids is not None:
            for marker_id in ids.flatten():
                id_str = str(marker_id)
                out_msg = String()
                out_msg.data = id_str
                self.publisher_.publish(out_msg)
                self.get_logger().info(f'ArUco detectado -> ID: {id_str}', throttle_duration_sec=1.0)

def main(args=None):
    rclpy.init(args=args)
    nodo = ArucoDetector()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()