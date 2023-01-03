import pygame
from pygame.locals import *
import os
import sys


pygame.init()

tela = pygame.display.set_mode()

lista_de_pixel = []
def MostarUmTexto(texto):
	texto = str(texto)
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	fontesys = pygame.font.SysFont(fonte, 60)
	texto = fontesys.render(texto, 1, (255, 90, 245))
	return texto
	
	
def Pixel(display, pos):
	preto = (0, 0, 0)
	global lista_de_pixel
	
	for i in range(1, 5):
		status = False
		test =[display, preto, (pos[0], pos[1]), 10+i, 40+i]
		lista_de_pixel.append(test)

cont_limpa = 0
break_soma = 5
status = False
while 1:
	tela.fill((255, 255, 255))
	
	for ev in  pygame.event.get():
		if ev.type == exit:
			exit()
		elif ev.type == MOUSEMOTION:
					break_soma = break_soma  if break_soma == 50000 else 50000
					Pixel(tela, pygame.mouse.get_pos())
		elif ev.type == MOUSEBUTTONDOWN and cont_limpa >= 5000:
			lista_de_pixel = []
			cont_limpa = 0
		    
	if break_soma < 10:
		status = False
		break_soma = 0
	else:
		status = True
		break_soma -= 20
	if status == False:
		cont_limpa += 1
		if cont_limpa >= 500:
			lista_de_pixel = []
			
	for pixel in lista_de_pixel:
		pygame.draw.circle(pixel[0], pixel[1], pixel[2], pixel[3], pixel[4])
	tela.blit(MostarUmTexto('Imagem vai ser apagada: '  + str(break_soma)), (0, 50))
	pygame.display.flip()