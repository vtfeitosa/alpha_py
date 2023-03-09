## Intruções de como instalar o ambiente virtual utilizando PYENV

#

- Instalar no powershell global

        >   Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"



- Depois ir para a pasta do projeto, e lá dar o comando para instalar uma versão local:

    #### Para instalar na maquina:
        > pyenv install (versão- ex: 2.7)

    #### Para instalar no projeto:
        > pyenv local (versão)

- Ao utilizar o comando abaixo, o terminal irá exibir qual versão do python está instalada no projeto local, e qual está no escopo global da maquina.

        > python --version

- Com esse comando, você irá executar o arquivo que importa a função que exibe o print indicando a versão local:


    #### Executa o aquivo.py : 
        > python (nome do aquivo .py)


### OBS: O PYENV vai instalar uma versão de python diferente para cada projeto.

#

## Intruções de como instalar o ambiente virtual utilizando VirtulEnv

#

- Dentro da pasta do projeto, dar o comando para criar o ambiente virtual:

        > virtualenv (nome do ambiente)

        > (nome do ambiente)/Scripts/Activate

- Sair do Ambiente

        > deactivate

#

## Intruções de como instalar a biblioteca Numpy

- Dentro do projeto e do ambiente virtual escolhido, executar o código abaixo para instalar o Numpy:

        > pip install numpy

- Com esse comando, você irá executar o arquivo que importa a função que exibe o print indicando a versão do Numpy que está no projeto local:

     #### Executa o aquivo.py : 
        > python (nome do aquivo .py)