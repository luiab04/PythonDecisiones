def main():
    # Escribe tu código abajo de esta línea
   ana = input("Tirada de Ana: a) Piedra  p) Papel  t) Tijera : ")
   juan = input("Tirada de Juan:  a) Piedra  p) Papel  t) Tijera: ")

if(len(ana) > 1) or (len(juan) > 1):
    print("Las tiradas deben ser un caracter")
elif(ana == "a" and juan == "a"):
    print("Empate")
elif(juan == "p" and ana == "a"):
    print("Gana Juan")
elif(juan == "t" and ana == "p"):
    print("Gana Juan")
elif(juan == "a" and ana == "t"):
    print("Gana Juan")
elif(ana == "p" and juan == "a"):
    print("Gana Ana")
elif(ana == "t" and juan == "p"):
    print("Gana Ana")
elif(ana == "a" and juan == "t"):
    print("Gana Ana")
else:
    print("Tirada invalida")

if __name__ == '__main__':
    main()
