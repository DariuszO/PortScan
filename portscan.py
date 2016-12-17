#!/usr/bin/env python3.5
#coding: utf-8

from os import system
from sys import exit
from time import sleep
from socket import *

'''
PortScan
'''

def menu():
    system("reset")
    print("""\033[31m
 ▄▄▄·              ▄▄▄      ▄▄▄▄▄ 
▐█ ▄█    ▪         ▀▄ █·    •██   
 ██▀·     ▄█▀▄     ▐▀▀▄      ▐█.▪ 
▐█▪·•    ▐█▌.▐▌    ▐█•█▌     ▐█▌· 
.▀        ▀█▄▀▪    .▀  ▀     ▀▀▀  
                                  
.▄▄ ·      ▄▄·      ▄▄▄·      ▐ ▄ 
▐█ ▀.     ▐█ ▌▪    ▐█ ▀█     •█▌▐█
▄▀▀▀█▄    ██ ▄▄    ▄█▀▀█     ▐█▐▐▌
▐█▄▪▐█    ▐███▌    ▐█ ▪▐▌    ██▐█▌
 ▀▀▀▀     ·▀▀▀      ▀  ▀     ▀▀ █▪ \033[1;m

\033[41m========= By: Magno Tutor =========\033[1;m

""")
    

def opcoes():
    menu()
    try:
        print("\033[31mEscolha:\033[1;m \n")
        escolha = int(input("  \033[1;91m[\033[1;m\033[1;32m1\033[1;m\033[1;91m]\033[1;m Escanear Portas\n  \033[1;91m[\033[2;m\033[1;32m2\033[1;m\033[1;91m]\033[1;m Quit\n\n \033[1;91m▬▶\033[1;m "))
    except:
        print("\n\033[31mEscolha invalida\033[1;m")
        sleep(2)
        opcoes()
        
    if escolha == 1:
        escanear()
    elif escolha == 2:
        system("reset")
        exit(1)
    else:
         print("\n\033[31mEscolha invalida\033[1;m")
         sleep(2)
         opcoes()

def escanear():
    menu()
    try:
        host = input("\033[31mDigite o host:\033[1;m ")
        print("")
    except:
        escanear()
    try:       
        ip = gethostbyname(host)
        print("\033[31mEndereco IP ▬▶\033[1;m %s \n" %(ip))
    except:
        print("\033[31mHost invalido.\033[1;m")   
        sleep(3)
        escanear()
    try:
        pi = int(input("\n\033[31mPorta inicial (ex: 80):\033[1;m "))
        print("")
    except:
        print("\033[31mPorta inicial invalida.\033[1;m")
        sleep(3)
        escanear()    
    try:
        pf = int(input("\033[31mPorta final (ex: 443):\033[1;m "))
        print("\n")
    except:
        print("\033[31mPorta final invalida.\033[1;m")
        sleep(3)
        escanear()         
        
    print("\033[33mIniciando o escaneamento\033[1;m\033[32m...\033[1;m\n")  
    for i in range(pi, pf+1):
            sckt = socket(AF_INET, SOCK_STREAM)
            res = sckt.connect_ex((ip,  i))
            if (res == 0):
                print("\033[32m▬▶ Porta\033[1;m %d \033[32maberta\033[1;m" %(i))
            else:
                print("\033[31m▬▶ Porta\033[1;m %d \033[31mfechada\033[1;m" %(i))
    print("\n\033[33mEscaneamento finalizado\033[1;m\n")
    continuar = input("\n\033[31mDeseja fazer outro escaneamento (s/n):\033[1;m ")
    if continuar == "s":
        escanear()
    elif continuar == "n":
        exit(1)
#sckt.close()

opcoes() 
