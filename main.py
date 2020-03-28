# ----- Inicials Imports ----- #
#import kivy
#kivy.require('1.11.1')

import os
from kivy import Config

# ----- Solution for problems with OpenGL and old graphic cards ----- #
try:
	os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
	Config.set('graphics', 'multisamples', '0')
except:
	pass

# ----- Configuração da janela ----- #
Config.set('graphics', 'resizable', True)
Config.set('kivy', 'exit_on_escape', '0')
Config.set('graphics', 'width', 300)
Config.set('graphics', 'heigth', 500)

# ----- Imports ----- #
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color


class Principal(BoxLayout):

	def __init__(self):
		super().__init__()

		self.a = 0  # Counter
		self.ids.bar_value.size_hint = (1, 0)  # Bar


	def count_up(self):  # Label text up

		if self.a == 100:
			self.ids.label_1.text = '100 %'
		else:
			self.a = self.a + 10
			self.ids.label_1.text = f'{str(self.a)} %'

		self.val(self.a)


	def count_down(self):  # Label text down

		if self.a == 0:
			self.ids.label_1.text = '0 %'
		else:
			self.a = self.a - 10
			self.ids.label_1.text = f'{str(self.a)} %'

		self.val(self.a)


	def val(self, value_y):  # Bar

		self.ids.bar_value.size_hint = (1, (value_y/100))

		if value_y < 31:
			with self.ids.bar_value.canvas:
				Color(rgba=[0, 1, 0, 1])

		elif value_y in range(32, 61):
			with self.ids.bar_value.canvas:
				Color(rgba=[1, 1, 0, 1])

		elif value_y > 61:
			with self.ids.bar_value.canvas:
				Color(rgba=[1, 0, 0, 1])


class Main(App):
	def build(self):
		return Principal()


if __name__ == '__main__':
	Main().run()
