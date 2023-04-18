import RPi.GPIO as GPIO 
from time import sleep
import sys

#pins = [6,5,1,7]
train_pins = [2,3,14,15]#train line 
tens_pins = [17,27,22,23]#tens digit number line
ones_pins = [24,0,5,6] #ones digit number line
dir_pins = [16,20,21,26] #direction line
delay = 0.0009
full_rotation = 4100
current_train_line = "A"
current_number = 0
curr_dir = 0

# sets all pins to output
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)



def pin_init(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

pin_init(train_pins)
print("Setup pins #1 Train Pins")
pin_init(tens_pins)
print("Setup pins #2 Tens Pins")
pin_init(ones_pins)
print("Setup pins #3 Ones Pins")
pin_init(dir_pins)
print("Setup pins #4 Dir Pins")

arr1 = [1,1,0,0]
arr2 = [0,1,0,0]

train_dict = {"A":1,
              "C":2,
              "E":3,
              "B":4,
              "D":5,
              "F":6,
              "M":7,
              "G":8,
              "L":9,
              "J":10,
              "Z":11,
              "N":12,
              "Q":13,
              "R":14,
              "W":15,
              "1":16,
              "2":17,
              "3":18,
              "4":19,
              "5":20,
              "6":21,
              "7":22,
              "T":23,
              "S":24,
              "CAR":25
              }

# Private methods (NOT CALLED FROM MAIN.PY)
def train_line_diff(curr_line, new_line):
    res = train_dict[new_line]-train_dict[curr_line]
    if(res >= 0 ):
        return res
    return 36 - train_dict[curr_line] + train_dict[new_line]

#controllors for basic movement
def step(num_of_steps, len_step, motor):
    print("starting to move...")
    for i in range(num_of_steps * len_step):
            move(motor)
    print("finished moving!")
              
def move(motor):
    global arr1
    global arr2
    arrOUT = arr1[1:]+arr1[:1]
    arr1 = arr2
    arr2 = arrOUT
    GPIO.output(motor, arrOUT)
    sleep(delay)
    
def move_to_line(new_line):
    global current_train_line
    num_step = train_line_diff(current_train_line, new_line)
    print("steps: " + str(num_step))
    current_train_line = new_line;
    step(num_step, full_rotation//36+1, train_pins)
    GPIO.output(train_pins, (0,0,0,0))


def move_to_direction(direction): # yet to be implemented
    # note direction is already an int
    # 0 downtown, 1 uptown, 2 blank
    global curr_dir
    num_step = direction - curr_dir
    if(num_step < 0):
        num_step += 3
    print("steps:",num_step)
    step(num_step, full_rotation//3, dir_pins)
    curr_dir = direction
    GPIO.output(dir_pins, (0,0,0,0))
    

def move_numbers(new_number):
    move_tens(new_number//10)
    move_ones(new_number%10)
    global current_number
    current_number = new_number
    

def move_tens(new_digit):
    global current_number
    current_digit = current_number//10
    steps = new_digit - current_digit
    if(steps < 0):
        steps  = 10 + steps
    print("steps:",steps)
    step(steps, full_rotation//10, tens_pins)
    GPIO.output(tens_pins, (0,0,0,0))
    

def move_ones(new_digit):
    global current_number
    current_digit = current_number%10
    steps = new_digit - current_digit
    if(steps < 0):
        steps  = 10 + steps
    print("steps:",steps)
    step(steps, full_rotation//10, ones_pins)
    GPIO.output(ones_pins, (0,0,0,0))
 
 # functions to be called by main.py

def update_train(new_line, direction, minutes):
    move_to_line(new_line)
    move_to_direction(direction)
    move_numbers(minutes)

def update_car(minutes):
    move_to_line("CAR")
    move_to_direction(2)
    move_numbers(minutes)  
    
    
#resets all displays
def reset_all():
    move_to_line("A")
    move_to_direction(0) #default is downtown
    move_numbers(0)

def clean_pins():
    GPIO.output(train_pins, (0,0,0,0))
    GPIO.output(tens_pins, (0,0,0,0))
    GPIO.output(ones_pins, (0,0,0,0))
    GPIO.output(dir_pins, (0,0,0,0))

#
# Debug Main
#

def test_main():
    print("If you see this message, the test_main is running")
    #we get a string of a single char
    print("moving line")
    move_to_line("L")
    sleep(2)
    print("\n====\nmoving number")
    move_numbers(55)
    sleep(2)
    print("\n====\nmoving dir")
    move_to_direction(2)


    print("\nwaiting...\n")
    sleep(2)

    #move_to_number(9)

    print("cleaning...")
    #reset_all() 
    clean_pins()
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)


    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(6, 0)
    GPIO.output(2, 0)
    GPIO.output(3, 0)
    print("program finished")
    sys.exit()

#if imported correctly should see this print
print("Motor Controller Imported")
