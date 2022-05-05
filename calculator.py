#Hello this is my first python program, I hope you like it
def suma(valor1,valor2):
    return valor1+valor2
def resta(valor1,valor2):
    return valor1-valor2
def mult(valor1,valor2):
    return valor1*valor2
def div(valor1,valor2):
    return valor1/valor2
def expo(valor1,valor2):
    return valor1**valor2
def modulo(valor1,valor2):
    return valor1%valor2

def main():
    while True:
        print("Bienvenido\n")
        print("1.- Suma dos numeros") 
        print("2.- Resta dos numeros") 
        print("3.- Multiplica dos numeros") 
        print("4.- Divide dos numeros") 
        print("5.- Exponente de dos numeros")
        print("6.- Modulo de dos numeros")
        print("7.- Salir") 
        
        opcion = int(input("Opcion: "))

        if opcion == 1:
            num1 = int(input("Ingrese el primer valor: "))
            num2 = int(input("Ingrese el segundo valor: "))
            print("La suma de los dos valores es: ", suma(num1,num2))
        elif opcion == 2:
            num1 = int(input("Ingrese el primer valor: "))
            num2 = int(input("Ingrese el segundo valor: "))
            print("La resta de los dos valores es: ", resta(num1,num2))
        elif opcion == 3:
            num1 = int(input("Ingrese el primer valor: "))
            num2 = int(input("Ingrese el segundo valor: "))
            print("La multiplicacion de los dos valores es: ", mult(num1,num2))
        elif opcion == 4:
            num1 = int(input("Ingrese el primer valor: "))
            num2 = int(input("Ingrese el segundo valor: "))
            print("La division de los dos valores es: ", div(num1,num2))
        elif opcion == 5:
            num1 = int(input("Ingrese el primer valor: "))
            num2 = int(input("Ingrese el segundo valor: "))
            print("La exponenciacion de los dos valores es: ", expo(num1,num2))
        elif opcion == 6:
            num1 = int(input("Ingrese el primer valor: "))
            num2 = int(input("Ingrese el segundo valor: "))
            print("El modulo de los dos valores es: ", modulo(num1,num2))
        elif opcion == 7:
            exit()
        else:
            print("Opcion invalida\n")

if __name__ == "__main__": 
    main() 