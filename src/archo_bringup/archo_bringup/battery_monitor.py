import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')
        self.publisher_ = self.create_publisher(Float32, 'battery_level', 10)
        self.timer = self.create_timer(1.0, self.publish_battery)
        self.level = 100.0


    def publish_battery(self):
        self.level = max(0.0, self.level - random.uniform(0.05, 0.2))

        msg = Float32()
        msg.data = self.level
        self.publisher_.publish(msg)
        self.get_logger().info(f'Battery: {self.level:.1f}%')

def main(args=None):
    rclpy.init(args=args)

    node = BatteryMonitor()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
