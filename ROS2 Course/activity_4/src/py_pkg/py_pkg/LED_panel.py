#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from battery_interface.srv import SetLed
from battery_interface.msg import PanelState

class LedStatePanel(Node):
    def __init__(self):
        super().__init__("led_panel_state_node")

        self.led_states_ = [0,0,0]

        self.server_ = self.create_service(SetLed, "set_led", self.callback_set_led)
        self.publisher_ = self.create_publisher(PanelState, "led_panel_state", 10)
        self.timer_ = self.create_timer(5.0, self.callback_publish)

    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):
        led_number = request.led_number
        state = request.led_state

        if led_number >= len(self.led_states_) or led_number < 0:
            response.success = False
            return response

        if state not in [0,1]:
            response.success = False
            return response

        self.led_states_[led_number] = state
        response.success = True
        return response


    def callback_publish(self):
        msg = PanelState()
        msg.led_states = self.led_states_
        self.publisher_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = LedStatePanel()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()