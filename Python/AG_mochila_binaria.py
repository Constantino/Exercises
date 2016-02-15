"""
   Programacion de Sistemas Adaptativos
   Unidad 1: Algoritmos adaptativos
   Autora principal: Dra. Sara E. Garza
   Adaptaciones por Constantino Mora
   Descripcion: Algoritmo genetico simple para resolver una instancia del problema de la mochila binaria
"""

import random
import math
from sys import argv#para recibir argumentos desde linea de comandos

class AGMochila:
    #Constructor
    def __init__(self, co, g, p, c, debug):
        self.debug = debug
        self.cant_obj=co
        self.ganancias=g
        self.pesos=p
        self.mejor_aptitud=-1
        self.ruleta=[]
        self.nueva_generacion=[] #Sucesores de la generacion actual 
        self.capacidad=c
        self.tam_generacion=0
        self.generacion=[] #Lista con individuos (cromosomas de la generacion)
        self.prob_mutacion=0 #Probabilidad de mutacion
        self.aptitud_total=0.0
        self.aptitudes={} #Diccionario con forma (cromosoma, aptitud)
        self.mejor_individuo='' #cromosoma
        self.mejor_aptitud=-1
        self.ruleta=[]
        self.nueva_generacion=[] #Sucesores de la generacion actual


    """ Para generar la poblacion inicial, necesitamos modelar el problema con vectores de caracteristicas.
        Vamos a representar cada combinacion de objetos como una cadena binaria de 5 bits.
        Para ello, vamos a escoger numeros aleatorios entre 0 y 2^cantidad de objetos-1 y los vamos a convertir a su valor en binario.
    """
    def generar_poblacion_inicial(self):
        poblacion=random.sample(xrange(0,pow(2,self.cant_obj)-1),self.tam_generacion) #Obtiene una muestra de numeros aleatorios en un cierto rango
        if self.debug:
            print 'POBLACION INICIAL: '
            print '--------------------'
        for individuo in poblacion:
            cromosoma=bin(individuo)[2:] #Para quitar el 0b del string
            cromosoma=cromosoma.zfill(self.cant_obj) #Rellena con ceros el string para que quede de un cierto largo (asi todos quedan iguales)
            self.generacion.append(cromosoma)
            if self.debug:
                print individuo,' ',cromosoma
            
    """Para evaluar, obtenemos el producto punto entre cada cromosoma y el vector de ganancias. Esta sera la aptitud del individuo (cromosoma).
       Tambien calculamos el producto punto entre el cromosoma y el vector de pesos.
       Si el peso es mayor a la capacidad de la mochila, la aptitud se vuelve cero (la combinacion no es factible).
       Vamos a registrar la aptitud total de la generacion y tambien vamos a guardar al mejor individuo y la mejor aptitud de todas las generaciones.
    """
    
    def evaluar(self):
        if self.debug:
            print '[EVALUACION]'
        self.aptitud_total=0
        self.aptitudes={}
        for cromosoma in self.generacion:
            aptitud=0.0
            peso=0.0
            for i in range(0,self.cant_obj):
                #Limpiar aptitud total
                aptitud+=int(cromosoma[i])*self.ganancias[i] #Nota que cromosoma[i] es un gen
                peso+=int(cromosoma[i])*self.pesos[i]
            if peso > self.capacidad:
                aptitud=0.0
            self.aptitudes[cromosoma]=aptitud
            self.aptitud_total+=aptitud
            if aptitud > self.mejor_aptitud:
                self.mejor_individuo=cromosoma
                self.mejor_aptitud=aptitud
            if self.debug:
                print cromosoma,' ',aptitud,' ',peso
        if self.debug:
            print '--------------------------'

            print "Aptitud total: " + str(self.aptitud_total)

        

    """Para la seleccion, utilizaremos la rueda de ruleta. Crearemos la ruleta de la siguiente manera:
       Calculamos el porcentaje de la aptitud total que pertenece al cromosoma; esta sera
       la cantidad de "copias" del individuo que se meteran en la ruleta.
       Al final, revolvemos la ruleta para que quede mejor distribuida.
    """
    def seleccionar(self):
        if self.debug:
            print '[SELECCION]'
        for cromosoma in self.aptitudes:

            if self.aptitudes[cromosoma] == 0: #Si la aptitud es cero que por lo menos obtenga un espacio
                cacho = 1
            else:                              #Si no, entonces calculamos su porcentaje
                cacho=int(math.ceil(self.aptitudes[cromosoma]/self.aptitud_total*100))

            if self.debug:
                print 'Al cromosoma ',cromosoma,' le corresponden ',cacho,' espacios.'
            for i in range(0,cacho):
                self.ruleta.append(cromosoma)
            random.shuffle(self.ruleta) #chaca chaca

    """ Para hacer el cruce, primero escogemos un punto al azar (podria ser tambien fijo).
        Una vez teniendo el punto, seleccionamos aleatoriamente a dos individuos de la ruleta,
        los cuales formaran una pareja. De esta pareja, saldran dos "hijos":
        uno con la cabeza de la mama (i.e. con los genes hasta antes del puntos de cruce)
        y el cuerpo del papa (i.e. los genes a partir del punto de cruce),
        y otro con la cabeza del papa y el cuerpo de la mama.
    """
    def cruzar(self):
        if self.debug:
            print '[CRUCE]'
        punto_cruce=random.randint(1,self.cant_obj-2)
        bebes=[]
        if self.debug:
            print 'El punto de cruce escogido es ',punto_cruce
        for  i in range(len(self.generacion)):
            papa=random.choice(self.ruleta) #Este metodo obtiene de manera aleatoria un elemento de una lista.
            mama=random.choice(self.ruleta)
            hijo1=papa[:punto_cruce] + mama[punto_cruce:] #Simplemente hacemos un "slicing" de las cadenas.
            hijo2=mama[:punto_cruce] + papa[punto_cruce:]
            bebes.append(hijo1) #Guardamos a los hijos en un arreglo auxiliar.
            bebes.append(hijo2)
            #print len(bebes)
            if self.debug:
                print 'Papas',papa,' ',mama,' generan hijos ',hijo1,' y ',hijo2
        self.nueva_generacion=random.sample(bebes,len(self.generacion)) #Como los bebes son el doble del tamanio de la generacion, escogemos solo la mitad.
        if self.debug:
            print 
            print 'Nueva generacion: '
            for individuo in self.nueva_generacion:
                print individuo

    """ Para hacer la mutacion, recorremos cada cromosoma gen por gen. En cada iteracion,
        lanzamos un numero aleatorio; si cae dentro del rango de la probabilidad de mutacion,
       cambiamos el gen por su contrario: es decir, si es 1 lo cambiamos por 0 y viceversa.
       Al final, hacemos la nueva generacion ya con los individuos mutados.
   """
    def mutar(self):
        if self.debug:
            print '[MUTACION]'
        poblacion=[]
        for cromosoma in self.nueva_generacion:
            crom_mutado=''
            for gen in cromosoma:
                r=random.random()
                if(r<=self.prob_mutacion):
                    crom_mutado+=str(abs(int(gen)-1))
                    if self.debug:
                        print 'Mutando el gen del cromosoma',cromosoma
                else:
                    crom_mutado+=gen
            poblacion.append(crom_mutado)
        self.nueva_generacion=poblacion #reescribimos la lista con los cromosomas mutados
        if self.debug:
            print
            print 'Nueva generacion mutada (X-boys): '
            for individuo in self.nueva_generacion:
                print individuo

    #Aqui simplemente hacemos que la generacion recien creada sea ahora la actual.
    def hacer_cambio_generacional(self):
        self.generacion=self.nueva_generacion

    #Metodo get para el mejor individuo
    def get_mejor_individuo(self):
        return self.mejor_individuo

    #Metodo get para la mejor aptitud
    def get_mejor_aptitud(self):
        return self.mejor_aptitud

    def aplicar_configuracion(self):
        self.prob_mutacion = random.randint(1,5)/10.0
        self.tam_generacion = random.randint(3,cantidadObjetos-cantidadObjetos/2) #tam de la generacion
        
#FIN DE LA CLASE


#Instancia del problema de la mochila
cantidadObjetos = int(argv[1]) #primer argumento desde linea de comandos
capacidadMochila = int(argv[2]) #segundo argumento desde linea de comandos
debug = int(argv[3]) #Es para activar o desactivar impresiones de los metodos para depuracion
ganancias=[]
pesos=[]

for i in range(cantidadObjetos): #Generar instancia aleatoria
    ganancias.append(random.randint(1,100))
    pesos.append(random.randint(1,100))

print "Cantidad de objetos: ",cantidadObjetos
print "Capacidad de la mochila: ",capacidadMochila
print "Ganancias: ",ganancias
print "pesos: ",pesos

#Cantidad de iteraciones
iteraciones = 4
#Cantidad de generaciones
generaciones=10


#Creamos el objeto para trabajar
ag=AGMochila(cantidadObjetos, ganancias, pesos, capacidadMochila, debug)

ganadores = {}
optimo = 0
mejorapt = 0

mejoresIteracion = {}

for i in xrange(0,iteraciones):
    ganador_iter = {}
    
    ag.aplicar_configuracion()
    print "Iteracion: ",i+1
    print "\tTam. de generacion: ",ag.tam_generacion,"\tProba. Mutacion: ",ag.prob_mutacion,"\n"
    
    #Generamos la poblacion inicial
    ag.generar_poblacion_inicial()
    #Hacemos el ciclo convencional de los AG's
    for g in xrange(0,generaciones):
        ag.evaluar()
        ag.seleccionar()
        ag.cruzar()
        ag.mutar()
        ag.hacer_cambio_generacional()
        individuo = ag.get_mejor_individuo() #Guardamos al mejor individuo hasta el momento
        mejoresIteracion[individuo] = ag.get_mejor_aptitud()#lo anexamos con su aptitud
    ag.evaluar()
    
    print "\tMejores de iteracion ",i+1," \n\t\t",mejoresIteracion,"\n"

    individuo = ag.get_mejor_individuo()#Obtiene al mejor de la iteracion
    ganador_iter[individuo] = ag.get_mejor_aptitud()
    if ganador_iter[individuo] > mejorapt:
        optimo = individuo
        mejorapt = ganador_iter[individuo]
    ganadores[i] = ganador_iter
 
print "Ganadores de cada iteracion: \n\t",ganadores
print "Ganador final: "
print "\tIndividuo OPTIMO: ",optimo," con aptitud de: ",mejorapt


