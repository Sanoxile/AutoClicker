import pyautogui
import keyboard
import time

# Define the target position offsets
OFFSET_X = 900
OFFSET_Y = 20

# Set initial active state to False
active = False

# Define the function to perform actions (holding click and "a")
def hold_click_and_a():
    screen_width, screen_height = pyautogui.size()
    
    # Move cursor a bit left and down from the center
    target_x = screen_width // 2 + OFFSET_X
    target_y = screen_height // 2 + OFFSET_Y
    
    # Move to the target position
    pyautogui.moveTo(target_x, target_y)
    
    # Hold down the left mouse button and the "a" key
    pyautogui.mouseDown(button='left')
    pyautogui.keyDown('d')

# Define the function to release actions
def release_click_and_a():
    # Release the left mouse button and the "a" key
    pyautogui.mouseUp(button='left')
    pyautogui.keyUp('d')

# Main loop to check for toggle and perform actions
try:
    while True:
        # Toggle active state when "right alt" is pressed
        if keyboard.is_pressed("right alt"):
            active = not active
            print("Active" if active else "Inactive")
            
            # Hold or release actions based on the active state
            if active:
                hold_click_and_a()
            else:
                release_click_and_a()
            
            # Add delay to prevent rapid toggling
            time.sleep(0.3)
        
        # Add a small delay in the loop
        time.sleep(0.1)
except KeyboardInterrupt:
    # Ensure actions are released if the script is interrupted
    release_click_and_a()
    print("Script stopped.")
