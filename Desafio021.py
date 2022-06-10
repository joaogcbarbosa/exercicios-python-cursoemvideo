#Faça um programa em python que abra e reproduza um áudio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('Desafio021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
