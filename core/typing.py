import sys
import time

def type_effect(text, delay=0.05) -> str:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # Forces the character to appear immediately
        time.sleep(delay)  # Waits for a short duration
    
    return ''

def type_input(text, delay=0.05) -> str:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    value = input()
    return value.strip()