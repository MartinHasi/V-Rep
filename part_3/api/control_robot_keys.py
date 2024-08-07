import sim
from time import sleep as delay
import numpy as np
import cv2
import sys

print("Program Started")
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.1', 19999, True, True, 5000, 5)

left_speed = 0
right_speed = 0

if clientID != -1:
    print('Connected to remote API Server.')
else:
    sys.exit('Failed connecting to remote API Server.')

delay(1)

error_code, left_motor_handle = sim.simxGetObjectHandle(
    clientID=clientID, objectName='/PioneerP3DX/leftMotor', operationMode=sim.simx_opmode_oneshot_wait
)
error_code, right_motor_handle = sim.simxGetObjectHandle(
    clientID=clientID, objectName='/PioneerP3DX/rightMotor', operationMode=sim.simx_opmode_oneshot_wait
)

error_code, camera_handle = sim.simxGetObjectHandle(
    clientID=clientID, objectName='cam1', operationMode=sim.simx_opmode_oneshot_wait
)
delay(1)

return_code, resolution, image = sim.simxGetVisionSensorImage(
    clientID=clientID, sensorHandle=camera_handle, options=0,
    operationMode=sim.simx_opmode_streaming
)
delay(1)

while True:
    return_code, resolution, image = sim.simxGetVisionSensorImage(
        clientID=clientID, sensorHandle=camera_handle, options=0,
        operationMode=sim.simx_opmode_streaming
    )
    im = np.array(image, dtype=np.int8)
    im.resize([resolution[0], resolution[1],3])

    im = cv2.flip(im, 0)
    #im = cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #im = cv2.resize(im, (512, 512))
    #im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

    error_code = sim.simxSetJointTargetVelocity(
        clientID=clientID, jointHandle=left_motor_handle, targetVelocity=left_speed,
        operationMode=sim.simx_opmode_oneshot_wait)
    error_code = sim.simxSetJointTargetVelocity(
        clientID=clientID, jointHandle=right_motor_handle, targetVelocity=right_speed,
        operationMode=sim.simx_opmode_oneshot_wait)

    cv2.imshow('data', im)
    com = cv2.waitKey(1)
    if com == ord('q'):
        break
    elif com == ord('w'):
        left_speed = 0.2
        right_speed = 0.2
    elif com == ord('a'):
        left_speed = -0.1
        right_speed = 0.2
    elif com == ord('d'):
        left_speed = 0.2
        right_speed = -0.1
    elif com == ord('s'):
        left_speed = -0.2
        right_speed = -0.2
    else:
        left_speed = 0
        right_speed = 0

    com = 'o'

cv2.destroyAllWindows()
