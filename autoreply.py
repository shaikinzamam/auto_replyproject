import pyautogui
import time
import pyperclip
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv("key.env")
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in key.env")
    exit()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are a person named shaikinzamam who speaks Hindi as well as English. She is from India and is a CA final student. You analyze the text and reply accordingly."
)

print("Starting auto-reply bot...")
print("Copying text in 3 seconds...\n")

# Clear clipboard
pyperclip.copy('')
time.sleep(2)

# Focus the window
pyautogui.click(1071, 1041) 
time.sleep(2)

# Click at start position
pyautogui.click(718, 200)
time.sleep(1)

# Drag to select text
pyautogui.dragTo(1868, 921, duration=2, button='left')
time.sleep(1)

# Copy the selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Get copied text
text = pyperclip.paste()
print("Copied text:", text)
print("\n" + "="*50)

if text and text.strip():
    # Generate reply using Gemini
    print("Generating reply...\n")
    try:
        response = model.generate_content(f"Reply to the message in a conversational way: {text}")
        reply = response.text
        
        print("--- Gemini Response ---")
        print(reply)
        print("="*50 + "\n")
        
        # Copy reply to clipboard
        pyperclip.copy(reply)
        
        # Paste the reply (click in reply box first)
        pyautogui.click( 796, 968)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        
        print("✓ Reply pasted successfully!")
        
    except Exception as e:
        print(f"Error generating reply: {e}")
else:
    print("❌ No text was copied. Check coordinates.")