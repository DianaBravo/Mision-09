#Autor Diana Marisol Medina Bravo

def extraerPares(lista):
    nuevaLista = []
    for dato in lista:
        if dato % 2 == 0:
            nuevaLista.append(dato)

    return nuevaLista

def extraerMayoresPrevio(lista):
        nuevaLista = []

        n = 1
        for dato in lista:
            if dato > n:
                n = dato
                nuevaLista.append(dato)
            else:
                n = dato
        if len(nuevaLista) == 1:
            nuevaLista = []

        return nuevaLista

def intercambiarParejas(lista):
    nuevaLista = []
    i=1
    p=0
    for x in range(0,len(lista)//2):
        nuevaLista.append((lista[i]))
        nuevaLista.append((lista[p]))
        if i< len(lista) or p<len(lista):
            i+=2
            p+=2
    if len(lista)%2 !=0:
        nuevaLista.append(lista[-1])

    return nuevaLista


def intercambiarMM(lista):
    if len(lista)==0:
        pass
    else:
        mayor = max(lista)
        menor = min(lista)
        a = lista.index(mayor)
        b = lista.index(menor)

        lista[a] = menor
        lista[b] = mayor

    return lista

def promediarCentro(lista):
    mayor=max(lista)
    menor=min(lista)
    contador=0

    lista1=lista
    lista1.remove(mayor)
    lista1.remove(menor)

    for dato in lista1:
        contador+=1
    if contador<1:
        resultado=0
    else:
        suma=sum(lista1)
        resultado= suma//(contador)

    return resultado

def calcularEstadistica(lista):
    n=len(lista)
    suma=sum(lista)

    if n==0:
        return(0,0)
    else:
        mean = float(suma / n)
        numero = 0
        for dato in lista:
            a=(dato-mean)**2
            suma2=a+numero
            numero = suma2
        division=suma2/(n-1)
        deviation=float((division)**0.5)
        return (mean, deviation)


def calcularSuma(lista):
    for n in range(len(lista)):
        if lista[n] == 13:
            a = lista.index(n)
            b = a + 1
            c = a - 1
            lista.remove(b)
            lista.remove(c)
            lista.remove(n)
        else:
            pass
    suma=sum(lista)

    return suma

def main():
    # Pruebas problema 1
    print("Ejercicio 1")
    listaNumeros1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    problema1 = extraerPares(listaNumeros1)
    print("La lista", listaNumeros1, "regresa pares", problema1)
    listaNumeros1 = [5, 7, 3]
    problema1 = extraerPares(listaNumeros1)
    print("La lista", listaNumeros1, "regresa pares", problema1)

    print("")

    # Pruebas problema 2
    print("Ejercicio 2")
    listaNumeros = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    problema2 = extraerMayoresPrevio(listaNumeros)
    print("Lista original es", listaNumeros,"regresa",problema2)
    listaNumeross = [5, 4, 3, 2]
    problema2 = extraerMayoresPrevio(listaNumeross)
    print("Lista original es", listaNumeross,"regresa",problema2)



    print("")

    # Pruebas problema 3
    print("Ejercicio 3")
    listaNumeros2 =[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    problema3 = intercambiarParejas(listaNumeros2)
    print("Recibe lista", listaNumeros2, "y regresa", problema3)
    listaNumeros2 = [1,2,3]
    problema3 = intercambiarParejas(listaNumeros2)
    print("Recibe lista", listaNumeros2, "y regresa", problema3)
    listaNumeros2 = [6, 12, 4, 56]
    problema3 = intercambiarParejas(listaNumeros2)
    print("Recibe lista", listaNumeros2, "y regresa", problema3)

    print("")

    # Pruebas problema 4
    print("Ejercicio 4")
    listaNumeros3= [5,9,3,22,19,31,10,7]
    print("Lista original es", listaNumeros3)
    problema4 = intercambiarMM(listaNumeros3)
    print("Regresa",problema4)
    listaNumeros4 =  [1,2,3]
    print("Lista original es",listaNumeros4)
    problema4 = intercambiarMM(listaNumeros4)
    print("Regresa",problema4)
    listaNumeros4 = []
    problema4 = intercambiarMM(listaNumeros4)
    print("Lista original es",listaNumeros4,"regresa",problema4)

    print("")

    # Pruebas problema 5
    print("Ejercicio 5")
    listaNumeros3 =  [70, 80, 90]
    problema5 = promediarCentro(listaNumeros3)
    print("Lista", listaNumeros3, "regresa", problema5)
    listaNumeros3 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    problema5 = promediarCentro(listaNumeros3)
    print("Lista", listaNumeros3, "regresa", problema5)

    print("")

    # Pruebas problema 6
    listaNumeros6=[1,2,3,4,5,6]
    print("Ejercicio 6")
    print("Lista original es", listaNumeros6)
    problema6 = calcularEstadistica(listaNumeros6)
    print("Regresa", problema6)
    listaNumeros4 =  [95,21,73,24,15,69,71,80,49,100,85]
    print("La lista original es:", listaNumeros4)
    problema6 = calcularEstadistica(listaNumeros4)
    print("Regresa", problema6)
    lista=[]
    print("La lista original es:", lista)
    a=calcularEstadistica(lista)
    print("Regresa",a)

    print("")

    # Pruebas problema 7
    print("Ejercicio 7")
    listaNumeros4 = [5, 2, 13, 4, 1, 6, 1, 8, 4, 1, 5],
    problema6 = calcularSuma(listaNumeros4)
    print("La lista original es:", listaNumeros4,"regresa", problema6)


    lista7 = [1, 2, 3, 4, 5, 6],
    print("Lista original es", lista7)
    problema6 = calcularSuma(lista7)
    print("Regresa", problema6)

main()