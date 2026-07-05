#!usr/bin/env python3

"""
Test suit for the ROS 2 minimal publisher node.

This scripts contains unit tests for verifying the funcionality of a minimal ROS 2 publisher.
It tests the node creation, message counter increment, and message content formatting.

------------
Suscription topics:
    None

------------
Publishing Topics:
    /py_example_topic (std_msgs/String): Example messages with incrementing counter

Author: Cristopher Mancilla
Date: July 05, 2026

"""

import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher
 


def test_publisher_creation():
    """

    """

    # Initialize ROS 2 communication
    rclpy.init()
