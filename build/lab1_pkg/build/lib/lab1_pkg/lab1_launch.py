from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab1_pkg',
            executable='talker',
            name='talker',
            parameters=[{'v': LaunchConfiguration('v',default = float(0))}, 
                        {'d': LaunchConfiguration('d',default = float(0))}],
        ),
        Node(
            package='lab1_pkg',
            executable='relay',
            name='relay'
        ),   
    ])

