#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/SteeringAngle', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print("started")
    while not rospy.is_shutdown():
        for i in range(80) :
            steering = 20
            rospy.loginfo(steering)
            pub.publish(steering)
            rate.sleep()
        for i in range(80) :
            steering = -20
            rospy.loginfo(steering)
            pub.publish(steering)
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
