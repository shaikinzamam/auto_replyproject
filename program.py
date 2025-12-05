import pyautogui
import time
import pyperclip
def automate_copy_paste():
  # Clear clipboard first
  pyperclip.copy('')
  
  # Focus the window
  pyautogui.click(1071, 1041) 
  time.sleep(2) 
  
  # Click at start position to focus
  pyautogui.click(718, 200)
  time.sleep(1)
  
  # Drag to select text (slower)
  pyautogui.moveTo(718, 200)
  time.sleep(0.5)
  pyautogui.dragTo(1868, 921, duration=2, button='left')
  time.sleep(1)
  
  # Copy the selected text
  pyautogui.hotkey('ctrl', 'c')
  time.sleep(1)
  
  # Get copied text
  text = pyperclip.paste()
  print("Copied text:", repr(text))
  
  # If text was copied, paste it
  if text and text.strip():
      pyautogui.click(1071, 1041)
      time.sleep(1)
      pyautogui.hotkey('ctrl', 'v')
      time.sleep(1)
      print("Text pasted successfully!")
  else:
      print("No text was copied. Try adjusting coordinates.")

automate_copy_paste()