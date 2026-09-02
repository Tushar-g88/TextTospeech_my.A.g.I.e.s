# My A.G.I.E.S. — Text-to-Speech 🎙️

> A Python-based Text-to-Speech module developed for **My A.G.I.E.S.**, focused on natural voice generation, audio playback, and reducing TTS response latency.

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Edge TTS](https://img.shields.io/badge/Edge--TTS-Neural%20Voice-0078D4?logo=microsoftedge\&logoColor=white)](https://github.com/rany2/edge-tts)
[![Pygame](https://img.shields.io/badge/Pygame-Audio-00A86B)](https://www.pygame.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?logo=selenium\&logoColor=white)](https://www.selenium.dev/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)](#roadmap)
[![license](https://github.com/Tushar-g88/TextTospeech_my.A.g.I.e.s/blob/main/)](#LICENSE)

---

## 📌 Overview

**My A.G.I.E.S. Text-to-Speech** is a collection of Python-based TTS implementations created as the voice-output component of the **My A.G.I.E.S. AI Assistant**.

The project experiments with different approaches to speech generation and playback, with a particular focus on **speed, reliability, and natural-sounding voices**.

### Main Pipeline

```text
Text Response
     ↓
  TTS Engine
     ↓
 Audio Generation
     ↓
   MP3 File
     ↓
 Pygame Player
     ↓
 🔊 Voice Output
```

---

## ✨ Features

* 🎙️ Natural Text-to-Speech
* ⚡ TTS latency optimization experiments
* 🔊 MP3 audio generation and playback
* 🗣️ Neural voice support with Edge TTS
* 🖥️ Local audio playback with Pygame
* 🌐 Browser-based TTS experiments
* 🐍 Multiple Python implementations
* 🤖 Designed for AI assistant integration

---

## 🛠️ Tech Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Core development            |
| Edge TTS   | Neural voice generation     |
| Pygame     | Audio playback              |
| pyttsx3    | Offline TTS experiments     |
| Selenium   | Browser automation          |
| HTML       | Browser-based TTS interface |

---

## 📂 Project Structure

```text
TextToSpeech/
│
├── TTS.py
├── TTs_Df.py
├── TextTospeech_B.py
├── fast_df_tts.py
├── ttsp.py
│
└── bry.html
```

### Files

| File                | Description                 |
| ------------------- | --------------------------- |
| `TTS.py`            | Basic TTS implementation    |
| `TTs_Df.py`         | Edge TTS and audio playback |
| `TextTospeech_B.py` | Browser-based TTS           |
| `fast_df_tts.py`    | TTS performance experiments |
| `ttsp.py`           | Main TTS implementation     |
| `bry.html`          | Browser TTS interface       |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Tushar-g88/TextTospeech_my.A.g.I.e.s.git
```

### 2. Open the project

```bash
cd TextTospeech_my.A.g.I.e.s
cd TextToSpeech
```

### 3. Install dependencies

```bash
pip install edge-tts pygame pyttsx3 selenium webdriver-manager
```

---

## ▶️ Usage

Run the main TTS program:

```bash
python ttsp.py
```

Other implementations can be tested with:

```bash
python TTS.py
python TTs_Df.py
python fast_df_tts.py
python TextTospeech_B.py
```

---

## 🎙️ Voice Configuration

For Edge TTS, the voice can be changed in the Python code:

```python
VOICE = "en-CA-ClaraNeural"
```

Replace the voice name with another supported Edge TTS voice.

---

## ⚡ Performance

A major goal of this project is to reduce the delay between receiving a text response and producing speech.

```text
AI Response
     ↓
Speech Generation
     ↓
Audio Processing
     ↓
Audio Playback
     ↓
     🔊
```

Current optimization work focuses on:

* Reducing speech-generation time
* Improving audio loading
* Efficient file handling
* Asynchronous processing
* Reducing unnecessary delays

---

## 📸 Screenshots

Add your project screenshots here.

```markdown
![My A.G.I.E.S. TTS](assets/screenshot.png)
```

---

## 🎬 Demo

Add your demo GIF or video here.

```markdown
![My A.G.I.E.S. Demo](assets/demo.gif)
```

---

## 🤖 My A.G.I.E.S. Integration

The Text-to-Speech system is designed to act as the **voice-output layer** of My A.G.I.E.S.

```text
             👤 User
                ↓
        🎤 Speech Recognition
                ↓
           🧠 AI Assistant
                ↓
          💬 AI Response
                ↓
         🎙️ Text-to-Speech
                ↓
            🔊 Voice
```

---

## 🗺️ Roadmap

### Completed

* [x] Basic TTS implementation
* [x] Edge TTS integration
* [x] MP3 generation
* [x] Pygame audio playback
* [x] Browser TTS experiments
* [x] Initial latency optimization

### In Progress

* [ ] Improve TTS response speed
* [ ] Improve audio management
* [ ] Better asynchronous processing
* [ ] Cleaner project architecture

### Planned

* [ ] Real-time streaming TTS
* [ ] Multiple voice selection
* [ ] Multi-language support
* [ ] Voice interruption
* [ ] Complete My A.G.I.E.S. integration
* [ ] TTS performance benchmarking

---

## ⚠️ Notes

* Edge TTS requires an internet connection.
* TTS speed can depend on network conditions.
* Selenium experiments require a compatible browser.
* Some files in this folder are experimental implementations.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## 👨‍💻 Author

**Tushar**

[![GitHub](https://img.shields.io/badge/GitHub-Tushar--g88-181717?logo=github\&logoColor=white)](https://github.com/Tushar-g88)

---

## ⭐ Support

If you find this project useful, consider giving it a **star ⭐** on GitHub.

---

<div align="center">

### My A.G.I.E.S. 🤖

**Giving AI a voice.**

</div>
