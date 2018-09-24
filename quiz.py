# encoding: utf-8
import os, sys

# Mini banco de dados
frase_facil = "Mais __0__ um __1__ na __2__ do que dois __3__."
frase_medio = "De __0__ e de __1__ todo __2__ tem um __3__."
frase_dificil = "Água __0__, __1__ dura, tanto __2__ até que __3__."
frases = [frase_facil, frase_medio, frase_dificil]
respostas_facil = ['vale', 'pássaro', 'mão', 'voando']
respostas_medio = ['médico', 'louco', 'mundo', 'pouco']
respostas_dificil = ['mole', 'pedra', 'bate', 'fura']
respostas = [respostas_facil, respostas_medio, respostas_dificil]
niveis = ['fácil', 'médio', 'difícil']
chances = [3, 2, 1]
# Define variável global para limpar a tela e será alimentada posteriormente pela função selecionaSO
limpar_tela = ""

# Função que define o SO e atribui o comando respectivo para limpar a tela em "clear"
# Aprendi sobre o comando os.system em:
# https://stackoverflow.com/questions/18937058/clear-screen-in-shell/31871439


def selecionaSO():
    while True:
        sistema_operacional = raw_input("Escolha um sistema operacional (Windows | Linux): ").lower()
        if sistema_operacional == "windows":
            limpar_tela = os.system('cls')
            break
        if sistema_operacional == "linux":
            limpar_tela = os.system('clear')
            break
        else:
            print "Opção inválida"

# Função que define o nível que o jogador irá jogar
# Loop roda até que usuário entre com um valor válido
# O valor é válido quando é igual a algum valor na lista níveis
# O retorno da função é a posição que nível está na lista


def selecionar_nivel():
    selecionaSO()
    while True:
        nivel = raw_input("Escolha um nível ( fácil | médio | difícil): ").lower()
        if nivel in niveis:
            return niveis.index(nivel)
        limpar_tela
        print "Opção inválida"

# A função abaixo recebe a posição (1,2,3) selecionada pelo usuário e retorna a frase, respostas
# e chances utilizando suas respectivas listas salvando tudo na variável nivel_selecionado


def controlar_nivel():
    nivel = selecionar_nivel()
    nivel_selecionado = (frases[nivel], respostas[nivel], chances[nivel])
    print ("Você tem {} chances para errar!".format(chances[nivel]))
    return nivel_selecionado

# A função abaixo recupera os valores separados de nivel_selecionado de acordo com input do usuário
# Exibe a quantidade de tentativas de acordo com a dificuldade selecionada
# Entra na condição de se as tentativas forem maior que -1 e o incremento do indice for menor que
# a quantidade de respostas, exibe o loop


def jogar_nivel():
    (frase, respostas, tentativas) = controlar_nivel()
    indice = 0
    while tentativas > -1 and indice < len(respostas):
        print(frase)
        palavra = raw_input("A palavra do campo __{}__ é? ".format(indice)).lower()
        if palavra in respostas[indice]:
                print "\nCerta resposta!\n"
            frase = frase.replace("__{}__".format(indice), respostas[indice])
            indice += 1
        else:
            tentativas -= 1
    resultado_final = tentativas, frase
    return resultado_final


def jogar():
    tentativas, frase = jogar_nivel()
    if tentativas == -1:
        limpar_tela
        print "\nFim de jogo! Você não conseguiu acertar todas as palavras."
    else:
        limpar_tela
        print "Você acertou todas as palavras do quiz!\n"
        return frase


print jogar()
