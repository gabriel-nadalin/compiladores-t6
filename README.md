# Linguagem NOTA
Notação Objetiva Tonal Audível


Uma apresentação da linguagem pode ser encontrada em : https://drive.google.com/drive/folders/1RT8eKFo1_1T6KRy3NL8tELw8fHCr7z34?usp=sharing

# Como rodar?
1. Faça o setup inicial do projeto, buildando o sintetizador e instalando as dependências do python
```sh
sudo apt install python3-venv
./setup_project
```
2. Ative o Virtual Environment do python
```sh
source venv/bin/activate
```
3. Rode o programa com o comando
```sh
python3 -m compilador.main <Path do arquivo fonte>
```
O output sairá na pasta `wav`

Exemplos de músicas podem ser encontrados na pasta `musicas`

Além disso, é possível criar somente o arquivo midi usando a tag '--midi-only'
```sh
python3 -m compilador.main <Path do arquivo fonte> --midi-only
```


# Sintaxe da linguagem
## Nota
A nota é o componente mais fundamental da linguagem. Cada nota será identificada e traduzida para dentro do arquivo midi, que pode ser lido por sintetizadores e programas específicos.

A linguagem aceita as notas `C`, `D`, `E`, `F`, `G`, `A`, `B`, incluindo os acidentes `#` e `b`.

Cada nota deve acompanhar sua oitava, na qual são aceitas as oitavas de `1` até `8`

Deste modo, a notação de acordes fica:

```
A4
Bb5
G#3
...
```
## Acordes
É combinar várias e compor acordes. O acorde é definido por todas as notas que foram definidar de `{` `}`
```
// Acorde dó maior
{ C4 E4 G4 }

// Acorde ré menor à sétima 
{ D4 F#4 A4 C5 }
```
> A linguagem não aceita repetição de notas dentro de um acorde

Os acordes também podem receber um identificador, de modo que um acorde definido pode ser repedido várias vezes invocando somente o seu nome.

A estrutura de definição de nome é a seguinte:
```
// Acorde dó maior
acorde do_maior{
    C4 E4 G4
}

// Acorde ré menor à sétima 
acorde re_menor_7 { D4 F#4 A4 C5 }
```

## Eventos
Por si só, as notas e acordes não tem significado se não houver uma notação de tempo para tocá-los. Deste modo, a linguagem nota apresenta o conceito de "Evento".

Evento são a combinação de uma nota ou acorde (identificador ou definição imediata) seguida pelo tempo que eles devem ser tocados em milisegundos
```
// Declarações
acorde do_maior { C4 E4 G4 }(1000)

// Execução
// Nota lá por 15 segundos
A4(15000)

// Acorde dó maior por meio segundo
do_maior(500)

// Ré menor à sétima por 735 milissegundos
{ D4 F#4 A4 C5 }(735)
```
> O compilador não aceita chamadas de notas e acordes sem ser por meio de um evento
## Pausas
Além das notas e acordes, outro tipo de evento possível são pausas. Pausas são tempos de silêncio que vão acontecer entre o fim da execução do último "som" e a execuçao do próximo. Pausas também são definidas como um evento, ou seja, precisam estar em notação de eventos
```
// Dó maior
{ C4 E4 G4 }(900)

// Pausa - tempo em silêncio - de 150 ms
pausa(150)

// Ré menor à sétima 
{ D4 F#4 A4 C5 }(1410)
``` 

## Frases
Por fim, é possível definir frases. Frases são conjuntos de eventos que podem ser chamados novamente. Quanto a linguagens de programações no geral, seriam uma espécie de função.


```
// do re mi fa fa fa
// Declaração da frase
frase do_re_mi_fa_fa{
    C4(300)
    D4(300)
    E4(300)
    F4(300)
    pausa(300)
    F4(300)
    F4(300)
    pausa(300)

    C4(300)
    D4(300)
    C4(300)
    D4(300)
    pausa(300)
    D4(300)
    D4(300)
    ...
}

// Chamada da frase
do_re_mi_fa_fa_fa
``` 
> Note que, diferente dos eventos, frases nao recebem notação de tempo, uma vez que ela já possui eventos em si.


# Funcionamento do compilador
O compilador da linguagem NOTA le os arquivos fonte ".nota" passados para ele, interpreta os tokens e elementos sintáticos usando o antlr e gera uma árvore sintática. Após isso, o compilador faz uma análise semântica, buscando compreender a corretude gera do programa e por fim produz um arquivo midi, que pode ser executado por um sintetizador.



# Integrantes do grupo
Augusto dos Santos Gomes Vaz - 800268
Gabrielly Castilho Guimarães - 805757
Gabriel Kusumota Nadalin - 819498
