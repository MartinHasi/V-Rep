import sim
from time import sleep as delay
# import numpy as np
import cv2
import sys

print("Program Started")


sim.simxFinish(-1)

clientID = sim.simxStart('127.0.1', 19999, True, True, 5000, 5)

if clientID != -1:
    print('Connected Successfully')
else:
    sys.exit('Failed to connect.')

delay(1)

error_code, left_motor_handle = sim.simxGetObjectHandle(
    clientID=clientID, objectName='/PioneerP3DX/leftMotor', operationMode=sim.simx_opmode_oneshot_wait
)
error_code, right_motor_handle = sim.simxGetObjectHandle(
    clientID=clientID, objectName='/PioneerP3DX/rightMotor', operationMode=sim.simx_opmode_oneshot_wait
)

error_code = sim.simxSetJointTargetVelocity(
    clientID=clientID, jointHandle=left_motor_handle, targetVelocity=0.2,
    operationMode=sim.simx_opmode_oneshot_wait)
error_code = sim.simxSetJointTargetVelocity(
    clientID=clientID, jointHandle=right_motor_handle, targetVelocity=0.4,
    operationMode=sim.simx_opmode_oneshot_wait)
