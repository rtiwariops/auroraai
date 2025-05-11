# AuroraAI

![AuroraAI Logo](assets/logo-512.png)

**Voice-driven AI assistant capturing audio from any app (Teams, Zoom, browsers) and streaming live, textual answers—perfect for interviews, meetings, and knowledge work.**

---

## 🚀 Quickstart

1. **Clone** the repo  
   ```bash
   git clone https://github.com/YourUsername/auroraai.git
   cd auroraai

2. Create & activate a Python virtual environment
    python3 -m venv .venv
    source .venv/bin/activate      # macOS/Linux
    # .venv\Scripts\activate       # Windows PowerShell

3. Install Python dependencies
    pip install --upgrade pip
    pip install .

4. Install Electron (if not already)
    npm install -g electron

5. Configure environment variables
    cp .env.example .env

6. Edit .env and provide:
    GENAI_API_KEY=sk-...
    GENAI_MODEL=gemini-1.5-flash

7. Run AuroraAI
    auroraai

🎧 How It Works
Start Recording
Click Start to begin capturing audio from your configured input device (e.g. BlackHole).

Stop & Transcribe
Click Stop to end recording; Whisper automatically transcribes your entire audio clip and displays it under Transcript.

Ask AI
Click Ask AI to send the transcript to Gemini. As Gemini responds, each token is streamed live into the Answer panel.

Copy & Share
All output is plain text—copy it, paste it, or feed it into your own RAG/finetune pipelines.

⚙️ Features
Universal Audio Capture via BlackHole (macOS) or any OS audio loopback

Manual Control: ideal for long-form questions (system design, interview scenarios)

One-Shot Transcription: no fragmented sentences—full-clip transcription on Stop

Live AI Streaming: real-time token-by-token answer display

Configurable Model: pick your Gemini variant via .env

Electron Desktop UI: cross-platform, zero-install Chrome-like window

📦 Installation Options
git clone https://github.com/YourUsername/auroraai.git
cd auroraai
pip install -e .

From PyPI
pip install auroraai
auroraai

🛠 Configuration
All settings are in .env:
| Variable        | Description                                | Example            |
| --------------- | ------------------------------------------ | ------------------ |
| `GENAI_API_KEY` | Your Google Generative AI (Gemini) API key | `sk-…`             |
| `GENAI_MODEL`   | Which Gemini model to use                  | `gemini-1.5-flash` |


See .env.example for reference.