#ALGORITMO PARA CALCULAR EL FACTORIAL DE UN NUMERO POR RECULCION
#5!=  5*4!
#10! = 10 *9!
#9! = 9 * 8!
#....
#2!= 2*1!
# 1! = 1*0= 1


def factorial(x):
    if x ==0:
         return 1
    else:
        return  x*factorial(x-1)



print(factorial(9))
