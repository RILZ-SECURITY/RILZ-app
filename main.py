from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import sys

class RilzApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        self.layout.add_widget(Label(text='RILZ SECURITY SYSTEM', font_size=24, color=(1, 1, 1, 1)))
        
        # Input Password
        self.pass_input = TextInput(hint_text='Masukkan Password', password=True, multiline=False, size_hint_y=None, height=100)
        self.layout.add_widget(self.pass_input)
        
        # Tombol Unlock
        btn = Button(text='UNLOCK SYSTEM', background_color=(1, 0, 0, 1), size_hint_y=None, height=120)
        btn.bind(on_press=self.cek_password)
        self.layout.add_widget(btn)
        
        # INFO NOMOR HP LU YANG BENER
        self.layout.add_widget(Label(text='Owner: 08972142960', font_size=16, color=(0.8, 0.8, 0.8, 1)))
        
        return self.layout

    def cek_password(self, instance):
        # Password: rilz
        if self.pass_input.text == 'rilz':
            sys.exit() 
        else:
            self.pass_input.text = ''
            self.pass_input.hint_text = 'PASSWORD SALAH!'

if __name__ == '__main__':
    RilzApp().run()
      
