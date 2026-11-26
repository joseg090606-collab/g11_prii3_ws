import cv2
import numpy as np
import rclpy
from std_msgs.msg import String

rclpy.init()
node = rclpy.create_node('overhead_aruco_detector')
cap = cv2.VideoCapture(0)

detector = cv2.aruco.ArucoDetector(
    cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100),
    cv2.aruco.DetectorParameters()
)

pubs = {}
valid_ids = set(range(20, 24)) | set(range(51, 60))

def loop():
    ret, frame = cap.read()
    if not ret:
        return

    corners, ids, _ = detector.detectMarkers(frame)
    vistos = set()

    if ids is not None:
        for i, m_id in enumerate(ids.flatten()):
            m_id = int(m_id)
            if m_id not in valid_ids:
                continue

            vistos.add(m_id)
            if m_id not in pubs:
                pubs[m_id] = node.create_publisher(String, f'/overhead_camera/aruco_{m_id}', 10)

            cx, cy = np.mean(corners[i][0], axis=0)
            pubs[m_id].publish(String(data=f'id: {m_id}, x: {cx:.1f}, y: {cy:.1f}'))

    # Borra los topics de los ArUco que ya no están en cámara
    for m_id in list(pubs.keys() - vistos):
        node.destroy_publisher(pubs.pop(m_id))

node.create_timer(0.05, loop)

try:
    rclpy.spin(node)
except KeyboardInterrupt:
    pass
finally:
    cap.release()
    node.destroy_node()
    rclpy.shutdown()