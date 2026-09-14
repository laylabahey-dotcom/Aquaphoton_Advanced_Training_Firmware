#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using namespace std::chrono_literals;

class NumberPublisher : public rclcpp::Node {
    public:
        NumberPublisher() : Node("number_publisher"), number_(2)
        {
            publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
            timer_ = this->create_wall_timer(1s, std::bind(&NumberPublisher::timer_callback, this));
        }
    private:
        void timer_callback(){
            auto msg = example_interfaces::msg::Int64();
            msg.data = 2;
            RCLCPP_INFO(this->get_logger(), "Publishing %ld", msg.data);
            publisher_->publish(msg);
        }
    int64_t number_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
};


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<NumberPublisher>());
  rclcpp::shutdown();
  return 0;
}