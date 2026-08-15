import rclpy
from rclpy.node import Node
from archo_interfaces.srv import ResetEncoder
from archo_interfaces.srv import EmergencyStop

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.get_logger().info('Starting motors...')
        self.get_logger().info('Motors ON')
        self.encoder_ticks = 15420
        self.srv = self.create_service(
            ResetEncoder, 'reset_encoder', self.handle_reset)
        self.emergency_stop = self.create_service(
            EmergencyStop, 'emergency_stop', self.handle_emergency_stop)

    def handle_reset(self, request, response):
        self.get_logger().info(f'Resetting encoder from {self.encoder_ticks} ticks')
        self.encoder_ticks = 0
        response.success = True
        response.message = 'Encoder reset to zero'
        return response

    def handle_emergency_stop(self, request, response):
        response.success = True
        if response.success == True:
            self.get_logger().info('Emergency stop request: success!')
        else:
            self.get_logger().info('Emergency stop request: failed!')
        return response


def main(args=None):
    rclpy.init(args=args)

    node = MotorController()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()