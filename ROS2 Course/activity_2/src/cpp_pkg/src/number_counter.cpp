#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using std::placeholders::_1;
using namespace std::chrono_literals;

class NumberCounter : public rclcpp :: Node {
    public:
    NumberCounter(): Node("number_counter"), count_(0)
    {
        subscription_ = this->create_subscription<example_interfaces::msg::Int64>(
            "number", 10, std::bind(&NumberCounter::subscription_callback, this, _1)
        );
        publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number_count", 10);

    }
    private:
    void subscription_callback(const example_interfaces::msg::Int64::SharedPtr msg){
        count_ += msg->data;
        RCLCPP_INFO(this->get_logger(), "Number is %ld", msg->data);

        RCLCPP_INFO(this->get_logger(), "Count is %ld", count_);
        example_interfaces::msg::Int64 count_msg;
        count_msg.data = count_;
        publisher_->publish(count_msg);
        }
    

    int64_t count_;    
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscription_;    
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;


};


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<NumberCounter>());
  rclcpp::shutdown();
  return 0;
}