import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped # AckermannDrive

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.declare_parameter('v')
        self.declare_parameter('d')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)        
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    def timer_callback(self):
        msg = AckermannDriveStamped()
        msg.drive.speed = self.get_parameter('v').get_parameter_value().double_value
        msg.drive.steering_angle = self.get_parameter('d').get_parameter_value().double_value
        #msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing_speed: "%f"' % msg.drive.speed)
        self.get_logger().info('Publishing_steering_angle: "%f"' % msg.drive.steering_angle)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
	# Destroy the node explicitly
    # (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
    talker.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
	main()
