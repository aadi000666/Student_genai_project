# 🤖  Gemini AI Assistant

Siya is an intelligent desktop AI assistant built with **Google Gemini API** and **Python**. It supports interactive terminal-based chat capabilities and personalized greetings.

---

## 📑 Table of Contents

- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#️-installation--setup)
- [Creating the .env File](#-creating-the-env-file)
- [Usage](#-usage)
- [Environment Variables](#-environment-variables)
- [License](#-license)

---

## 🚀 Features

- 💬 **Interactive AI Chat:** Real-time responses powered by the Gemini API.
- 🕒 **Smart Greetings:** Dynamic greeting system (Morning / Afternoon / Evening).
- 🧠 **Context-Aware Sessions:** Smooth chat interface with session management.
- ⚡ **Environment Support:** Secure API key management using `.env`.

---

## 🛠️ Tech Stack

| Category         | Details                          |
|-------------------|-----------------------------------|
| **Language**      | Python                            |
| **AI Engine**     | Google Gemini API (`google-genai`)|
| **Dependencies**  | `python-dotenv`, `google-genai`   |

---

## 📂 Project Structure

```
├── app.py           # Main application code
├── .env             # Environment variables (API Keys)
├── .gitignore       # Git ignored files (.env, venv)
└── README.md        # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Go to the project directory

```bash
cd "your-project-path"
```

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows:**
```bash
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install google-genai python-dotenv
```

### 4️⃣ Create the `.env` file

See the detailed section below.

### 5️⃣ Run the assistant

```bash
python app.py
```

That's it! Siya is now ready to chat with you. 🎉

---

## 🔑 Creating the .env File

The `.env` file is just a plain text file that stores your secret API key so it's never hardcoded inside `app.py`. Here's how to create it, step by step, on any OS:

### Step 1: Get your Gemini API key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey).
2. Sign in with your Google account.
3. Click **"Create API Key"** and copy the key that's generated — it'll look something like `AIzaSy...`.

### Step 2: Create the file itself

The file must be named exactly `.env` (with the dot at the start, no filename before it, no `.txt` extension) and must sit in the **same folder as `app.py`**.

**Option A — Using a code editor (easiest):**
1. Open your project folder in VS Code (or any editor).
2. Right-click in the file explorer panel → **New File**.
3. Name it `.env` and press Enter.
4. Paste the line below into it and save.

**Option B — Using terminal/command line:**

Windows (Command Prompt):
```bash
type nul > .env
```

Windows (PowerShell):
```bash
New-Item .env
```

macOS / Linux:
```bash
touch .env
```

Then open it with any text editor (`notepad .env` on Windows, or `nano .env` / `code .env` elsewhere) and add the content from Step 3.

### Step 3: Add your key to the file

Open `.env` and add this single line (replace with your real key):

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

**Important formatting rules:**
- No quotes around the key.
- No spaces before or after the `=` sign.
- No semicolons or trailing characters.
- Save the file as plain text (not `.docx` or rich text).

### Step 4: Make sure it's git-ignored

Open (or create) a `.gitignore` file in the same folder and add:

```
.env
venv/
```

This prevents your secret key from ever being pushed to GitHub by accident.

### Step 5: Verify it's working

Run your app:
```bash
python app.py
```

If `python-dotenv` is loading the key correctly (via `load_dotenv()` in `app.py`), the assistant should start without any "API key not found" error. If you do get that error, double-check:
- The file is named `.env` exactly (not `env.txt` or `.env.txt`).
- It's in the same directory you're running `python app.py` from.
- There are no typos in the variable name `GEMINI_API_KEY`.

---

## 💻 Usage

- After running the app, you'll get a personalized greeting based on the time of day (Good Morning / Afternoon / Evening).
- Type your message in the terminal and press Enter — Siya will respond in real time using the Gemini API.
- To exit the chat, type `exit` or `quit` (if implemented in your app), or press `Ctrl + C`.

---

## 🔐 Environment Variables

| Variable          | Description                          | Required |
|--------------------|---------------------------------------|----------|
| `GEMINI_API_KEY`   | Your Google Gemini API key            | ✅ Yes   |

> ⚠️ Never push your `.env` file to GitHub. It's already listed in `.gitignore`, so it stays safe by default.

---

## 📄 License

This project is open-source and available under the **MIT License**.
