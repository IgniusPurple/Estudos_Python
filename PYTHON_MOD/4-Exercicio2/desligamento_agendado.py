import os

def turn_off_on_hour():
    os.system('shutdown +60')
    

def turn_off_half_an_hour():
    os.system('shutdown +30')

def cancel_shutdown():
    os.system('shutdown -c')
    
    