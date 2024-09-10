import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped #AckermannDrive

class Relay(Node):
    def __init__(self):
        super().__init__('relay')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10) 
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            'drive',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
    def listener_callback(self, msg):
        self.get_logger().info('steering_angle_orignal: "%f"' % msg.drive.steering_angle)
        self.get_logger().info('speed_orignal: "%f"' % msg.drive.speed)
        msg.drive.steering_angle *= 3
        msg.drive.speed *= 3
        self.get_logger().info('steering_angle_updated: "%f"' % msg.drive.steering_angle)
        self.get_logger().info('speed_updated: "%f"' % msg.drive.speed)
       # self.publisher_.publish(msg)
def main(args=None):
    rclpy.init(args=args)

    relay = Relay()

    rclpy.spin(relay)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    relay.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
