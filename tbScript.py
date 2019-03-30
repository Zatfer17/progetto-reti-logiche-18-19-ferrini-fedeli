from random import *
from math import *

def genera_centroide(int):
    centroide = []
    for i in range(0,int):
        centroide.append(randint(0,1))
    return centroide

def decimale(array):
    a = 0
    for i in range(0,8):
        a = a + array[i]*pow(2,i)
    return a


print("ALTERNATIVE:\n"
      "  A. Tutto casuale\n"
      "  B. Maschera di soli 0\n"
      "  C. Maschera di soli 1\n"
      "  D. Maschera di soli 1 e centroidi uguali\n"
      "  E. Distanza minima\n"
      "  F. Distanza massima")
selection = input("Scegli alternativa: ")

if selection == 'A' or selection == 'a':
    ingresso = []
    for i in range(0, 20):
        ingresso.append(int(decimale(genera_centroide(8))))
elif selection == 'B' or selection == 'b':
    ingresso = []
    ingresso.append(0)
    for i in range(1, 20):
        ingresso.append(int(decimale(genera_centroide(8))))
elif selection == 'C' or selection == 'c':
    ingresso = []
    ingresso.append(255)
    for i in range(1, 20):
        ingresso.append(int(decimale(genera_centroide(8))))

elif selection == 'D' or selection == 'd':
    ingresso = []
    ingresso.append(255)
    a = int(decimale(genera_centroide(8)))
    for i in range(1, 17):
        ingresso.append(a)
    ingresso.append(int(decimale(genera_centroide(8))))
    ingresso.append(int(decimale(genera_centroide(8))))

elif selection == 'E' or selection == 'e':
    ingresso = []
    ingresso.append(255)
    targetX = int(decimale(genera_centroide(8)))
    targetY = int(decimale(genera_centroide(8)))
    ingresso.append(targetX)
    ingresso.append(targetY)
    for i in range(3, 17):
        ingresso.append(int(decimale(genera_centroide(8))))
    ingresso.append(targetX)
    ingresso.append(targetY)

elif selection == 'F' or selection == 'f':
    ingresso = []
    ingresso.append(255)
    for i in range(1, 17):
        ingresso.append(255)
    ingresso.append(0)
    ingresso.append(0)

print("\nDA SOSTITUIRE A RIGA 23 DEL TEST BENCH:")
print("signal RAM: ram_type := (0 => std_logic_vector(to_unsigned( " + str(ingresso[0]) + " , 8)),\n"
       "                         1 => std_logic_vector(to_unsigned( " + str(ingresso[1]) + " , 8)),\n"
       "                         2 => std_logic_vector(to_unsigned( " + str(ingresso[2]) + " , 8)),\n"
       "                         3 => std_logic_vector(to_unsigned( " + str(ingresso[3]) + " , 8)),\n"
       "                         4 => std_logic_vector(to_unsigned( " + str(ingresso[4]) + " , 8)),\n"
       "                         5 => std_logic_vector(to_unsigned( " + str(ingresso[5]) + " , 8)),\n"
       "                         6 => std_logic_vector(to_unsigned( " + str(ingresso[6]) + " , 8)),\n"
       "                         7 => std_logic_vector(to_unsigned( " + str(ingresso[7]) + " , 8)),\n"
       "                         8 => std_logic_vector(to_unsigned( " + str(ingresso[8]) + " , 8)),\n"
       "                         9 => std_logic_vector(to_unsigned( " + str(ingresso[9]) + " , 8)),\n"
       "                         10 => std_logic_vector(to_unsigned( " + str(ingresso[10]) + " , 8)),\n"
       "                         11 => std_logic_vector(to_unsigned( " + str(ingresso[11]) + " , 8)),\n"
       "                         12 => std_logic_vector(to_unsigned( " + str(ingresso[12]) + " , 8)),\n"
       "                         13 => std_logic_vector(to_unsigned( " + str(ingresso[13]) + " , 8)),\n"
       "                         14 => std_logic_vector(to_unsigned( " + str(ingresso[14]) + " , 8)),\n"
       "                         15 => std_logic_vector(to_unsigned( " + str(ingresso[15]) + " , 8)),\n"
       "                         16 => std_logic_vector(to_unsigned( " + str(ingresso[16]) + " , 8)),\n"
       "                         17 => std_logic_vector(to_unsigned( " + str(ingresso[17]) + " , 8)),\n"
       "                         18 => std_logic_vector(to_unsigned( " + str(ingresso[18]) + " , 8)),\n"
       "others => (others =>'0'));")
distanze = []
#print (ingresso)
mask = bin(ingresso[0])[2:]
#print(str(mask))
if len(mask)<8:
    a='0';
    while len(mask)<8:
        mask=a+mask
#print(str(mask))
for i in range(0,8):
    if str(mask)[i]=='1':
        x = fabs(ingresso[2*i+1]-ingresso[17])
        y = fabs(ingresso[2*i+2]-ingresso[18])
        distanze.append(x+y)
    else:
        distanze.append(512)
#print(distanze)
min = min(distanze)
output = []
for i in range(0,8):
    if distanze[i]==min and distanze[i]!=512 :
        output.append(1)
    else :
        output.append(0)
#print(output)
#print(output[::-1])
print("\nDA SOSTITUIRE A RIGA 111 DEL TEST BENCH:")
print("assert RAM(19) = std_logic_vector(to_unsigned( "+ str(int(decimale(output))) + ", 8)) report \"test fallito\" severity failure;")

input()

