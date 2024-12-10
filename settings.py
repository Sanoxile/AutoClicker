import pyautogui
import keyTimingInfo

class Settings:

    def __init__(self): # Initialize screen variables
        self.screen_width, self.screen_height = pyautogui.size()
        self.center_width = self.screen_width // 2
        self.center_height = self.screen_height // 2
        self.toggle_key = "right alt"
        self.key_info = []

    def add_key_info(self, key, button, hold, cursor_y, cursor_x, time_in_milis):   # Add a key that isn't already added
        valid = True
        for info in self.key_info:
            if info.button == button:
                valid = False
                break
        if valid:
            info = keyTimingInfo.KeyTimingInfo(key, button, hold, cursor_y, cursor_x, time_in_milis)
            self.key_info.append(info)
    
    def change_toggle_key(self, button):    # Changes toggle key for clicker
        valid = True
        for info in self.key_info:
            if info.button == button:
                valid = False
                break
        if valid:
            self.toggle_key = button