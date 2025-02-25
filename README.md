# Downloader

Brief Explanation

This tool is a Python-based video downloader that can download videos and audio from YouTube, Facebook, and TikTok.

Key features:
✅ Download videos in various qualities (low, medium, high).
✅ Download only audio (MP3) from video.
✅ Displays progress bar while downloading.
✅ Can resume interrupted downloads (resume download).
✅ Select the storage folder as desired.

📥 Installation on Multiple Platforms
1️⃣ Installation in Termux (Android)

Run the following command in Termux:
```
pkg update && pkg upgrade
pkg install python ffmpeg
pip install yt-dlp colorama tqdm
git clone https://github.com/Z-BL4CX-H4T/Downloader.git
cd Downloader
python2 Downloader.py
```
📌 FFmpeg must be installed to convert audio to MP3.

2️⃣ Installation on Linux (Debian/Ubuntu)
Run the following command in the terminal:
```
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip ffmpeg
pip3 install yt-dlp colorama tqdm
git clone https://github.com/Z-BL4CX-H4T/Downloader.git
cd Downloader
python2 Downloader.py
```
📌 Required to support video/audio downloading and progress bar display.

3️⃣ Installation on Windows
1. Download and install Python from python.org .

2. Open Command Prompt (CMD) and run the command:
```pip install yt-dlp colorama tqdm```

4. Install FFmpeg:
Download FFmpeg from ffmpeg.org .
Add ffmpeg.exe to System Environment Variables.

📌 FFmpeg is required to download and convert audio to MP3 format.

💡 Conclusion
This tool is a simple solution to download videos/audios from various platforms without having to open a browser. Just run it in the terminal, enter the URL, and the download will be processed automatically.
