import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionServer
from archo_interfaces.srv import ResetEncoder
from archo_interfaces.srv import EmergencyStop
from archo_interfaces.action import MoveToShelf

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
        self.action_server = ActionServer(
            self, MoveToShelf, 'move_to_shelf', self.execute_move)


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

    def execute_move(self, goal_handle):
        target = goal_handle.request.shelf_number
        self.get_logger().info(f'Moving to shelf {target}')
        distance = 18.0
        feedback = MoveToShelf.Feedback()

        while distance > 0:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                result = MoveToShelf.Result()
                result.success = False
                result.final_message = 'Cancelled mid-route'
                return result

            distance -= 3.0
            feedback.distance_remaining = max(distance, 0.0)
            feedback.status = 'moving'
            goal_handle.publish_feedback(feedback)
            time.sleep(0.5)

        goal_handle.succeed()
        result = MoveToShelf.Result()
        result.success = True
        result.final_message = f'Arrived at shelf {target}'
        return result



def main(args=None):
    rclpy.init(args=args)

    node = MotorController()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()