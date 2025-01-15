import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import socket
import time
from colorama import Fore, Style, init
import winsound

# Inicializando o colorama para colorir o console
init(autoreset=True)

# Inicializando o reconhecedor de fala e a síntese de fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configurando a voz para português
def configurar_voz_para_portugues():
    """Configura a voz do pyttsx3 para português."""
    for voice in engine.getProperty('voices'):
        if 'portuguese' in voice.languages or 'pt' in voice.id:
            engine.setProperty('voice', voice.id)
            break
    else:
        print("Voz em português não encontrada. Usando a voz padrão.")

configurar_voz_para_portugues()

def falar(texto):
    """Faz o sistema falar o texto especificado com um ícone de robô e cor amarela."""
    print(Fore.YELLOW + f"🤖 Jarvis: {texto}" + Style.RESET_ALL)
    winsound.Beep(1000, 500)  # Som de "ping" ao começar a falar
    engine.say(texto)
    engine.runAndWait()

def executar_comando(comando):
    """Executa comandos específicos baseados no que foi dito."""
    if 'abrir navegador' in comando.lower():
        falar("Abrindo o navegador.")
        webbrowser.open('https://www.google.com')
    elif 'fechar' in comando.lower():
        falar("Fechando o programa.")
        exit()
    elif 'ora' in comando.lower():
        falar(f"A hora atual é {obter_hora_atual()}.")
    else:
        falar("Desculpe, não entendi o comando.")

def obter_hora_atual():
    """Retorna a hora atual."""
    return time.strftime("%H:%M:%S")

def verificar_conexao_internet():
    """Verifica se há conexão com a internet."""
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except (socket.timeout, socket.gaierror):
        return False

def listar_microfones():
    """Lista todos os microfones disponíveis."""
    print("Microfones disponíveis:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")

def capturar_audio():
    """Captura áudio do microfone e retorna o texto reconhecido."""
    try:
        with sr.Microphone() as source:
            print(Fore.GREEN + "Você: ", end="")  # Exibe "Você: " em verde
            recognizer.adjust_for_ambient_noise(source, duration=2)  # Ajusta para o ruído ambiente
            audio = recognizer.listen(source)

            if verificar_conexao_internet():
                # Usando reconhecimento online (Google)
                return recognizer.recognize_google(audio, language='pt-BR')
            else:
                # Usando reconhecimento offline (Sphinx)
                return recognizer.recognize_sphinx(audio, language='pt-BR')

    except sr.UnknownValueError:
        return "Não entendi."
    except sr.RequestError as e:
        return f"Erro no serviço de reconhecimento: {e}"

if __name__ == "__main__":
    # Listar microfones para garantir que o correto será usado
    listar_microfones()

    # Selecionar o microfone correto (substituir o índice pelo desejado)
    microfone_id = int(input("Digite o número do microfone que deseja usar: "))
    with sr.Microphone(device_index=microfone_id) as source:
        print(Fore.GREEN + "Configuração concluída. Sistema iniciado!" + Style.RESET_ALL)
        while True:
            comando = capturar_audio()
            print(Fore.GREEN + comando)  # Exibe o comando do usuário em verde
            executar_comando(comando)
