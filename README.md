# 🎬 YouTube Video/Audio Downloader (Flask + yt-dlp)

A simple browser-based YouTube downloader built with **Python Flask** and powered by **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**.  
Download any public YouTube video in **MP4** (video) or **MP3** (audio) format right from your browser.

---

## 🚀 Features

- ✅ Download YouTube videos in MP4 format (best resolution)  
- ✅ Extract and download audio as high-quality MP3  
- ✅ Minimal web UI — easy to use in any browser  
- ✅ Backend powered by Flask  
- ✅ Uses `yt-dlp` (faster & more stable than `pytube`)  
- ✅ No ads, no bloat — just clean downloading  

---

## 📁 Project Structure

```plaintext
youtube_downloader/
│
├── app.py                  # Flask server with download logic  
├── requirements.txt        # Python dependencies  
├── downloads/              # Stores downloaded video/audio  
├── templates/  
│   └── index.html          # Frontend UI (HTML)  
├── static/  
│   └── style.css           # CSS styling  
├── .gitignore              # Git ignore file  
└── README.md               # Project info  
```

## ⚙️ Installation

### 1. Clone this repository
```
git clone https://github.com/yourusername/youtube_downloader.git
cd youtube_downloader
```
### 2. Set up a virtual environment
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### If yt-dlp is missing, install it manually:
```
pip install yt-dlp
```

## 🧪 Usage
### 1. Run the server
```
python app.py
```
You should see:
```
Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

### 2. Open in your browser
Visit http://localhost:5000

Paste a YouTube link
Select format: MP4 (video) or MP3 (audio)
Click Download Video

Your download should begin automatically after processing.

## 📦 Requirements
Python 3.8 or higher
Flask
yt-dlp

### requirements.txt
```
Flask
yt-dlp
```
