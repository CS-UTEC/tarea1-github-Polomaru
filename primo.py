def primo(number):
    if (number<0):
        return ("No es natural, por lo tanto no es primo")
    if (number < 2):   
        return ("No es primo")
    if (number==2):
        return ("Es primo")
    for x in range(2, number):
        if (number % x== 0):
            return ("No es primo")
        return ("Es primo")  
mi_numero=int(input("Ingrese un numero: "))
print(primo(mi_numero))
