import random

import pygame
from pygame.locals import *     

#Criar um tabuleiro aleatório
def novo_tabuleiro(n, color1, color2, color3, color4, color5):
    
    #Criar a matriz
    tabuleiro = []
    for _ in range(15):
        game_matrix = []
        for _ in range(13):
            game_matrix += [random.randint(1,n),]
        tabuleiro += [game_matrix,]

    #Criar a parte gráfica
    for y in range(15):
        for x in range(13):   
            pos = (105+30*x, 150+30*y)
            if tabuleiro[y][x] == 1:
                block = color1
            if tabuleiro[y][x] == 2:
                block = color2
            if tabuleiro[y][x] == 3:
                block = color3
            if tabuleiro[y][x] == 4:
                block = color4
            if tabuleiro[y][x] == 5:
                block = color5
            screen.blit(block, pos)
    pygame.display.update()
    return tabuleiro

#Verificar as redondezas de onde o jogador escolheu a peça
def player_select(y, x, lista): 
    lenght_y = len(tabuleiro)
    lenght_x = len(tabuleiro[0])
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (0 <= i < lenght_y) and (0 <= j < lenght_x) and (0 <= y < lenght_y) and (0 <= x < lenght_x) and (i == y or j == x) and not (i == y and j == x):
                if tabuleiro[y][x] != 0:
                    if tabuleiro[i][j] == tabuleiro[y][x] and ((i,j) not in lista):                   
                        lista += [(i,j),]
                        lista += player_select(i, j, lista)
    
    group_selected = []
    for i in lista:
        if i not in group_selected:
            group_selected += [i,]
    return sorted(group_selected)

#Elimina uma coluna de 0 e acrescenta ao final aka unir colunas
def eliminar_coluna():
    for j in range(len(tabuleiro[0])):
        eliminar = True
        for i in range(len(tabuleiro)):
            if tabuleiro[i][j] != 0:
                eliminar = False
        if eliminar:
            for k in range(len(tabuleiro)):
                del tabuleiro[k][j]
                tabuleiro[k].append(0)
            return

#Remover peças do tabuleiro
def to_remove(tup):
    for i in tup:
        y = i[0]
        x = i[1]
        tabuleiro[y][x] = 0

#Atualizar o tabuleiro
def tabuleiro_update(color1, color2, color3, color4, color5):
    if not winner and not loser:
        for y in range(len(tabuleiro)):
            for x in range(len(tabuleiro[0])):
                if tabuleiro[y][x] == 0:
                    pygame.draw.rect(screen, (0,0,0), (105+30*x, 150+30*y, 20, 20))
                else:    
                    pos = (105+30*x, 150+30*y)
                    if tabuleiro[y][x] == 1:
                        block = color1
                    if tabuleiro[y][x] == 2:
                        block = color2
                    if tabuleiro[y][x] == 3:
                        block = color3
                    if tabuleiro[y][x] == 4:
                        block = color4
                    if tabuleiro[y][x] == 5:
                        block = color5
                    screen.blit(block, pos)
                pygame.display.update()

#Queda dos blocos
def search_zero():
    for y, linha in enumerate(tabuleiro):
        for x, block in enumerate(linha):
            if block == 0 and y != 0:
                tabuleiro[y][x] = tabuleiro[y-1][x]
                tabuleiro[y-1][x] = 0

#Ganhou o jogo se todos os blocos forem 0:
def win():
    if not winner and not loser:
        for linha in tabuleiro:
            for block in linha:
                if block != 0:
                    return False
        return True

def lose(): 
    if not winner and not loser:
        for y in range(len(tabuleiro)):
            for x in range(len(tabuleiro[0])):
                if len(player_select(y, x, [])) != 0:
                    return False
        return True
            
            
############################################################################## MAIN FUNCTIONS


##JOGO 
def main_game(n, color1, color2, color3, color4, color5):
    #Ecrã do inicio do jogo
    bg = pygame.image.load("Menu/bg1.png")
    screen.blit(bg, (0, 0))

    #Evitar spam do click do rato
    mouse_click = False

    #Pontos
    pygame.font.init()
    fonte = pygame.font.Font(pygame.font.get_default_font(), 20)
    screen.blit(fonte.render("Score: ", 1, (0,0,0)), (190, 27)) 
    pontos = 0
    #Venceu
    global winner
    global loser
    winner = False
    loser = False
    
    #Dá instrução para criar o tabuleiro de jogo global
    global tabuleiro
    tabuleiro = novo_tabuleiro(n, color1, color2, color3, color4, color5)
    
    winlose=pygame.time.get_ticks()
    #Loop do jogo
    while True:
        ##Eventos 
        #Ver se ganhou ou perdeu
        seconds=(pygame.time.get_ticks()-winlose)/1000
        if seconds >= 0.75:
            if win():
                winner = True
                bg = pygame.image.load("Menu/win.png")
                screen.blit(bg, (100, 145))
            
            if lose():
                loser = True
                bg = pygame.image.load("Menu/loser.png")
                screen.blit(bg, (100, 145))
            
        #clique do rato
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and mouse_click == False:
                start_time = pygame.time.get_ticks()
                mouse_click = True
                (j, i) = pygame.mouse.get_pos()
                y = (i-150)/30
                x = (j-105)/30
                if 0 <= (y-int(y)+0.2) <= 0.9 and 0 < (x-int(x)+0.2) < 0.9:
                    pieces = player_select(int(y), int(x), []) 
                    if len(pieces) != 0:
                        winlose = pygame.time.get_ticks()
                        pontos += (len(pieces))*(len(pieces)-1)
                        to_remove(pieces)  
                if 450 < j < 595 and 15 < i < 60:
                    main_game(n, color1, color2, color3, color4, color5)
                    break
                if 10 < j < 150 and 15 < i < 60:
                    main_menu()
                    break

            #Controlar quando o jogador pode carregar novamente
            if mouse_click == True and (pygame.time.get_ticks() - start_time >= 100):
                mouse_click = False

            #Sair do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
        
        #Atualizar o tabuleiro
        search_zero()
        eliminar_coluna()
        tabuleiro_update(color1, color2, color3, color4, color5)

        #Sistema de pontuação
        rect = pygame.draw.rect(screen, (255,201,14), [310, 23, 99, 27])
        screen.blit(fonte.render(str(pontos), 1, (0,0,0)), (350, 27))       
        
        #Atualizar o ecrã
        pygame.display.flip()


##MENU PRINCIPAL


def main_menu():
    pygame.init()
    pygame.display.set_caption('Bubblets!')

    #Cria o ecrã global do jogo
    global screen
    screen = pygame.display.set_mode((600, 600))
    bg = pygame.image.load("Menu/main_menu1.png")
    screen.blit(bg, (0, 0))
    pygame.display.update()

    #Carrega circulos
    color1 = pygame.image.load("Skins/circleblue.png")
    color2 = pygame.image.load("Skins/circlered.png")
    color3 = pygame.image.load("Skins/circlegreen.png")
    color4 = pygame.image.load("Skins/circleyellow.png")
    color5 = pygame.image.load("Skins/circlepurple.png") 

    #Eventos do ecrã inicial
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (j, i) = pygame.mouse.get_pos()
                #Botão Easy
                if 50 < j < 200 and 425 < i < 490:
                    main_game(2, color1, color2, color3, color4, color5)
                    break
                
                #Botão Medium
                if 200 < j < 400 and 425 < i < 490:
                    main_game(4, color1, color2, color3, color4, color5)
                    break
                
                #Botão Hard
                if 400 < j < 550 and 425 < i < 490:
                    main_game(5, color1, color2, color3, color4, color5)
                    break  
                
                #Escolher Circulo
                if 100 < j < 200 and 225 < i < 325:
                    color1 = pygame.image.load("Skins/circleblue.png")
                    color2 = pygame.image.load("Skins/circlered.png")
                    color3 = pygame.image.load("Skins/circlegreen.png")
                    color4 = pygame.image.load("Skins/circleyellow.png")
                    color5 = pygame.image.load("Skins/circlepurple.png")   
                    ball = pygame.image.load("Select/ball_light.png")
                    heart = pygame.image.load("Select/heart_dark.png")
                    star = pygame.image.load("Select/star_dark.png")
                    screen.blit(ball, (99, 220))
                    screen.blit(heart, (401, 219))
                    screen.blit(star, (225, 115))
                
                #Escolher Coração #Colocar para só quem já desbloqueou usar
                if 400 < j < 500 and 225 < i < 325: 
                    color1 = pygame.image.load("Skins/heartblue.png")
                    color2 = pygame.image.load("Skins/heartred.png")
                    color3 = pygame.image.load("Skins/heartgreen.png")
                    color4 = pygame.image.load("Skins/heartyellow.png")
                    color5 = pygame.image.load("Skins/heartpurple.png")
                    ball = pygame.image.load("Select/ball_dark.png")
                    heart = pygame.image.load("Select/heart_light.png")
                    star = pygame.image.load("Select/star_dark.png")
                    screen.blit(ball, (99, 220))
                    screen.blit(heart, (401, 219))
                    screen.blit(star, (225, 115))
                
                #Escolher Estrela #Colocar para só quem já desbloqueou usar
                if 225 < j < 375 and 115 < i < 270: 
                    color1 = pygame.image.load("Skins/starblue.png")
                    color2 = pygame.image.load("Skins/starred.png")
                    color3 = pygame.image.load("Skins/stargreen.png")
                    color4 = pygame.image.load("Skins/staryellow.png")
                    color5 = pygame.image.load("Skins/starpurple.png")  
                    ball = pygame.image.load("Select/ball_dark.png")
                    heart = pygame.image.load("Select/heart_dark.png")
                    star = pygame.image.load("Select/star_light.png")
                    screen.blit(ball, (99, 220))
                    screen.blit(heart, (401, 219))
                    screen.blit(star, (225, 115))

            #Sair do Jogo        
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
          
        pygame.display.flip()

#INICIADOR
if __name__ == "__main__":
    main_menu()