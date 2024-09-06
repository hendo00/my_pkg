import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import pygame
import time

DEBOUNCE_TIME = 0.3  # 300 milliseconds debounce time
DEADZONE = 0.1  # Deadzone for joystick axis
# VEL = 5.0  # Base velocity multiplier
RATE_HZ = 10  # Rate in Hz

def get_axis_with_deadzone(axis_value, deadzone):
    """Apply a dead zone to joystick axis values."""
    if abs(axis_value) < deadzone:
        return 0
    return axis_value

class VelocityControlNode(Node):

    def __init__(self):
        super().__init__('vel_ctrl_node')

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

        self.subscriber_ = self.create_subscription(
            String,
            'ack',
            self.ack_callback,
            10
        )
        
        pygame.init()
        pygame.joystick.init()

        self.joystick = None
        self.connect_joystick()

        self.get_logger().info('Velocity Control Node has started.')


    def connect_joystick(self):
        """Attempt to connect to the first available joystick."""
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.get_logger().info(f'Joystick {self.joystick.get_name()} initialized.')
        else:
            self.joystick = None
            self.get_logger().warn('No joystick found. Waiting for connection.')

    
    def ack_callback(self, msg):
        """Callback for the esp32 msg"""
        self.get_logger().info(f'Recieved ACK: {msg.data}')
        
    def run(self):
        last_command_time = 0
        rate = self.create_rate(RATE_HZ)  # Adjustable loop rate

        while rclpy.ok():
            pygame.event.pump()  # Process Pygame events

            if self.joystick:
                current_time = time.time()

                if current_time - last_command_time > DEBOUNCE_TIME:
                    y_axis_value = self.joystick.get_axis(1)
                    x_axis_value = self.joystick.get_axis(2)

                    # Apply deadzone
                    y_axis_value = get_axis_with_deadzone(y_axis_value, DEADZONE)
                    x_axis_value = get_axis_with_deadzone(x_axis_value, DEADZONE)

                    # Debug joystick values
                    self.get_logger().info(f'Joystick axis values: x={x_axis_value}, y={y_axis_value}')

                    twist = Twist()
                    twist.linear.x = -float(y_axis_value)
                    twist.angular.z = float(x_axis_value)

                    # Debug published values
                    self.get_logger().info(f'Published: linear.x={twist.linear.x}, angular.z={twist.angular.z}')

                    self.publisher_.publish(twist)
                    last_command_time = current_time

            else:
                self.send_stop_command()
                self.connect_joystick()

                # self.get_logger().warn("Joystick not connected or not initialized.")

            # Sleep to maintain loop rate
            # rate.sleep()
            time.sleep(1/RATE_HZ)

    def send_stop_command(self):
        """Send a stop command to halt the robot."""
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher_.publish(twist)
        self.get_logger().info('Published stop command.')

def main(args=None):
    rclpy.init(args=args)
    node = VelocityControlNode()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        node.send_stop_command()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
