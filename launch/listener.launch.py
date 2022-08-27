from launch import LaunchDescription
from launch_ros.actions import Node

def generat_launch_desc():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executables='listener'
        )
    ])