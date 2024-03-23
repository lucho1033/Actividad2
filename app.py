nombres= "Luis Ernesto" # variable tipo cadena
apellidos= "Espinel Cano"# variable tipo cadena
edad = 43.5 # variable tipo float
estadoCivil = "Casado"
hijos = 2 #VAriable tipo int

print("mi nombre completo es", nombres , apellidos)
print("Tengo ", edad, "años," , "soy",estadoCivil, "y tengo",hijos,"Hijos")

# Operaciones básicas.
hija= 12
hijo = 9
sumaEdad = 12 + 9
restaEdada = 12 - 9 
promedioEdad = sumaEdad/2
print("la suma de sus edades es:", sumaEdad)
print("la resta de sus edades es:", restaEdada)
print("El promedio de sus edades es de: ", promedioEdad)

# Uso de condicionales if, elif y else 

edad1 =int(input("Favor ingrese su edad")) 
if edad1 < 18 and edad1>15:
    print("Eres menor de edad y no puedes ingresar al sitio")
elif edad1 > 1 and edad1 < 15:
    print("Eres un bebé vete a dormir")    
else:
    print("Bienvenido")    
