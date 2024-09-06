#include "my_pkg/subscriber.hpp"

SubscriberNode::SubscriberNode() : Node("subscriber_node")
{
subscriber_ = create_subscription<std_msgs::msg::Int32>("int_topic", 10, 
std::bind(&SubscriberNode::callback, this, std::placeholders::_1));

}
void SubscriberNode::callback(const std_msgs::msg::Int32::SharedPtr msg)
{
RCLCPP_INFO(get_logger(), "Hello %d", msg->data);
}
