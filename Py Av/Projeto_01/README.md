### Intruções de como instalar o ambiente virtual utilizando pyenv



- Instalar no powershell global

        Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"



- Depois ir para a pasta do projeto, e lá dar o comando para instalar uma versão local:

     ###Para instalar na maquina:
    pyenv install (versão- ex: 2.7)

    ###Para instalar no projeto:
    pyenv local (versão)

- Ao utilizar o comando abaixo, o terminal irá exibir qual versão do python está instalada no projeto local, e qual está no escopo global da maquina.

    python --version

### OBS: O PYENV vai instalar uma versão de python diferente para cada projeto.