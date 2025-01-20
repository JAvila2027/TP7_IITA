""" Trabajo Practico N° 7
Nombre y Apellido: Joaquin Avila
Comisión: Jueves - virtual
tips:
- para comentar codigo se usa # o comillas triples 
- si se usa vscode, se puede usar el comando ctrl+k, ctrl+c
"""
"""
1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo.
"""
# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base=base
#         self.altura=altura
#     def area(self):
#         return self.base * self.altura

# mi_rectangulo=Rectangulo(5,14)
# area=mi_rectangulo.area()
# print(F"El area del rectangulo es: {area}")

"""
2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

"""
# class Mate:
#     def __init__(self,restantes_cebadas,estado,cants_cebadas):
#         self.restantes_cebadas=restantes_cebadas
#         self.estado=estado
#         self.cants_cebadas=cants_cebadas

#     def cebar(self):
#         if self.estado=="lleno":
#             print("¡Cuidado! ¡Te quemaste!")
#         else:
#             self.estado= ("lleno")
#     def beber(self):
#         if self.estado=="vacio":
#             print("EL mate esta vacio")
#         else:
#             self.estado ="vacio"
#             if self.restantes_cebadas>0:
#                 self.restantes_cebadas-=1
#             if self.restantes_cebadas==0:
#                 print("Advertencia: el mate está lavado.")
#     def mostrar_estado(self):
#         print(F"Estado: {self.estado}, cebadas restantes: {self.restantes_cebadas}/{self.cants_cebadas}")

# mi_mate=Mate(3,"vacio",3)
# mi_mate.mostrar_estado()
# mi_mate.beber()
# mi_mate.cebar()
# mi_mate.mostrar_estado()
# mi_mate.beber()
# mi_mate.mostrar_estado()
# mi_mate.cebar() 
# mi_mate.beber() 
# mi_mate.cebar() 
# mi_mate.beber()
# mi_mate.cebar() 
# mi_mate.beber()
# mi_mate.mostrar_estado()
"""
3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho.

"""
# class Corcho:
#     def __init__(self,bodega):
#         self.bodega=bodega
# class Botella:
#     def __init__(self,corcho=None):
#         self.corcho=corcho
# class Sacacorchos:
#     def __init__(self):
#         self.corcho=None
#     def destapar(self,botella):
#         if botella.corcho ==None:
#             print("LA botella ya esta destapada")
#         elif self.corcho !=None:
#             print("El sacacorchos ya contiene un corcho")
#         else:
#             self.corcho=botella.corcho
#             botella.corcho=None
#             print("La botella ha sido destapada")
#     def limpiar(self):
#         if self.corcho == None:
#             print("No hay un corcho en el sacacorchos")
#         else:
#             self.corcho=None
#             print("El sacacorchos esta limpio")
#     def mostrar_estado(self,botella):
#         if botella.corcho == None:
#             print("NO hay un corcho en la botella")
#         else:
#             print(f"Corcho en la botella: {botella.corcho.bodega}")
#         if self.corcho == None:
#             print("No hay corchos en el sacacorchos")
#         else:
#             print(f"Hay un corcho en el sacacorchos: {self.corcho.bodega}")

# corcho=Corcho("Bodega 1")
# botella=Botella(corcho)
# sacacorchos=Sacacorchos()
# sacacorchos.mostrar_estado(botella)
# sacacorchos.destapar(botella)
# sacacorchos.mostrar_estado(botella)
# sacacorchos.limpiar()
# sacacorchos.mostrar_estado(botella)
"""
4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. 
"""

# class Restaurante:
#     def __init__(self,restaurante_nombre,tipo_comida):
#         self.restaurante_nombre=restaurante_nombre
#         self.tipo_comida=tipo_comida
#     def describir_restaurante(self):
#         print(f"Nombre de la heladeria es:{self.restaurante_nombre}")
#         print(F"EN la heladeria vendemos :{self.tipo_comida}")
#     def abrir_restaurante(self):
#         print(F"LA Heladeria {self.restaurante_nombre} esta abierta!!!")
# class Heladeria(Restaurante):
#     def __init__(self,restaurante_nombre,tipo_comida,sabores):
#         self.restaurante_nombre=restaurante_nombre
#         self.tipo_comida=tipo_comida
#         self.sabores=sabores
#     def los_sabores(self):
#         print("Sabores disponibles: ")
#         for sabor in self.sabores:
#             print(f"-{sabor}")
# mi_heladeria=Heladeria("Heladerias de fulano","Helados",["dulce de leche","crema de cielo","chocolate","frutilla","menta"])
# mi_heladeria.describir_restaurante()
# mi_heladeria.abrir_restaurante()
# mi_heladeria.los_sabores()

"""
5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada
"""

# class Personaje:
#     def __init__(self,vida,posicion,velocidad):
#         self.vida=vida
#         self.posicion=posicion
#         self.velocidad=velocidad
#     def recibir_ataque(self,cantidad):
#         self.vida -= cantidad
#         if self.vida <=0:
#             self.vida =0
#             print("el jugador ha muerto")
#     def movimiento(self,direccion):
#         if direccion=="arriba":
#             self.posicion=(self.posicion[0],self.posicion[1] + self.velocidad)
#         elif direccion=="abajo":
#             self.posicion=(self.posicion[0],self.posicion[1] - self.velocidad)
#         elif direccion=="izquierda":
#             self.posicion=(self.posicion[0] - self.velocidad, self.posicion[1])
#         elif direccion=="derecha":
#             self.posicion=(self.posicion[0] + self.velocidad,self.posicion[1])
#         else:
#             print("posicion no valida")
# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad,ataque):
#         self.vida=vida
#         self.posicion=posicion
#         self.velocidad=velocidad
#         self.ataque=ataque
#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida<= 0:
#             self.vida=0
#             print("el jugador ha muerto")
#     def movimiento(self, direccion):
#         if direccion=="arriba":
#                         self.posicion=(self.posicion[0],self.posicion[1] + self.velocidad)
#         elif direccion=="abajo":
#             self.posicion=(self.posicion[0],self.posicion[1] - self.velocidad)
#         elif direccion=="izquierda":
#             self.posicion=(self.posicion[0] - self.velocidad, self.posicion[1])
#         elif direccion=="derecha":
#             self.posicion=(self.posicion[0] + self.velocidad,self.posicion[1])
#         else:
#             print("posicion no valida")
#     def atacar(self,otro_personaje):
#         otro_personaje.recibir_ataque(self.ataque)
# class Campesino:
#     def __init__(self,vida,posicion,velocidad,cosecha):
#             self.vida=vida
#             self.posicion=posicion
#             self.velocidad=velocidad
#             self.cosecha=cosecha
#     def recibir_ataque(self,cantidad):
#         self.vida-=cantidad
#         if self.vida<=0:
#             self.vida=0
#             print("el jugador ha muerto")
#     def movimiento(self, direccion):
#         if direccion=="arriba":
#                         self.posicion=(self.posicion[0],self.posicion[1] + self.velocidad)
#         elif direccion=="abajo":
#             self.posicion=(self.posicion[0],self.posicion[1] - self.velocidad)
#         elif direccion=="izquierda":
#             self.posicion=(self.posicion[0] - self.velocidad, self.posicion[1])
#         elif direccion=="derecha":
#             self.posicion=(self.posicion[0] + self.velocidad,self.posicion[1])
#         else:
#             print("posicion no valida")
#     def cosechar(self):
#         return self.cosecha
# soldado=Soldado(100,(5,9),5,20)
# campesino=Campesino(100,(1,10),3,50)
# soldado.movimiento="derecha"
# campesino.movimiento="arriba"
# print(f"El soldado esta en la posicion:{soldado.posicion}")
# print(f"El campersino esta en la posicion:{campesino.posicion}")
# soldado.atacar(campesino)
# print(F"VIda actual del campesino:{campesino.vida}")
# cants_cosechadas=campesino.cosechar()
# print(F"Esta es la cantidada que cosecho el campesino:{cants_cosechadas}")
"""
6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.
"""
# class Usuario:
#     def __init__(self,nombre,apellido,gmail,edad):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.gmail=gmail
#         self.edad=edad
#     def describir_usuario(self):
#         print(F"Nombre:{self.nombre}")
#         print(F"Apellido:{self.apellido}")
#         print(F"Gmail:{self.gmail}")
#         print(F"Edad:{self.edad}")
#     def saludar_usuario(self):
#         print(F"Hola {self.nombre} como estas?")
# usuario1=Usuario("Juani","Torres","juanitoTorrr57@gmail.com",5)
# usuario2=Usuario("MArtina","Perez","MartuPE1434@gmail.com",30)
# usuario3=Usuario("Jorge","JOrgito","jorgitofake@gmail.com",78)
# usuario4=Usuario("Mica","Fernandez","mmicaferr@gmail.com",23)
# usuarios=[usuario1,usuario2,usuario3,usuario4]
# for usuario in usuarios:
#     usuario.describir_usuario()
#     usuario.saludar_usuario()
#     print("--------------------------")
"""
7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

"""
# class Usuario:
#     def __init__(self,nombre,apellido,gmail,edad):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.gmail=gmail
#         self.edad=edad
#     def describir_usuario(self):
#         print(F"Nombre:{self.nombre}")
#         print(F"Apellido:{self.apellido}")
#         print(F"Gmail:{self.gmail}")
#         print(F"Edad:{self.edad}")
#     def saludar_usuario(self):
#         print(F"Hola {self.nombre} como estas?")
# class Admin(Usuario):
#     def __init__(self,nombre,apellido,gmail,edad,privilegios):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.gmail=gmail
#         self.edad=edad
#         self.privilegios=privilegios
#     def mostrar_privilegios(self):
#         print("Privilegios del admin:")
#         for privilegio in self.privilegios:
#             print(privilegio)
# admin=Admin("Fede","Suarez","federez@gmail.com",30,
#             ["puede postear en el foro", "puede borrar un post", "puede banear usuario"])
# admin.describir_usuario()
# admin.saludar_usuario()
# admin.mostrar_privilegios()
"""
8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
el método para mostrar privilegios.
"""
# class Usuario:
#     def __init__(self,nombre,apellido,gmail,edad):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.gmail=gmail
#         self.edad=edad
#     def describir_usuario(self):
#         print(F"Nombre:{self.nombre}")
#         print(F"Apellido:{self.apellido}")
#         print(F"Gmail:{self.gmail}")
#         print(F"Edad:{self.edad}")
#     def saludar_usuario(self):
#         print(F"Hola {self.nombre} como estas?")
# class Privilegios:
#     def __init__(self,privilegios):
#         self.privilegios=privilegios
#     def mostrar_privilegios(self):
#         print("Privilegios del admin:")
#         for privilegio in self.privilegios:
#             print(privilegio)
# class Admin(Usuario):
#     def __init__(self,nombre,apellido,gmail,edad,privilegios):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.gmail=gmail
#         self.edad=edad
#         self.privilegios=Privilegios(privilegios)
# admin=Admin("Fede","Suarez","federez@gmail.com",30,
#             ["puede postear en el foro", "puede borrar un post", "puede banear usuario"])
# admin.describir_usuario()
# admin.saludar_usuario()
# admin.privilegios.mostrar_privilegios()
"""
9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
funcionó.

"""
# from restaurante_ejercicio9_modulo import Restaurante
# class Heladeria(Restaurante):
#     def __init__(self,restaurante_nombre,tipo_comida,sabores):
#         self.restaurante_nombre=restaurante_nombre
#         self.tipo_comida=tipo_comida
#         self.sabores=sabores
#     def los_sabores(self):
#         print("Sabores disponibles: ")
#         for sabor in self.sabores:
#             print(f"-{sabor}")
# mi_heladeria=Heladeria("Heladerias de fulano","Helados",["dulce de leche","crema de cielo","chocolate","frutilla","menta"])
# mi_heladeria.describir_restaurante()
# mi_heladeria.abrir_restaurante()
# mi_heladeria.los_sabores()
