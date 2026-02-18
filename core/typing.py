# AI derived
from core.debug import debug
import sys
import time

if debug:
    delay = float(input('[TYPE SPEED (0.01-0.05)] '))
else:
    delay = 0.03

def type_effect(text, delay=delay) -> str:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # Forces the character to appear immediately
        time.sleep(delay)  # Waits for a short duration
    
    return ''

def type_input(text, delay=delay) -> str:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    value = input()
    return value.strip()
