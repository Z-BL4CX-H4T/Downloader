import yt_dlp
import time
import sys
import os
import re
import shutil
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)

ascii_art = f"""{Fore.RED}
██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}                                                  
{Fore.YELLOW}  ⚡ TOOLS DOWNLOADER VIDEO (Facebook, YouTube, TikTok) ⚡{Style.RESET_ALL}
{Fore.RED}  📌 Dibuat oleh: [Mr.P3T0K]  {Style.RESET_ALL}
"""

def clear_screen():
    columns = shutil.get_terminal_size().columns
    print("\n" * 0)

def is_valid_url(url):
    regex = r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be|www\.facebook\.com|www\.tiktok\.com)\/.+$'
    return re.match(regex, url) is not None

class ProgressBar:
    def __init__(self):
        self.pbar = None

    def hook(self, d):
        if d['status'] == 'downloading':
            total_size = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)

            if total_size:
                if self.pbar is None:
                    self.pbar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Mengunduh", colour="cyan")
                self.pbar.update(downloaded - self.pbar.n)

        elif d['status'] == 'finished':
            if self.pbar:
                self.pbar.close()
            print(f"\n{Fore.GREEN}✅ Download selesai! Video tersimpan sebagai '{d['filename']}'{Style.RESET_ALL}")

def download_video(url, platform):
    if not is_valid_url(url):
        print(f"{Fore.RED}❌ URL tidak valid! Pastikan Anda memasukkan URL yang benar.{Style.RESET_ALL}")
        return
    
    quality = input(f"{Fore.YELLOW}Pilih kualitas video (low/medium/high): {Style.RESET_ALL}")
    format_map = {
        'low': 'worst',
        'medium': 'best',
        'high': 'bestvideo+bestaudio/best'
    }

    output_folder = input(f"{Fore.YELLOW}Masukkan folder penyimpanan (kosongkan untuk default): {Style.RESET_ALL}") or "downloads"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    progress_bar = ProgressBar()
    ydl_opts = {
        'format': format_map.get(quality, 'best'),
        'outtmpl': os.path.join(output_folder, f'{platform}_video.mp4'),
        'progress_hooks': [progress_bar.hook],
        'continuedl': True,  # Resume download jika terputus
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"{Fore.RED}❌ Terjadi kesalahan saat mengunduh video: {e}{Style.RESET_ALL}")

def download_audio(url):
    if not is_valid_url(url):
        print(f"{Fore.RED}❌ URL tidak valid!{Style.RESET_ALL}")
        return

    output_folder = input(f"{Fore.YELLOW}Masukkan folder penyimpanan (kosongkan untuk default): {Style.RESET_ALL}") or "downloads"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, 'audio.mp3'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"{Fore.RED}❌ Terjadi kesalahan saat mengunduh audio: {e}{Style.RESET_ALL}")

def main():
    clear_screen()
    print(ascii_art)

    print(f"{Fore.BLUE}Pilih platform video yang ingin diunduh:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[1] YouTube{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[2] Facebook{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[3] TikTok{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[4] Unduh Audio (MP3){Style.RESET_ALL}")
    print(f"{Fore.CYAN}[0] Keluar{Style.RESET_ALL}")

    choice = input(f"\n{Fore.GREEN}Masukkan pilihan (1/2/3/4/0): {Style.RESET_ALL}")

    if choice == "1":
        url = input(f"{Fore.BLUE}Masukkan URL video YouTube: {Style.RESET_ALL}")
        download_video(url, "youtube")

    elif choice == "2":
        url = input(f"{Fore.BLUE}Masukkan URL video Facebook: {Style.RESET_ALL}")
        download_video(url, "facebook")

    elif choice == "3":
        url = input(f"{Fore.BLUE}Masukkan URL video TikTok: {Style.RESET_ALL}")
        download_video(url, "tiktok")

    elif choice == "4":
        url = input(f"{Fore.BLUE}Masukkan URL video untuk diunduh sebagai MP3: {Style.RESET_ALL}")
        download_audio(url)

    elif choice == "0":
        print(f"\n{Fore.BLUE}Terima kasih telah menggunakan Downloader Video! 🚀{Style.RESET_ALL}")
        sys.exit()

    else:
        print(f"{Fore.RED}❌ Pilihan tidak valid! Silakan coba lagi.{Style.RESET_ALL}")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()