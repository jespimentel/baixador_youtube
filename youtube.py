################################################################
#
# Extrai áudio ou vídeo a partir de uma lista de URLs do YouTube
#
#                 Autor: José E. S. Pimentel
#                                
################################################################

import pafy

pasta_de_download = 'C:\\Users\\jepim\\Downloads' # Altere conforme o caso
opcao = input ('Somente audio? (y/n): ')
lista = input ("Entre com a lista de URLs separadas por ',': ")
lista = lista.split(',')
print()

def get_audio(url_video, pasta_de_download):
  try:
    v = pafy.new(url_video)
    audio = v.getbestaudio(preftype='m4a')
    print ('Baixando o áudio de ' + url_video)
    audio.download(pasta_de_download)
  except:
    print ('Erro com a url: ' + url_video + '\n')

def get_video(url_video, pasta_de_download):
  try:
    v = pafy.new(url_video)
    video = v.getbest()
    print ('Baixando o vídeo de ' + url_video)
    video.download(pasta_de_download)
  except:
    print ('Erro com a url: ' + url_video + '\n')

for l in lista:
    l = l.replace (' ', '')
    if opcao == 'y':
        get_audio(l, pasta_de_download)
    else:
        get_video(l, pasta_de_download)

print ('Programa concluído')
