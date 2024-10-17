from pytube import YouTube
from pathlib import Path
from os import startfile
from pywebio.input import input
from pywebio.output import put_text, put_html

import urllib

# Modifique o header do User-Agent
urllib.request.install_opener(
    urllib.request.build_opener(
        urllib.request.ProxyHandler({}),
        urllib.request.HTTPHandler(),
        urllib.request.HTTPSHandler(),
        urllib.request.BaseHandler()
    )
)

def video_download():
    while True:
        video_link = input("Informe o link do vídeo: ")
        
        # Verificar se o link começa com "https://"
        if video_link.startswith("https://"):
            put_html("<h1 style='color: red; font-size:50px;'>Fazendo o download do vídeo...</h1>")
            
            try:
                # Fazer o download do vídeo
                video_url = YouTube(video_link)
                video = video_url.streams.get_highest_resolution()
                
                # Definir o caminho de download
                path_to_download = Path(r"c:\users\user\Desktop")
                
                # Fazer o download do vídeo
                video.download(str(path_to_download))
                
                put_html("<h1 style='color: red; font-size:50px;'>Vídeo baixado com sucesso!</h1>")
                
                # Abrir o diretório
                startfile(path_to_download)
                
            except Exception as e:
                put_text(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    video_download()