#Escribir una clase en python llamada círculo que contenga un radio, con un método que
#devuelva el área y otro que devuelva el perímetro del círculo.
#Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
#usuario e impidiendo la instanciación.
#Si printeamos el objeto creado debe mostrarse una representación amigable.
#El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
#mostrar un error y no permitir modificación.
#Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
#multiplicado por n. No permitir la multiplicación por números <= 0
#solo clases
# probando, solo actualizo clases

import matplotlib.pyplot as plt
import math

class Circulo:

   def __init__(self, radio):
        self.radio = radio

    # devuelve el radio
   def get_radio(self):

       return self.radio

   # calcula y devuelve el area
   def devolver_area(self):

        xarea = math.pi * ( self.radio ** 2 )

        return xarea

   # calcula y devuelve el perimetro
   def devolver_perimetro(self):

        xperimetro = 2 * math.pi *  self.radio

        return xperimetro

   # dibuja el circulo
   def dibujar_circulo(self):

       figure, axes = plt.subplots()
       draw_circle = plt.Circle((10, 10),  self.radio)

       plt.xlim(0, 20)
       plt.ylim(0, 20)

       axes.set_aspect(1)
       axes.add_artist(draw_circle)
       plt.title('Circle')
       plt.show()

       return


while True:

    print("Ingresa el radio del Circulo !:( q para salir)")

    xradio = input()

    try:

        fradio = int(xradio)

        if fradio > 0:

            if fradio <20:

                circu = Circulo(fradio)

                print(circu.get_radio())

                print("El area es {:.2f}".format(circu.devolver_area()) )
                print("El perimetro es es {:.2f}".format(circu.devolver_perimetro()) )

                circu.dibujar_circulo()
            else:

                print( "el valor del radio debe estar entre 1 y 10")

        else:

            print("ingrese valor mayor a 0")

    except:

        if xradio == "q":
           break
        else:

            print("ingrese valor numerico entero")