#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-2
"""
* Copyright (C) 2022 Ryuichi Ueda.  All rights reserved.
"""

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
   global n
   n = message.data

if __name__ == '__main__': 
   rospy.init_node('twice')
   sub = rospy.Subscriber('count_up', Int32, cb) 
   pub = rospy.Publisher('twice', Int32, queue_size=1) 
   rate = rospy.Rate(1)
   while not rospy.is_shutdown():
     
    if n % 3 == 1:
        print ("ヽ(∴｀┏Д┓´)ﾉ彡",n) #←世界のナベアツです
        pub.publish(3)
        
    else:
        print ("  ( o     o )",n)
        pub.publish(n)

      
    rate.sleep()
