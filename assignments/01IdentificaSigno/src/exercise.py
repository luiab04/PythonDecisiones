import math
def main():
    #escribe tu código abajo de esta línea
    numero = int(input('Dame un número: '))
def identificador(numero):
    if numero == 0:
        return 'Es cero'
    if numero < 0:
        return 'Es negativo'
    if numero > 0:
        return 'Es positivo'

mensaje = identificador(numero)
print(mensaje)

if __name__ == '__main__':
    main()
