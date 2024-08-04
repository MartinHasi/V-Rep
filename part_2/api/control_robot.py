import sim
import time
import sys

print("Progrram Started")


while True:
    motor_left_speed = 1
    motor_right_speed = 2

    sim.simxFinish(-1)
    clientID = sim.simxStart("127.0.0.1", 19999, True, True, 5000, 5)
    # if clientID != -1:
    #     print("Connected Successfully")

    # else:
    #     sys.exit("Failed to connect.")

    # time.sleep(1)

    error_code, left_motor_handle = sim.simxGetObjectHandle(
        clientID=clientID, objectName="/PioneerP3DX/leftMotor", operationMode=sim.simx_opmode_oneshot_wait)
    error_code, right_motor_handle = sim.simxGetObjectHandle(
        clientID=clientID, objectName="/PioneerP3DX/rightMotor", operationMode=sim.simx_opmode_oneshot_wait)

    motor_left = sim.simxSetJointTargetVelocity(
        clientID=clientID, jointHandle=left_motor_handle, targetVelocity=motor_left_speed, operationMode=sim.simx_opmode_oneshot_wait)
    motor_right = sim.simxSetJointTargetVelocity(
        clientID=clientID, jointHandle=right_motor_handle, targetVelocity=motor_right_speed, operationMode=sim.simx_opmode_oneshot_wait)

    time.sleep(5)
    motor_left_speed = 2
    motor_right_speed = 1

    sim.simxFinish(-1)
    clientID = sim.simxStart("127.0.0.1", 19999, True, True, 5000, 5)
    # if clientID != -1:
    #     print("Connected Successfully")

    # else:
    #     sys.exit("Failed to connect.")

    # time.sleep(1)

    error_code, left_motor_handle = sim.simxGetObjectHandle(
        clientID=clientID, objectName="/PioneerP3DX/leftMotor", operationMode=sim.simx_opmode_oneshot_wait)
    error_code, right_motor_handle = sim.simxGetObjectHandle(
        clientID=clientID, objectName="/PioneerP3DX/rightMotor", operationMode=sim.simx_opmode_oneshot_wait)

    motor_left = sim.simxSetJointTargetVelocity(
        clientID=clientID, jointHandle=left_motor_handle, targetVelocity=motor_left_speed, operationMode=sim.simx_opmode_oneshot_wait)
    motor_right = sim.simxSetJointTargetVelocity(
        clientID=clientID, jointHandle=right_motor_handle, targetVelocity=motor_right_speed, operationMode=sim.simx_opmode_oneshot_wait)
    time.sleep(5)
