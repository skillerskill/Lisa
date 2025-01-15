# Lisa
Para TCC

# Lisa_ia
Este projeto é de uma assistente virtual para computadore


Aqui está um exemplo de `README.md` que você pode usar para seu projeto no GitHub:

```markdown
# Assistente Virtual de Comandos de Voz

Este projeto é uma aplicação simples de assistente virtual que responde a comandos de voz. O sistema pode funcionar tanto online quanto offline, utilizando reconhecimento de fala online (Google) ou offline (Pocketsphinx).

## Funcionalidades

- **Reconhecimento de fala**: O sistema pode ouvir e interpretar comandos de voz.
- **Comandos disponíveis**:
  - "Abrir navegador": Abre o navegador padrão e acessa o Google.
  - "Fechar": Fecha um programa específico (exemplo dado é para um programa chamado `programa.exe`).
- **Modo offline**: Se não houver conexão com a internet, o reconhecimento de fala será feito offline com a biblioteca `Pocketsphinx`.
- **Modo online**: Se houver internet, o reconhecimento de fala será feito utilizando a API do Google.

## Como Funciona

1. **Reconhecimento de fala online**: Utiliza a API do Google (requer conexão com a internet).
2. **Reconhecimento de fala offline**: Utiliza a biblioteca `Pocketsphinx`, funcionando sem conexão com a internet.

### Comandos suportados:
- **Abrir navegador**: Abre o navegador e acessa o Google.
- **Fechar**: Fecha um programa específico (exemplo dado: `programa.exe`).
  
### Dependências

- [speech_recognition](https://pypi.org/project/SpeechRecognition/): Para reconhecimento de fala.
- [pyttsx3](https://pypi.org/project/pyttsx3/): Para síntese de fala.
- [pocketsphinx](https://pypi.org/project/pocketsphinx/): Para reconhecimento de fala offline.
- [webbrowser](https://docs.python.org/3/library/webbrowser.html): Para abrir o navegador.

## Instalação

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/seu_usuario/assistente-virtual.git
cd assistente-virtual
```

### Passo 2: Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # No Linux/macOS
venv\Scripts\activate      # No Windows
```

### Passo 3: Instalar as dependências

```bash
pip install -r requirements.txt
```

Ou instale as dependências manualmente:

```bash
pip install speech_recognition pyttsx3 pocketsphinx
```

### Passo 4: Rodar o código

```bash
python assistente_virtual.py
```

## Código

```python
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import socket

# Inicializando o reconhecedor de fala e a síntese de fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def executar_comando(comando):
    if 'Abrir navegador' in comando:
        falar("Abrindo o navegador.")
        webbrowser.open('https://www.google.com')
    elif 'fechar' in comando:
        falar("Fechando o programa.")
        os.system('taskkill /f /im programa.exe')  # Exemplo para fechar um programa
    else:
        falar("Desculpe, não entendi o comando.")

def verificar_conexao_internet():
    try:
        # Tentativa de conexão com um servidor público
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except (socket.timeout, socket.gaierror):
        return False

while True:
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = recognizer.listen(source)

        try:
            if verificar_conexao_internet():
                # Usando o serviço online se houver conexão com a internet
                comando = recognizer.recognize_google(audio, language='pt-BR')
            else:
                # Usando o serviço offline (pocketsphinx) se não houver conexão com a internet
                comando = recognizer.recognize_sphinx(audio, language='pt-BR')

            print("Você disse: " + comando)
            executar_comando(comando)

        except sr.UnknownValueError:
            print("Não entendi.")
        except sr.RequestError:
            print("Erro de conexão com o serviço de reconhecimento de fala.")
```

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Certifique-se de que seu código esteja bem testado antes de enviar!

## Licença

Este projeto é de código aberto sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
```

### Detalhes importantes:
- **Instalação**: A instrução de instalação inclui um passo para criar um ambiente virtual e instalar as dependências.
- **Requisitos**: As dependências principais estão listadas, incluindo as bibliotecas `speech_recognition`, `pyttsx3`, `pocketsphinx` e `webbrowser`.
- **Código**: O código completo está incluído, com explicações sobre como ele funciona.
  
Você pode adicionar o `requirements.txt` com as dependências necessárias para facilitar a instalação:

```
speech_recognition
pyttsx3
pocketsphinx
```

Este `README.md` deve ser suficiente para que outros possam entender o propósito do projeto, instalá-lo e contribuir.
