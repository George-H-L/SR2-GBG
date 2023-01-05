import time
import math
from sr.robot3 import *
import cv2
import numpy as np
R = Robot()
#SR0KFF is the wheels board
#SR0WH1J is the claw board
motorL_1 = R.motor_boards["SR0TBG"].motors[0]
motorL_2 = R.motor_boards["SR0TBG"].motors[1]
#motorLeft is left wheel, motorRight is right wheel 
motorR_1 = R.motor_boards["SR0G1JB"].motors[1]
motorR_2 = R.motor_boards["SR0G1JB"].motors[0]
#motorClaw is claw, motorVert is vertical movement of claw
def drv(p, t):
  motorL_1.power = p
  motorR_1.power = p
  motorL_2.power = p
  motorR_2.power = p
  time.sleep(t)
  
drv(0.25,3)  