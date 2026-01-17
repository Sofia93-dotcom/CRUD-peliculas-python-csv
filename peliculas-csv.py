#funciones auxiliares
import csv

                  
def pedir_texto(mensaje):
      while True:
            texto=input(mensaje).strip()
            if texto=="":
                  print("El campo no puede estar vacío")
                  continue
            return texto
      
def pedir_anio(mensaje):
      while True:
            numero=input(mensaje).strip()
            try:
                  numero=int(numero)
            except ValueError:
                  print("Solamente se aceptan números, no texto")
                  continue
            return numero  

def existe_titulo(titulo):
      try:

           with open("peliculas.csv",mode="r",newline="",encoding="utf-8")as archivo:
            lector=csv.reader(archivo)
            encabezado=next(lector)

            for fila in lector:
                  if not fila:
                       continue
                  if fila[0].lower()==titulo.lower():
                        return True
      except FileNotFoundError:
           return False           
                  
      return False  
#funciones principales
def agregar_pelicula():
      titulo=pedir_texto("Ingrese el titulo :").title()
      if existe_titulo(titulo):
            print("El titulo que desea ingresar ya existe")
            return
      
      genero=pedir_texto("Ingrese el género").title()
      anio=pedir_anio("Ingrese el año :")



      with open("peliculas.csv",mode="a", newline="",encoding="utf-8")as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow([titulo,genero,anio ])
      print("Pelicula agregada correctamente")   

def mostrar_peliculas():
    total_peliculas = 0

    try:
        with open("peliculas.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)

            for i, fila in enumerate(lector, start=1):
                if not fila:
                     continue
                print(f"{i}) Título: {fila[0]} | Género: {fila[1]} | Año: {fila[2]}")
                total_peliculas += 1

    except FileNotFoundError:
        print("El archivo 'peliculas.csv' no existe")
        return

    if total_peliculas == 0:
        print("No se encontraron películas")
    else:
        print(f"El total de películas es de: {total_peliculas}")

      


            

def buscar_pelicula():
     titulo=pedir_texto("Ingrese el titulo :").lower()
     contador=0
     try:
         with open("peliculas.csv",mode="r",newline="",encoding="utf-8")as archivo:
           lector=csv.reader(archivo)
           encabezado=next(lector)

           for fila in lector:
                 if not fila:
                      continue
                 if titulo in fila[0].lower():
                       print(f"Titulo : {fila[0]}, Género : {fila[1]}, Año : {fila[2]}")
                       contador+=1
     except FileNotFoundError:
           print("Aún no hay peliculas cargadas")  
           return

     if contador==0:
          print("No se encontraron resultados para su búsqueda")
     else:
          print(f"Los resultados encontrados son : {contador}") 


def eliminar_pelicula():
    titulo = pedir_texto("Ingrese el titulo de la pelicula a eliminar: ").lower()

    try:
        with open("peliculas.csv", mode="r",newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)

            lista_nueva = []
            eliminado = False

            for fila in lector:
                if not fila:
                     continue
                if fila[0].lower() == titulo:
                    eliminado = True
                else:
                    lista_nueva.append(fila)

    except FileNotFoundError:
        print("Aún no hay películas cargadas")
        return

    if not eliminado:
        print("La película que desea eliminar no existe")
        return

    with open("peliculas.csv", mode="w", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)
        escritor.writerows(lista_nueva)

    print("Película eliminada correctamente")

def editar_pelicula():
     titulo=pedir_texto("Ingrese el titulo de la pelicula a editar :").lower()
     try:
          with open("peliculas.csv",mode="r",newline="",encoding="utf-8")as archivo:
               lector=csv.reader(archivo)
               encabezado=next(lector)

               lista_nueva=[]
               editado=False

               for fila in lector:
                    if not fila:
                         continue
                    if fila[0].lower()==titulo:
                         genero_nuevo=pedir_texto("Ingrese nuevamente el género :").title()
                         anio_nuevo=pedir_anio("Ingrese nuevamente el año :")
                         pelicula_editada=[fila[0],genero_nuevo,anio_nuevo]
                         lista_nueva.append(pelicula_editada)
                         editado=True
                    else:
                         lista_nueva.append(fila)
     except FileNotFoundError:
           
          print("Aún no hay peliculas cargadas")
          return
     if not editado:
          print("La pelicula ingresada no existe")
          return
     with open("peliculas.csv",mode="w",newline="",encoding="utf-8")as archivo:
          escritor=csv.writer(archivo)
          escritor.writerow(encabezado)
          escritor.writerows(lista_nueva)
     print("Pelicula editada correctamente!")     
          
     


              
          
     
                        
                 
                 
                    
                        
   

               

                         
          
                                       
      


      


      
            



#menu principal:
def mostrar_menu():
    
        print("="*50)
        print("\n---MENÚ---")
        print("1.Agregar pelicula")
        print("2.Mostrar peliculas")
        print("3.Buscar pelicula")
        print("4.Eliminar pelicula")
        print("5.Editar pelicula")
        print("6.Salir")
        print("="*50)
def main():
      while True:
            mostrar_menu()
            opcion=input("Ingrese una opción :").strip()
            match opcion:
                  case "1":
                        agregar_pelicula()
                  case "2":
                        mostrar_peliculas()
                  case "3":
                        buscar_pelicula()
                  case "4":
                      eliminar_pelicula()
                  case "5":
                      editar_pelicula()
                  case "6":
                      print("Saliendo")
                      break        
                        
                        
                  case _:
                        print("Error. Ingrese una opción de la 1 a 6")  


main()
      






       

          


 