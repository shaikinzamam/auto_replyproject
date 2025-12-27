# 🤖 Auto Reply Bot using PyAutoGUI + Gemini API

This project is a desktop automation bot that **copies text automatically from screen, sends it to Gemini API for generating a response, and pastes the reply back automatically.**  
Useful for replying to chats/messages automatically.

---

## 📌 Features

- Auto-detect & copy text on screen
- Sends text to Gemini API using google.generativeai
- Generates meaningful reply automatically
- Pastes response back in the input box
- Works with any chat window
- Clipboard based automation

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `autoreply.py` | Main script handling copy → AI reply → paste automation |
| `main.py` | Script to track mouse coordinates for automation setup |
| `program.py` | Alternative automation script copy & paste only |

---

## 🔧 Requirements

Install dependencies:

```bash
pip install google-generativeai pyautogui pyperclip python-dotenv
