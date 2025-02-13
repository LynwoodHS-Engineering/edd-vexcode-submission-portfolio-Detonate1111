#Couldn't upload the video so here is the google drive link
#https://drive.google.com/file/d/19tgFkcfPli9DDPwkc_IieoRBWV3Vw7yN/view?usp=sharing

from vex import *
import time

brain=Brain()

motorRight = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
motorLeft = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
spiral = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
clawMotor = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)

spiral.set_velocity(100)
spiral.spin(REVERSE)
time.sleep(6)
spiral.stop()

time.sleep(1)

motorLeft.set_velocity(50)
motorLeft.spin(FORWARD)
motorRight.set_velocity(50)
motorRight.spin(FORWARD)

time.sleep(1.85)

motorRight.stop()
motorLeft.stop()

clawMotor.set_velocity(100)
clawMotor.spin(REVERSE)
time.sleep(2)


time.sleep(1)

spiral.spin(FORWARD)
time.sleep(10)
spiral.stop()


clawMotor.stop()
clawMotor.spin(FORWARD)
time.sleep(2)

spiral.spin(REVERSE)
time.sleep(8)
spiral.stop()

motorLeft.spin(FORWARD)
motorRight.spin(FORWARD)

time.sleep(1.85)

motorRight.stop()
motorLeft.stop()

clawMotor.stop()
clawMotor.spin(REVERSE)
time.sleep(1.5)
clawMotor.stop()
