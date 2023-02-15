"""track_ct_py controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard

# create the Robot instance.
robot = Robot()
print('start')
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
left_motor = robot.getDevice('left_motor')
right_motor = robot.getDevice('right_motor')
rot_motor = robot.getDevice('rot_motor')


left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

vel = 0.1
left_motor.setVelocity(vel)
right_motor.setVelocity(vel)

keyboard = Keyboard()
last_key = -1
keyboard.enable(10*timestep )

rot_max = rot_motor.getMaxPosition()
rot_min = rot_motor.getMinPosition()
pos = rot_motor.getTargetPosition()
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    rot_motor.setPosition(pos)
    key = keyboard.getKey()
    if key>0 and key!=last_key:
        last_key=key
        print(key)
    if key==ord('Y'):
        pos = rot_motor.getTargetPosition()+0.01
        if pos>rot_max:pos=rot_max-0.001
    if key==ord('H'):
        pos = rot_motor.getTargetPosition()-0.01
        if pos<rot_min:pos=rot_min+0.001
    if key==ord('W'):
        left_motor.setVelocity(vel)
        right_motor.setVelocity(vel)
        
    if key==ord('X'):
        left_motor.setVelocity(-vel)
        right_motor.setVelocity(-vel)
        
    if key==ord('A'):
        left_motor.setVelocity(-vel)
        right_motor.setVelocity(vel)
        
    if key==ord('D'):
        left_motor.setVelocity(vel)
        right_motor.setVelocity(-vel)
        
    if key==ord('S'):
        left_motor.setVelocity(0.)
        right_motor.setVelocity(0.)
    if key==ord('N'):
        vel -=0.01
        print(vel)
    if key==ord('M'):
        vel +=0.01
        print(vel)
        
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
