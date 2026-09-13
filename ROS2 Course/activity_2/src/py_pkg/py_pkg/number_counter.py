#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.msg import String

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.subscriber_ = self.create_subscription(Int64, "number", self.subscriber_callback, 10)

        self.count = 0
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

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

