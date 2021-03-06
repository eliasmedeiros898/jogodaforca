import random
from words import words
from dicas import dicas
from words_backup import words_backup
import string
import emoji
import os
from time import sleep


def palavra_valida(words):

    palavra = random.choice(words)
    
    while "-" in palavra or " " in palavra or len(palavra) > 14:
        palavra = random.choice(words)
    
    words.remove(palavra)
    return palavra.upper()
            


    

def jogo_da_forca():
    palavra = palavra_valida(words) #pegando uma palavra válida da lista
    letras_palavra = set(palavra) #criando uma coleção com as letras da palavra
    alfabeto = set(string.ascii_uppercase) #definindo os caracteres válidos em UPPERCASE
    letras_usadas = set() # coleção que irá ser incrementada com o decorrer do programa
    vida = 10
    pontos = 0
    
    
    while vida > 0  and len(letras_palavra) > 0: #loop que irá funcionar até ser zerada a coleção de letras da palavra ou as vidas

        
        print(emoji.emojize(f"Vidas({vida}): "+ vida*":heart: ", language='alias'))

        print("Letras usadas -> "," ".join(letras_usadas)) #mostrar as letras usadas pelo usuário até o momento

        mostrar_lista_letras = [letra_usuario if letra_usuario in letras_usadas else "-" for letra_usuario in palavra]
        print("Palavra atual -> ", "".join(mostrar_lista_letras))


        letra_usuario = input("Chute uma letra: ").upper() 
        
       

        if letra_usuario in alfabeto - letras_usadas: #condição que adicionará a letra digitada a lista de letras digitadas
            letras_usadas.add(letra_usuario)
            os.system("cls")
            if letra_usuario in letras_palavra:#condição que irá reduzindo as letras da palavra até que chegue a zero
                letras_palavra.remove(letra_usuario)
                print(emoji.emojize("\033[1;32mCorreto! ✅\033[m",language='alias'))
            else:
                vida -= 1
                os.system("cls")
                print("\033[1;31mEssa letra não pertence a palavra, -1 vida\033[m")
                
        elif letra_usuario in letra_usuario:
            os.system("cls")
            print("\033[1;33mVocê já digitou essa letra, tente novamente\033[m")
            
        else:
            os.system("cls")
            print("Você não digitou uma letra válida, tente novamente")

        if vida == 5:
            for i in range(0,30):
                if palavra == words_backup[i].upper():
                    print(f"\033[1;32m{dicas[i]}\033[m")
                
            
        
            
    print(f"A palavra é: {palavra}")
    print(f"Pontos feitos: {vida}")
    sleep(3)
    os.system("cls")
    pontos = vida
    return pontos
    
    
print("\033[1;32m")
num_times = int(input("Quantos times irão jogar? "))
print("\033[m")
os.system("cls")
cont = 0
pont_final_times = [0] * num_times

while cont < 5: #número de rodadas a serem jogadas
    cont+=1
    for i in range(0,num_times):
        pontos = 0
        print(f"\033[1;92mRodada {cont} / Time {i+1}\033[m: \n")
        pont_final_times[i] += jogo_da_forca()
        
        


os.system("cls")
print("Pontuação final: \n")

for i in range(0,num_times):
    print(f"\033[1;36mTime {i+1} = {pont_final_times[i]} pontos\033[m\n")








