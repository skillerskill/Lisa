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


# Automação de Sistema com Python

Este projeto apresenta uma série de funções em Python para automação de tarefas do sistema operacional. Inclui funcionalidades como exibir informações do sistema, gerenciamento de arquivos, controle de energia, e outras ações úteis.

## Código Completo

```python
import os
import platform
import psutil
import subprocess
import datetime
import webbrowser
import socket
import pyttsx3

# Inicializando a síntese de fala
engine = pyttsx3.init()

def falar(texto):
    """Faz o sistema falar o texto especificado."""
    engine.say(texto)
    engine.runAndWait()

# Funções de Sistema
def obter_hora_atual():
    """Retorna a hora atual."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def obter_data_atual():
    """Retorna a data atual."""
    return datetime.datetime.now().strftime("%d/%m/%Y")

def obter_ano_atual():
    """Retorna o ano atual."""
    return datetime.datetime.now().year

def especificacoes_computador():
    """Retorna informações sobre o computador."""
    return {
        "Sistema Operacional": platform.system(),
        "Versão do SO": platform.version(),
        "Nome do Computador": platform.node(),
        "Arquitetura": platform.architecture(),
        "Processador": platform.processor(),
        "Usuário": os.getlogin()
    }

def porcentagem_bateria():
    """Retorna a porcentagem da bateria."""
    battery = psutil.sensors_battery()
    return battery.percent if battery else "Sem informações sobre bateria."

def abrir_programa(nome_programa):
    """Abre um programa pelo nome."""
    os.system(f"start {nome_programa}")

def listar_diretorio(caminho='.'):
    """Lista os arquivos e pastas de um diretório."""
    return os.listdir(caminho)

def desligar_computador():
    """Desliga o computador."""
    os.system("shutdown /s /t 1")

def reiniciar_computador():
    """Reinicia o computador."""
    os.system("shutdown /r /t 1")

def redes_disponiveis():
    """Lista redes Wi-Fi disponíveis."""
    resultado = subprocess.check_output("netsh wlan show networks", shell=True).decode()
    return resultado

# Exemplos de uso
if __name__ == "__main__":
    falar("Bem-vindo! Vamos testar os comandos.")

    print(f"Hora atual: {obter_hora_atual()}")
    print(f"Data atual: {obter_data_atual()}")
    print(f"Ano atual: {obter_ano_atual()}")
    print(f"Especificações do computador: {especificacoes_computador()}")
    print(f"Porcentagem da bateria: {porcentagem_bateria()}%")

    # Exemplos de ações
    # falar(f"Agora são {obter_hora_atual()} e a data é {obter_data_atual()}")
    # abrir_programa("notepad")  # Abre o Bloco de Notas
    # print(listar_diretorio("."))  # Lista o diretório atual
    # print(redes_disponiveis())  # Lista redes Wi-Fi disponíveis

#Explicando o comando

Aqui está o conteúdo explicado no formato de um arquivo `README.md`:

```markdown
# Assistente de Voz em Python

Este projeto é um assistente de voz simples, desenvolvido em Python, que utiliza reconhecimento de fala para capturar comandos do usuário, executa ações específicas e responde utilizando síntese de voz.

## Funcionalidades
- **Reconhecimento de fala**: Converte comandos de áudio em texto.
- **Síntese de voz**: Responde ao usuário falando os textos.
- **Execução de comandos**:
  - Abrir o navegador.
  - Encerrar o programa.
- **Reconhecimento online e offline**: Funciona com ou sem internet.
- **Configuração personalizada do microfone**.

## Pré-requisitos
Certifique-se de ter o Python instalado no seu sistema e instale as seguintes bibliotecas:
```bash
pip install SpeechRecognition pyttsx3
```

## Configuração
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/assistente-voz-python.git
   cd assistente-voz-python
   ```
2. Instale as dependências listadas acima.
3. Execute o programa:
   ```bash
   python assistente.py
   ```

## Explicação do Código

### 1. Importação de Módulos
O código utiliza bibliotecas essenciais para reconhecimento de fala, síntese de voz, navegação na web e verificação de conexão com a internet.

### 2. Inicialização
- `speech_recognition.Recognizer`: Inicializa o reconhecedor de fala.
- `pyttsx3.init`: Configura o mecanismo de síntese de voz.

### 3. Configuração da Voz
A função `configurar_voz_para_portugues()` ajusta a voz para português, se disponível no sistema.

### 4. Reconhecimento de Fala
A função `capturar_audio()`:
- Ajusta o ruído ambiente.
- Escuta o áudio do microfone.
- Converte o áudio em texto usando:
  - **Google Speech API** (online).
  - **Sphinx** (offline), caso não haja internet.

### 5. Comandos Disponíveis
- **"Abrir navegador"**: Abre o Google no navegador padrão.
- **"Fechar"**: Encerra o programa.
- **Outros comandos**: Informa que o comando não foi reconhecido.

### 6. Verificação de Conexão
A função `verificar_conexao_internet()` verifica se há conexão ativa tentando acessar o site do Google.

### 7. Listagem de Microfones
A função `listar_microfones()` exibe os microfones disponíveis no sistema para seleção.

### 8. Execução
O programa inicia listando os microfones e solicitando que o usuário escolha um. Após configurado, entra em um laço contínuo de captura de áudio, execução de comandos e resposta ao usuário.

## Como Usar
1. Execute o programa:
   ```bash
   python assistente.py
   ```
2. Escolha o microfone a ser usado.
3. Siga as instruções no terminal:
   - Diga "Abrir navegador" para abrir o Google.
   - Diga "Fechar" para encerrar o programa.

## Estrutura do Código
```python
├── configurar_voz_para_portugues()  # Configura a voz para português
├── falar(texto)                     # Faz o sistema falar
├── executar_comando(comando)        # Executa ações com base no comando
├── verificar_conexao_internet()     # Verifica conexão com a internet
├── listar_microfones()              # Lista microfones disponíveis
├── capturar_audio()                 # Captura e reconhece o áudio
└── __main__                         # Ponto de entrada
```

## Contribuição
Sinta-se à vontade para contribuir com melhorias neste projeto! Para isso:
1. Faça um fork do repositório.
2. Crie um branch com suas alterações.
3. Envie um pull request.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Contato
Caso tenha dúvidas ou sugestões, entre em contato:
- **Email**: seuemail@exemplo.com
- **GitHub**: [seuperfil](https://github.com/seuusuario)
```

Sinta-se à vontade para personalizar o conteúdo de acordo com suas preferências!