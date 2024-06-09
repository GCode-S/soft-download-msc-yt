import os
from pytube import YouTube
from moviepy.editor import *

# Função para baixar o vídeo do YouTube e converter para MP3
def download_and_convert(url):
    try:
        # Baixando o vídeo
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        temp_path = os.path.join('temp', 'temp.mp4')
        video.download(filename=temp_path)

        # Convertendo para MP3
        video_clip = AudioFileClip(temp_path)
        output_path = os.path.join('download', f'{yt.title}.mp3')
        video_clip.write_audiofile(output_path)

        print(f'O vídeo "{yt.title}" foi convertido para MP3 e salvo em {output_path}')
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    # Lista de URLs dos vídeos do YouTube
    # Pegando a Lista das Urls a partir de um documento de texto chamado listUrls.txt
    urls = []

    with open('listUrls.txt', 'r') as file:
        for l in file:
            urls.append(l.strip())
    

    # Criando a pasta 'download' se ela não existir
    if not os.path.exists('download'):
        os.makedirs('download')

    # Criando a pasta 'temp' se ela não existir
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # Loop sobre cada URL e baixar/convertê-lo
    for url in urls:
        download_and_convert(url)
