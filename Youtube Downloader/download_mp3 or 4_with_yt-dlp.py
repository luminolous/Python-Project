import yt_dlp

url = input('Input URL here: ')
format = input('format of file (mp3/mp4): ').upper()

if format == 'MP3':
    # MP3 Download
    ydlOpts = {
        'format': 'bestaudio/best',
        'outtmpl': r'C:\audio.%(ext)s'
    ,
    }
elif format == 'MP4':
    # MP4 Download
    ydlOpts = {
        'format': 'best',  
        'outtmpl': r'C:\video.%(ext)s',  
    }

with yt_dlp.YoutubeDL(ydlOpts) as ydl:
    ydl.download([url])

print("Download selesai!")
