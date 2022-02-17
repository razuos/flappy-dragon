<p align="center">
    <img align="left" src="https://raw.githubusercontent.com/razuos/flappy-dragon/main/assets/barrier/bottom.png" alt="Barrier">
    <img src="https://raw.githubusercontent.com/razuos/flappy-dragon/main/assets/barrier/top.png" alt="Barrier">
    <img align="right" src="https://raw.githubusercontent.com/razuos/flappy-dragon/main/assets/character/character.png" alt="Dragon">
</p>

# flappy-dragon

Flappy Dragon é um jogo desenvolvido utilizando a biblioteca Graphics (John Zelle) onde um dragão deve desviar de obstáculos gerados de forma aleatória.

## Como inicializar

As dependências são Python3 e Tkinter, podem ser instaladas em um sistema com APT dessa forma: `sudo apt install python3 python3-tk`.

## Arquitetura

O jogo foi escrito com GameObjects (como os utilizados em Unity) e GameStates em mente.

### GameObjects

Existem 5 GameObjects: `Barrier`, `Character`, `Lost`, `Menu` e `Score`. Os objetos `Lost`, `Menu`, e `Score` são elementos da interface gráfica. Já o `Barrier` e o `Character` são objetos atrelados à gameplay. Podem ser encontrados no diretório `gameObjects`, em seus respectivos arquivos.

### Obstáculos

Os obstáculos são divididos em três componentes: base, meio e topo. Como um obstáculo pode ser maior que outro, podem ter mais de um meio, mas sempre terão uma base e um topo. Os componentes estão na pasta `assets/barrier`.

### Pontuação

A pontuação é incrementada com o tempo sobrevivido, nada muito complexo.

### GameStates

O jogo possui 3 estados: `MENU`, `MAIN` e `LOST`. Os estados `MENU` e `LOST` são auto-explicativos e o estado `MAIN` ocorre quando o jogador está jogando, efetivamente. Os estados estão definidos em `game.py`