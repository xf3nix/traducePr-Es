from kivy.app import App
from googletrans import Translator
from kivy.uix.boxlayout import BoxLayout


'''

https://www.codeproject.com/Tips/1236705/How-to-Use-Google-Translator-in-Python

Return value of translate API is a Translated class object, which has the following member variables.

    src – source language (default: auto)
    dest – destination language (default: en)
    origin – original text
    text – translated text
    pronunciation – pronunciation

To access the translated string and source language, access member variables of translated object.

'''


class Box01(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def trasladar(self):

        entrada = self.ids.entrada.text

        if entrada != "":

            translator = Translator()

            translated = translator.translate(entrada, src='es', dest='pt')
            
            self.ids.salida.text = translated.text

    def limpiar(self):
        self.ids.entrada.text = ""
        self.ids.salida.text = ""


class MainApp(App):
    title = "Portuñol"

    def build(self):
        return Box01()


if __name__ == "__main__":
    MainApp().run()
