#Operaciones que puede realizar la calculadora


def sumar (a, b): #Suma dos valores
    return a + b

def restar (a, b): #Resta dos valores
    return a - b

def multiplicar (a, b): #Multiplica dos valores
    return a * b

def dividir (a, b): #Dividide dos valores 
    return a / b
try: #Devuelve el mensaje de "Error" si es división por 0 
    a = 1 / 0
except Exception as e:
    print(f"error: {str(e)}")
    
# Función principal
def main():
    print("Seleccione operación")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    while True:
        opcion = input("Elija el numero de la operacion (1/2/3/4) o 'salir' para terminar: ")
        if opcion =='salir':
            break
        if opcion in ['1','2','3','4']:
         num1 = float (input("Ingrese el primer número: "))
         num2 = float (input("Ingrese el segundo número: "))
        if opcion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif opcion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif opcion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Opción no válida. Vuelva a intentar.") 

    #Ejecuta la función principal.
    if __name__ == "__main__":
        main()
    
        