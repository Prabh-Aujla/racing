# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: `````` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: "source /opt/ros/foxy/setup.bash" sets up your environment to use the core, globally installed ROS 2 packages and tools. 
"source install/local_setup.bash"sets up the environment for the local workspace where you add the packages that you build.


### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: ''queue_size''argument controls the number of messages that stored in memory in the subscriber's or publisher's message queue before they are processed or delivered.

A small ''queue_size''will limit the number of messages a publisher can buffer. And the subscriber will drop messages if it can't keep up with the incoming rate.

A larger ''queue_size'' allows more messages to be published and not be lost. this allows the subsriber to handle incoming messages and ensures fewer messages are dropped. this can delay the messgage processing. 

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: No, you don't have to run ''colcon build'' after changing the launch file because the file is  being executed directly from the source directory and the changes take effect immidiately. 

Yes, you need to run ''colcon build'' after changing the launch file. Since ROS 2 iwill look for the launch file in the install directory. all the changes you make won't be reflected until you rebuild the package.
