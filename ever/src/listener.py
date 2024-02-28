#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry


flag = 0
y=0
s=0
def callback(data):
    global flag
    global y
    global s
    if flag == 0:
        s = data.pose.pose.position.y
        flag = 1
    else:
        y = data.pose.pose.position.y
    rospy.loginfo(y)
    if y-s >= 75 :
        rospy.loginfo("reached the goal")
        pub_2 = rospy.Publisher('/brakes', Float64, queue_size=10)
        rospy.loginfo("braaaaaake")
        pub_2.publish(1)
        pub = rospy.Publisher('/cmd_vel', Float64, queue_size=10)
        pub.publish(0)

        rospy.is_shutdown()


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/odom", Odometry, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    
    


