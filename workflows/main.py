#!/usr/bin/env python3
JARVIS Android — Gercek zamanli sesli yardimci cekirdegi
"""

import asyncio
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text='J.A.R.V.I.S Android Ready', font_size='20sp')
        self.add_widget(self.label)
        self.btn = Button(text='Başlat', size_hint=(1, 0.2))
        self.add_widget(self.btn)

class JarvisApp(App):
    def build(self):
        return JarvisUI()

if __name__ == '__main__':
    JarvisApp().run()