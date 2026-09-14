#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.subscriber_ = self.create_subscription(Int64, "number", self.subscriber_callback, 10)

        self.count = 0
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.timer = self.create_timer(1.0, self.timer_callback)


        self.server_ = self.create_service(SetBool, "reset_counter", self.callback_SetBool)

    def callback_SetBool(self, request: SetBool.Request, response: SetBool.Response):
        if request.data:
            self.count = 0
            response.success = True
            response.message = "Counter has been reset"
        else:
            response.success = False
            response.message = "Counter has not been reset"
        return response
            

    def subscriber_callback(self, msg):
        self.count += msg.data

    def timer_callback(self):
        msg = Int64()
        msg.data = self.count
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

