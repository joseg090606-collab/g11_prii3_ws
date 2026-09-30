import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool, Empty
from turtlesim.srv import SetPen, TeleportAbsolute

class TurtleControl(Node):
    def __init__(self):
        super().__init__('turtle_control_g11')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Servicios PBI 
        self.srv_pause = self.create_service(SetBool, 'pause_resume', self.pause_callback)
        self.srv_restart = self.create_service(Empty, 'restart', self.restart_callback)
        
        # Clientes de turtlesim 
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.is_paused = False
        self.step = 0
        
        self.sequence = [
            (-2.0, 0.0, 1),    
            (1.0, 0.0, 0),     
            (-0.5, 0.0, 0),    
            (0.0, 1.57, 0),    
            (2.5, 0.0, 0),     
            (0.0, 2.356, 0),   
            (0.8, 0.0, 0),     
            (-0.8, 0.0, 1),    
            (0.0, 0.785, 1),  
            (2.5, 0.0, 1),    
            (0.0, 1.57, 1),    
            (2.0, 0.0, 1),     
            (1.0, 0.0, 0),     
            (-0.5, 0.0, 0),    
            (0.0, 1.57, 0),    
            (2.5, 0.0, 0),     
            (0.0, 2.356, 0),   
            (0.8, 0.0, 0),     
            (0.0, 0.0, 1)      
        ]

    def call_set_pen(self, off):
        if self.pen_client.wait_for_service(timeout_sec=1.0):
            req = SetPen.Request()
            req.r = 255; req.g = 255; req.b = 255; req.width = 3
            req.off = off
            self.pen_client.call_async(req)

    def center_turtle(self):
        if self.teleport_client.wait_for_service(timeout_sec=1.0):
            req = TeleportAbsolute.Request()
            req.x = 5.544445
            req.y = 5.544445
            req.theta = 0.0  
            self.teleport_client.call_async(req)

    def pause_callback(self, request, response):
        self.is_paused = request.data
        response.success = True
        return response

    def restart_callback(self, request, response):
        self.step = 0
        self.is_paused = False
        self.call_set_pen(0)
        self.center_turtle() 
        return response

    def timer_callback(self):
        if self.is_paused:
            return
            
        if self.step == len(self.sequence):
            self.center_turtle()
            self.step += 1
            return
        elif self.step > len(self.sequence):
            return 
        
        current = self.sequence[self.step]
        self.call_set_pen(current[2])
        
        msg = Twist()
        msg.linear.x = current[0]
        msg.angular.z = current[1]
        self.publisher_.publish(msg)
        
        self.step += 1

def main():
    rclpy.init()
    node = TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

