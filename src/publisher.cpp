#include "my_pkg/publisher.hpp"

PublisherNode::PublisherNode() : Node("publisher_node")
{
    publisher_ = create_publisher<std_msgs::msg::Int32>("int_topic", 10);
    timer_ = create_wall_timer(500ms, std::bind(&PublisherNode::timer_callback, this));

}

void PublisherNode::timer_callback()
{
    message_.data+=1;
    publisher_->publish(message_);
}


