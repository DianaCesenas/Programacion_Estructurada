#crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los emails sin duplicados

email=[]

i="si"
while i=="si":
    #dict has no atribute add es porque no le puse comillas al set email{""} a no ser que sea lista[]
    email.append(input("nuevo email: "))

    i=str(input("desea volver a capturarlo? (si/no)"))

email_set=set(email)#quitar duplicados
email=list(email_set)
print(email)
