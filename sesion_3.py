# tipos de datos primitivos

# edad = 18 # int
# altura = 1.80 # float
# nombre = "santiago" # string  # string significa cadena "" por ser con comillas cadena de caracteres 
# es mayor = true #booleano True False

# es una expresion que califica el estado de una preposicion y ejecuta una rama del codigo dependiendo del estado booleano de esa proposicion.

# clasificar el estado de un pedido segun su codigo:
# 1: "recibido"
# 2: "preparado"
# 3: "despachado"
# otro: "desconocido"

# if condicion:
    # ejecuta el codigo que pongamos aca
# else:
    # lo que pasa si es falso

# if condicion_matizada:
    #ejecuta si es verdadero
# elif codicion_2:
    #ejecuta si esta condicion es verdadera
# else:
    #ejecuta ninguna condicion se cumple

# definir como le fue a un alumno segun sus notas

# nota = float(input("Hey, como te fue en el examen de ese cucho...: "))
# if nota >= 4.0:
    # print("le gane a ese viejo")
# else:
    # print("me tire la nota.")

n = float(input("ingrese una nota para dictaminar el rango: "))

if n < 0 or n > 5:
    print("dato invalido")
else:
    if n >= 4.6:
        print("sobresaliente")
    else:
        if n >= 4:
            print("Alto")
        elif n >= 3:
            print("Basico")
        else:
            print("Bajo") 










