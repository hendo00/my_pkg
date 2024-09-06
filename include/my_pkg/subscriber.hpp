#ifndef MY_PKG__SUBSCRIBER_HPP_
#define MY_PKG__SUBSCRIBER_HPP_

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include <chrono>
using namespace std::chrono_literals;

class SubscriberNode : public rclcpp::Node
{
public:
    SubscriberNode();

private:
    void callback(const std_msgs::msg::Int32::SharedPtr msg);

    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscriber_;

};

#endif
