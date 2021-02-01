from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from herencia import *


      

class SecondWindow(Screen):
    verLib = ObjectProperty(None)
    current = ""
   
    def escribe(self):
        self.verLib.text = current

    def on_enter(self, *args):
        #open and read the file after the appending:
        f = open("demofile3.txt", "r")
        self.verLib.text = f.read()
        print(f.read()) 
        
class MainWindow(Screen):
    autor = ObjectProperty(None)
    libro = ObjectProperty(None)
    noLibro = ObjectProperty(None)

    def alta(self):
        miLibrero.altaLib(self.libro.text,self.autor.text)
        self.autor.text = ""
        self.libro.text = ""

    def baja(self):
        miLibrero.baja(int(self.noLibro.text))
        
    def cambioAutor(self):
        miLibrero.cambioAutor(int(self.noLibro.text), self.autor.text)
    
    #al abrir la otra ventana se guarda el librero en un fichero
    def muestraL(self):
        f = open("demofile3.txt", "w")
        f.write(miLibrero.mostrar())


    





class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")



class MyMainApp(App):

    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()