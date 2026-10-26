'''
2. Motor-command limiting: Given signed left/right motor commands and a maximum permitted
magnitude, clamp both values while preserving sign.
'''

left_motor_input = -100 #Say .. im assuming input but we can take inputs also and make it
right_motor_input = 100

clamping_permitted = 105

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
def clamp_func(clamp, left_input, right_input):
    return ((sign(left_input)*min(abs(clamp), abs(left_input))), (sign(right_input)*min(abs(clamp), abs(right_input))))

#the above func basically returns a tuple with what the value that must be given to the motors

print(clamp_func(clamp = clamping_permitted, left_input = left_motor_input, right_input = right_motor_input))

'''
This will work we can make tiny changes to accomdate anything else also ig!!


We can take .. input for the motorsand clamp it basically .. to any value we choose
'''



