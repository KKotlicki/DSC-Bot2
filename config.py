prefix = '?'
mp3_dir = 'music'
pic_dir = 'co_memes'
res_dir = 'resources'
temp_mp3_name = 'song.mp3'
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
