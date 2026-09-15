#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from battery_interface.srv import SetLed

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery_node")
        self.client_ = self.create_client(SetLed, "set_led")

    def call_set_led(self, led_number, led_state):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Add Two Ints server...")

        request = SetLed.Request()
        request.led_number = led_number
        request.led_state = led_state

        future = self.client_.call_async(request)
        future.add_done_callback(self.callback_call_set_led)

    def callback_call_set_led(self, future):
        response = future.result()
        self.get_logger().info("Got response: " + str(response.success))


def main(args=None):
    led_num = 1
    led_state = 0
    rclpy.init(args=args)
    node = BatteryNode()
    node.call_set_led(led_num, led_state)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()