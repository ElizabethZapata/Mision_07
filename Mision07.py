#Autor: Elizabeth Citlalli Zapata Cortes
# Mision 7

def dividir(dividendo, divisor):

    cociente= 0     #contador número de veces que se pudo restar
    numeroInicial= dividendo

    while dividendo >= divisor:
        dividendo= dividendo - divisor
        cociente += 1

    return numeroInicial,  divisor, cociente, dividendo


def encontrarMayor(valor):
    numeroMayor= 0  #Acumulador

    while valor != -1 :
        if valor >= numeroMayor:
            numeroMayor = valor
        elif valor < numeroMayor:
            numeroMayor = numeroMayor
        valor = int(input("Teclea un número [-1 para salir]: "))
    return  numeroMayor


def main():
    print("Mision 07. Ciclos while.")
    print("Autor: Elizabeth Citlalli Zapata Cortes")
    print("Matrícula: A01746002")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")

    opcion= int(input("Teclea tu opcion: "))

    while opcion != 3:
        if opcion == 1:
            print("Calculando divisiones")
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            numeroInicial,divisor,cociente,dividendo= dividir(dividendo, divisor)
            print(numeroInicial,"/",divisor,"=", cociente,", sobra", dividendo)

        elif opcion ==2:
            print("Teclea una serie de números para encontrar el mayor.")
            valor = int(input("Teclea un número [-1 para salir]: "))
            if valor == -1:
                print("No hay valor")
            else:
                numeroMayor= encontrarMayor(valor)
                print("El mayor es: ", numeroMayor)

        elif opcion > 3:
            print("ERROR, teclea 1, 2 o 3")
        print()
        print("Mision 07. Ciclos while.")
        print("Autor: Elizabeth Citlalli Zapata Cortes")
        print("Matrícula: A01746002")
        print("1. Calcular divisiones")
        print("2. Encontrar el mayor")
        print("3. Salir")

        opcion = int(input("Teclea tu opcion: "))
    print("Gracias por usar este programa, regresa pronto.")




main ()