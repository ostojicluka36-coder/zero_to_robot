import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Dashboard(Node):
    def __init__(self):
        super().__init__('dashboard')
        self.subscription = self.create_subscription(
            Float32, 'battery_level', self.battery_callback, 10)

    def battery_callback(self, msg):
        if msg.data < 20.0:
            self.get_logger().warning(f"Low battery: {msg.data:.1f}%")
        else:
            self.get_logger().info(f"Dashboard sees: {msg.data:.1f}%")


def main(args=None):
    rclpy.init(args=args)

    node = Dashboard()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()