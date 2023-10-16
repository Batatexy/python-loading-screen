import os
#Quanto maior mais lento (Min=1 / Default=8)
speed=8
# #Pense em número kkkkkkk

while True:
    os.system('cls')
    num=str(input("Pense e escreva um número: "))
    for i in range(0,101,1):
        for j in range(0,speed,1):
            os.system('cls')
            print("Pensando... " f'{i}%')
            print('▁'*100)
            if i>=100:
                print('█'*i)
            elif i==99:
                print('█'*i,'▏')
            else:
                print('█'*i,' '*(98-i),'▏')
                
            print('▔'*100)

    print("Você pensou no número",f'{num}!')
    print("")
    pause=str(input("Pressione qualquer tecla para pensar em um novo número: "))