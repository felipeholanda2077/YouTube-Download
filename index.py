# Precisa ter a biblioteca Pytube instalada no computador para funcionar.

from pytube import YouTube
link = input("Enter URL of Video")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()

#-----------------ou---------------

from pytube import YouTube, streams

url = input(str('Url para download: '))

video = YouTube(url)

stream = video.streams.get_highest_resolution()

stream.download(output_path='C:/Users/felip/OneDrive/Documentos/YouTube-Abaixador')

print('Download concluido com sucesso!')
