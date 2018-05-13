import RPi.GPIO as GPIO

# Constant for number of led lights on the board
NUM_LIGHTS = 5

# set up pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)     # 2^4
GPIO.setup(11, GPIO.OUT)    # 2^3
GPIO.setup(13, GPIO.OUT)    # 2^2
GPIO.setup(15, GPIO.OUT)    # 2^1
GPIO.setup(16, GPIO.OUT)    # 2^0
GPIO.setup(18, GPIO.OUT)    # program is running

GPIO.output(18, True)

# led animation at start up function
#def led_startup_animation():

# add 1 to binary representation
# a represents an array representation of the binary number
def add(a):
    c = 1
    i = 0
    
    while(c > 0 and i < NUM_LIGHTS):
        if (a[i] == 0):
            a[i] = 1
            c = 0
        else:
            a[i] = 0
        i = i + 1
        
    return a

# subtract one from binary representation
# a represents an array representation of the binary number
def subtract(a):
    i = 0
    while(a[i] == 0 and i < NUM_LIGHTS):
        i = i + 1
    if (i < NUM_LIGHTS):
        a[i] = 0
        i = i - 1
        while (i > -1):
            a[i] = 1
            i = i - 1
    return a
            
#if binary number is at a maximum return true
#else return false indicating we can add to it
def isMax(a, i):
    while (i > -1):
        if (a[i] == 0):
            return False
        i = i - 1
    print("Already at maximum")
    return True

#if binary numbe is at a minimum return true
#else return false indicating we can subtract from it
def isMin(a, i):
    while (i > -1):
        if (a[i] == 1):
            return False
        i = i - 1
    print("Already at minimum")
    return True
    
#assign values to leds with array a
def update_led_display(a):
    GPIO.output(7, a[4])
    GPIO.output(11, a[3])
    GPIO.output(13, a[2])
    GPIO.output(15, a[1])
    GPIO.output(16, a[0])
        
binaryNumber = [0, 0, 0, 0, 0]
user_input = 0

#run startup led animation
#led_startup_animation()

while(user_input != -1):

    if (user_input == 1 and isMax(binaryNumber, NUM_LIGHTS - 1) == False):
        binaryNumber = add(binaryNumber)
    elif (user_input == 0 and isMin(binaryNumber, NUM_LIGHTS - 1) == False):
        binaryNumber = subtract(binaryNumber)
        
    update_led_display(binaryNumber)

    user_input = input("1 to increase, 0 to decrease value:")

#shut down GPIO
GPIO.cleanup()

#legacy code from this project
'''
def led_represent_value(ledInteger):
    if (ledInteger < 0):
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(12, False)
        GPIO.output(22, False)
    elif (ledInteger == 0):
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(12, False)
    elif (ledInteger == 1):
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(12, True)
    elif (ledInteger == 2):
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(12, False)
    elif (ledInteger == 3):
        GPIO.output(7, False)
        GPIO.output(11, True)
        GPIO.output(12, True)
    elif (ledInteger == 4):
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(12, False)
    elif (ledInteger == 5):
        GPIO.output(7, True)
        GPIO.output(11, False)
        GPIO.output(12, True)
    elif (ledInteger == 6):
        GPIO.output(7, True)
        GPIO.output(11, True)
        GPIO.output(12, False)
    elif (ledInteger == 7):
        GPIO.output(7, True)
        GPIO.output(11, True)
        GPIO.output(12, True)
    else:
        print("Error: user input = " + ledInteger)
'''
