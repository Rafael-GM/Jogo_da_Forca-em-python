# vamos usar 3 bibliotecas: os para limpar, random para gerar nomes aleatórios e time para o tempo ir mais devagar.
import os, time, random

# ======================================variáveis globais==================================
# agora vou fazer variáveis globais q vou usar como vida, erros etc...
tentativas = 0;
palavras_certa = 0;
palavras_erradas = 0;
palavra_em_jogo = 0;
letras_ja_digitadas = [];

vidas = 5;
pontos = 0;

# vamos fazer a variável para limpar quando terminar.
# vamos chamar a biblioteca os.
# estou dizendo abaixo q se o os(sistema operacional for do tipo nt vai ser limpado se for de outro tipo vai ser limpado tbm.)
limpar = "os.system( 'cls' if os.name == 'nt' else 'clear')"

# nosso jogo ja vai vim com algumas palavras adcionadas
def palavras_do_jogo():

    palavra = ["banana","laranja","abacaxi","coco","uva","damasco","caqui","melancia","cereja","goiaba","acerola","ameixa",
        "amora","cacau","caju","carambola","figo","framboesa","pinha","graviola","groselha","jabuticaba","jaca","jambo",
		"kiwi","limao","manga","maracuja","morango","pera","pitanga","tangerina","ramon","renan","lucas","exodo","little",
		"joao","tyler","gustavo","thiago","francisco","jose","renata","janaina","olivia","camila","paula","otavio","carlos",
		"wesley","felipe","davi","luciana","fernanda","alvissaras","beneplacito","empedernido"]
    palavras = []
    pala_fatiada = []
    for i in palavra:               #estou fatiando elas para ficar as letras.
        for let in i:
            pala_fatiada.append(let)
        palavras.append(pala_fatiada)
        pala_fatiada = []
    return palavras

palavras = palavras_do_jogo()


# ===========================================================================================


# ======================================== interface =======================================

def cabecalho():
    print("|==============================================================|")
    print("|                        JOGO DA FORCA                         |")
    print("|==============================================================|")


def placar(p1,p2,p3,p4,p5,p6): #quando invocar placar vou passar o valor dos parâmetros de cada p.
    cabecalho()
    print("|                           Vidas: ", str(p1), "                         |")
    print("|                                                              |")
    print("| Palavras Certas =",str(p2),"                    Palavras Erradas=",str(p3)," |")
    print("| Tentativas =",str(p4),"                         Pontos =",str(p5),"          |")
    print("|==============================================================|")
    print("| Letras ja Digitadas:",','.join(letras_ja_digitadas)," ")
    print("|                                                              |")
    print("|                       ",' '.join(p6),"                        ") #a função join tira isso ["_","_","_"] e deixa assim _ _ _
    print("|--------------------------------------------------------------|")


def fim():
    print("|==============================================================|")
    print("|                   OBRIGADO POR JOGAR ^_^                     |")
    print("|==============================================================|")

def game_over():
    print("|==============================================================|")
    print("|                          GAME OVER                           |")
    print("|==============================================================|")
# =============================================================================================


# ============================================jogo=========================================

# =========================================================================================
# aqui vou fazer a função da pergunta para saber se ele quer adcionar mais nomes.
# vou passar 2 parâmetros questão e erros para caso der um erro.
def pergunta(questao, erro="| Digite S para SIM e N para NÃO."):
    try:  # serve para fazer uma verificação.
        resposta = input(questao)
        if resposta[0] == "S" or resposta[0] == "s":  # coloquei [0] pq o usuário pode colocar sim no lugar de s e com isso o programa vai pegar so a primeira letra q vai ser o s.
            return True
        elif resposta[0] == "N" or resposta[0] == "n":
            return False
        else:
            print(erro)
    except:  # parece com o try só q ele vai verificar uma exeção no meu código.
        print("| Verifique se digitou um valor aceito.")


# ============================================================================================


#=============================================================================================
#vou fazer a função que pede para o usuário digitar uma letra.
def letra_digitada(questao):

    while True:
        try:  # serve para fazer uma verificação.
            respost = input(questao)
            return respost[0]

        except:
            print("| Verifique se digitou um valor aceito.")
#=============================================================================================


# ============================================================================================
# aqui vou fazer a função para resetar as palavras originias da variável palavra.
def reset_palavra():
    palavras = palavras_do_jogo()
    return palavras


# ============================================================================================


# ============================================================================================
# vou fazer a função do gerenciador de arquivo para saber qual a palavra ele vai adcionar.
def gerenciador_de_palavras():
    # vou começar limpando a tela e imprimindo o cabeçalho.
    eval(limpar)
    cabecalho()

    cont = 0  # vou usar para contar
    palavras_recebidas = []

    while True:
        cont += 1
        palavras_recebidas += [input(f"| Digite a {str(cont)}º palavra.\n|:")]
        print("|                                                              |")

        if not pergunta("| Quer adcionar mais palavras [S|N]?\n|:"):   #coloco o not pq só é para dar um break se for não
            break

    # vamos fazer com q ele pegue a nossa palavra digitada e fatie ela em pedaços.
    palavras_tratadas = []
    palavra_fatiada = []
    for palavra in palavras_recebidas:
        for letra in palavra:
            palavra_fatiada.append(letra)
        palavras_tratadas.append(palavra_fatiada)
        palavra_fatiada = []

    #vamos supor q o usuario Digite uma lista vazia, vamos ter q removela
    if [] in palavras_tratadas:

        lista_vazia = 0  #tenho q fazer essa variavel para depois percorrer, se nao se eu só pedir para excluir as palavras_tratadas[j] ele vai excluir somente uma, ja se fizermos a contagem não.
        for palavra in palavras_tratadas:   #estou percorrendo todas as listas digitadas
            if palavra == []:
                lista_vazia += 1    #estou dizendo q a cada lista vazia q tiver em palavra vai ser adcionado mais 1 na minha variável

        for i in range(lista_vazia):    #aqui vou percorrer o tanto de vezes q tem uma lista vazia
            for j in range(len(palavras_tratadas)): #vou ver todas as listas
                if palavras_tratadas[j] == []:  #pego somente as []
                    del(palavras_tratadas[j])
                    break

    return palavras_tratadas

# ============================================================================================
#==============================================================================================


#=============================================================================================
#vou criar a função q serve para escolher a palavra em jogo e trabalhar com tela.
def palavra_em_jogo(palavras):
    return palavras.pop(random.randint(0, len(palavras) -1))
palavra_para_tentativas = palavra_em_jogo(palavras)
#=============================================================================================


#=============================================================================================
#vamos fazer uma função para nos retornar o tanto de tentativas que vamos ter dependendo da palavra.
def numero_de_tentativas(palavra_em_jogo):

    if len(palavra_para_tentativas) <= 6:  #estou dizendo q se for igual ou nemor que 6 o numero de letras ele vai ter 3 tentativas
        tentativas = 3

    else:
        tentativas = len(palavra_para_tentativas) // random.randint(2,6)   #se não vai ser o numero de letras dividido por 2 3 ou 4
        if tentativas <= 2:     #se o numero depois da divisão for menor ou igual a 2 elevai receber mais 2
            tentativas +=2

    return tentativas

#=============================================================================================


#=============================================================================================
#vamos fazer a função das letra Certas
def letras_certas(palavra_em_jogo):

    letras = []

    quantidade = len(palavra_em_jogo) // 2
    for i in range(0, len(palavra_em_jogo)):
        letras.append("_")

    #caso eu queira q ja venha algumas letras à mostra
    for i in range(0, quantidade):  #estou indo de 0 a metade da minha palavra_em_jogo
        indice = random.randint(0, len(palavra_em_jogo) -1)     #a função randint vai mostrar para nós metade ou menos das letras que estar na palavra_em_jogo
        letras[indice] = palavra_em_jogo[indice]   # aqui estou adcionando as letras à mostra para a as letras

    return letras
#=============================================================================================
def image(p0):
    if p0 >= 5:
        print("""|                                                              |
|                   |||||||||||||                              |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                  ++++                                        |
|                 ++++++                                       |""")


    if p0 == 4:
        print("""|                                                              |
|                   |||||||||||||                              |
|                   ++         ***                             |
|                   ++        *   *                            |
|                   ++         ***                             |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                  ++++                                        |
|                 ++++++                                       |""")


    if p0 == 3:
        print("""|                                                              |
|                   |||||||||||||                              |
|                   ++         ***                             |
|                   ++        *   *                            |
|                   ++         ***                             |
|                   ++          |                              |
|                   ++          |                              |
|                   ++          |                              |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                  ++++                                        |
|                 ++++++                                       |""")


    if p0 == 2:
        print("""|                                                              |
|                   |||||||||||||                              |
|                   ++         ***                             |
|                   ++        *   *                            |
|                   ++         ***                             |
|                   ++         /|                              |
|                   ++        / |                              |
|                   ++          |                              |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                  ++++                                        |
|                 ++++++                                       |""")


    if p0 == 1:
        print("""|                                                              |
|                   |||||||||||||                              |
|                   ++         ***                             |
|                   ++        *   *                            |
|                   ++         ***                             |
|                   ++         /|\                             |
|                   ++        / | \                            |
|                   ++          |                              |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                   ++                                         |
|                  ++++                                        |
|                 ++++++                                       |""")


    if p0 == 0:
        print("""|                                                              |
|                   |||||||||||||                              |
|                   ++         ***                             |
|                   ++        *   *                            |
|                   ++         ***                             |
|                   ++         /|\                             |
|                   ++        / | \                            |
|                   ++          |                              |
|                   ++         /                               |
|                   ++        /                                |
|                   ++                                         |
|                   ++                                         |
|                  ++++                                        |
|                 ++++++                                       |""")


    if p0 == -1:
        print("""|                                                              |
|                   |||||||||||||                              |
|                   ++         ***                             |
|                   ++        *   *                            |
|                   ++         ***                             |
|                   ++         /|\                             |
|                   ++        / | \                            |
|                   ++          |                              |
|                   ++         / \                             |
|                   ++        /   \                            |
|                   ++                                         |
|                   ++                                         |
|                  ++++                                        |
|                 ++++++                                       |""")



    print("|                                                              |")





#=============================================================================================
adcionar = True
while adcionar:
    # vou usar o eval pq ela execulta oq estar em uma string, ou seja, ela vai execultar oq estar dentro de limpar.
    eval(limpar)
    cabecalho()

    # irei perguntar se vai querer adcionar mais palavras.
    if pergunta("| Quer adicionar mais palavras [S|N]?\n|:"):  # estou usando minha função pergunta q ja foi feita para esse tipo de pergunta sim ou não
        print("|                                                              |")
        # perguntar se o usuário deseja usar as palavras ja cadastradas no jogo.
        if pergunta("| Deseja usar as palavras ja cadastradas no jogo [S|N]?\n|:"):
            palavras += gerenciador_de_palavras()  # estou dizendo q se for sim minha variável global palavras vai receber a outra palavra q eu digitar em gerenciador de palavras
        else:
            palavras = gerenciador_de_palavras()  # ja aqui minha variável palavras vai ser igual a somente a palavra q eu digitar, as outras vao ser descartadas.

            # irei verificar se o usuario realmente digitou uma palavra.
            if palavras == []:  # estou vendo se a plavra estar vazia.
                palavras = reset_palavra()  # se estiver vou usar essa função para resetar as palavras originais do jogo.
                print("| Nenhuma palavra adcionada, usaremos as palavras do próprio jogo.")
                time.sleep(3)

    #incio do jogo

    game_on = True

    while game_on:
        palavra_ja_certa = palavra_em_jogo(palavras)
        tentativas = numero_de_tentativas(palavra_ja_certa)
        palavra_jogando= letras_certas(palavra_ja_certa)    # não coloquei palavra_em_jogo assim como na função feita pq se não, não poderia fazer o len(palavra_em_jogo) então tive q adcionar palavra_em_jogo a uma variável para colocar a variável no lugar

        #tentnado achar a letras

        start_game = True
        while start_game:
                eval(limpar)
                placar(vidas, palavras_certa, palavras_erradas, tentativas, pontos, palavra_jogando)     #esses são os valores dos p lá do placar


                image(vidas)

                #vou fazer a variavel da letra digitada.
                letra = letra_digitada("| Digite uma Letra: ")  #vou fazer essa função la encima.


                acertou = False   #vai começar como falso, caso ele acerte vai ser True

                for i in range(0, len(palavra_ja_certa)):   #vou ver todas as letras da palavra
                    if letra == palavra_ja_certa[i] and palavra_jogando[i] == "_":       #vou ver se a letra q eu digitei estar na palavras
                        palavra_jogando[i] = letra          #se tiver vou adcionar ela a minha variavel onde as letras estão escondidas

                        acertou = True      # se ele acertar vai ser True

                        #break       #esse break serve para evitar q uma palavra q tenha 2 letra "a" por exemplo imprima as duas, como ele só vai ser impresso uma, somente se eu digitar o "a" de novo q ele vai aparecer.

                #letras ja digitadas
                letras_ja_digitadas += letra

                #atualizando o placar.

                if not acertou:     #estou dizendo q se acertou = False , ou seja, se ele errou
                    tentativas -= 1
                    print("|                 Seu fraco :( Vc errou.                       |")
                    print("|                                                              |")
                    time.sleep(1)
                else:
                    if len(palavra_jogando) <= 6:
                        pontos += 1

                    elif len(palavra_jogando) >=7:
                        pontos += 2

                #verificação de pontos para ganhar vidas.
                if pontos >= 30:
                    print("| Você atingiu 30 pontos, tome mais uma vida para te ajudar.   |")
                    time.sleep(3)
                    vidas += 1
                    pontos = 0


                #vamos verificar se ele ecertou todas as letras
                completou = False

                if '_' not in palavra_jogando:      #estou verificando se na minha palavra ainda tem "_" se não tiver é pq terminei ela
                    completou = True        #se eu terminei então vai ser verdadeiro

                if completou:       #se for verdadeiro então palavras_certa vai receber 1 e start_game = False para para o ciclo e o jogo voltar para o ciclo de antes escolher outra palavra comecar de novo.
                    palavras_certa += 1
                    letras_ja_digitadas = []
                    eval(limpar)
                    placar(vidas, palavras_certa, palavras_erradas, tentativas, pontos, palavra_jogando)
                    print("|                                                              |")
                    if palavras_certa == 1:
                        print("|        Calma, não se afobe, agora que foi a primeira.        |")
                        time.sleep(3)

                    if palavras_certa == 2:
                        print("|                    Ainda estar pouco ;-;                     |")
                        time.sleep(2)

                    if palavras_certa == 3:
                        print("|           Você é melhorzinho do q eu pensei haha             |")
                        time.sleep(3)

                    if palavras_certa >= 4:
                        print("|              Nossa, vai lá, você consegui ^-^                |")
                        time.sleep(2)
                    start_game = False

                #verificar se ele acabou com suas tentativas
                if tentativas == 0:
                    palavras_erradas += 1
                    vidas -= 1
                    letras_ja_digitadas = []
                    eval(limpar)
                    placar(vidas, palavras_certa, palavras_erradas, tentativas, pontos, palavra_ja_certa)
                    image(vidas)
                    time.sleep(2)

                    start_game = False



                if palavras == [] and "_" not in palavra_jogando:
                    eval(limpar)
                    fim()
                    print("| Meus parabêns, você conseguiu concluir o jogo.")
                    time.sleep(3)

                    eval(limpar)


                    resposta = True
                    while resposta:
                        eval(limpar)
                        game_over()
                        try:
                            print("|                                                              |")
                            sair = input("| Quer iniciar um novo jogo[S|N]?                              |\n|:")
                            print("|                                                              |")

                            if sair[0] == "N" or sair[0] == "n":
                                resposta = False
                                game_on = False
                                adcionar = False
                            elif sair[0] == "S" or sair[0] == "s":
                                vidas = 5
                                palavras_erradas = 0
                                pontos = 0
                                palavras_certa = 0

                                resposta = False
                                game_on = False

                            else:
                                print("Dgite S para 'sim' e N para 'não'.")
                        except:
                            print("Verifique se digitou um valor válido.")

                #verificar se a vida chegou em 0
                if vidas == -1 :

                    eval(limpar)


                    resposta = True
                    while resposta:
                        eval(limpar)
                        game_over()
                        try:
                            print("|                                                              |")
                            sair = input("| Quer iniciar um novo jogo[S|N]?                              |\n|:")
                            print("|                                                              |")

                            if sair[0] == "N" or sair[0] == "n":
                                resposta = False
                                game_on = False
                                adcionar = False
                            elif sair[0] == "S" or sair[0] == "s":
                                vidas = 5
                                palavras_erradas = 0
                                pontos = 0
                                palavras_certa = 0

                                resposta = False
                                game_on = False

                            else:
                                print("Dgite S para 'sim' e N para 'não'.")
                        except:
                            print("Verifique se digitou um valor válido.")



eval(limpar)
fim()
