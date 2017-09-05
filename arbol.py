class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

class Pila:
    def __init__(self):
        self.pila=[]        
    def apilar(self,x):
      # funcion para agregar un elemento a la pila
        self.pila.append(x)
    
    def desapilar(self):
      # funcion para eliminar un elemento de la pila
       if (self.pila != []):
  
        return self.pila.pop()
       else: 
        return "Lista vacia"
    

def evaluar(arbol):
    try:
      if(arbol.valor == '+'):
         return (evaluar(arbol.izq) + evaluar(arbol.der))
      if(arbol.valor == '-'):
         return (evaluar(arbol.izq) - evaluar(arbol.der))
      if(arbol.valor == '*'):
         return (evaluar(arbol.izq) * evaluar(arbol.der))
      if(arbol.valor == '/'):
         return (evaluar(arbol.izq) / evaluar(arbol.der))
      if(arbol.valor.isdigit()):
          return int(arbol.valor)
      else:
          return (buscarDic(lista[i],diccionario))
    except AttributeError:
      return int(arbol)

def agregarDic(letra,valor,dic):    
    tam = 0
    if(len(dic) == 0):
        dic[tam,0] = letra
        dic[tam,1] = valor        
    else:
        
        while(tam < (len(dic)/2) and letra != dic[tam,0]):
            tam = tam + 1
        dic[tam,0] = letra
        dic[tam,1] = valor
        
    
            

def buscarDic(letra,dic):    
    if(len(dic) == 0):
        print("El arreglo no tiene elementos")
    else:
        tam = 0
        while(tam < (len(dic)/2)):
            if(letra == dic[tam,0]):
                return dic[tam,1]
            tam = tam + 1
        print("La variable no esta definida")
        return false
    
                
       
cadena = input("Ingrese una cadena, Termine con el numero 0:")
ecuacion=[]

while(cadena != '0'):
    ecuacion.append(cadena)
    cadena = input("Ingrese una cadena, Termine con el numero 0:")    
    
pila= Pila()    
veces= 0
diccionario={}

while(veces < len(ecuacion)):    
    lista = ecuacion[veces].split(" ")    
    tam = len(lista)
    i = 0    
    while(i < tam):
        
        if(lista[i] in "+ - * /"):
           der = pila.desapilar()
           izq = pila.desapilar()
           nodo = Nodo(lista[i],izq,der) 
           pila.apilar(nodo)#Ingreso del sub arbol con los dos simbolos
        else:
            if(lista[i].isdigit()):                
                pila.apilar(lista[i])
            else:                
                if(lista[i] == "="):                    
                    agregarDic(lista[i+1],evaluar(pila.desapilar()),diccionario)                    
                    i = i+1                    
                else:                    
                    pila.apilar(buscarDic(lista[i],diccionario))
                    
        i = i+1
        
    veces = veces +1
    
print ("el resultado al evaluar el arbol es: " + str(evaluar(pila.desapilar())))
