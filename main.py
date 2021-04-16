# ----- Inicials Imports ----- #
# import kivy
# kivy.require('1.11.1')

import os
from kivy import Config
import platform

# ----- Soluciona problemas de OpenGL e placas graficas antigas em windows -- #
if platform.system() == 'Windows':

	os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
	Config.set('graphics', 'multisamples', '0')

# ----- Necessário para Video e Audio no Linux----- #
if platform.system() == 'Linux':

	os.environ['KIVY_VIDEO'] = 'ffpyplayer'

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

		self.a = 0  # Counter 1
		self.b = 0  # Counter 2
		self.ids.bar_value1.size_hint = (0, 0)  # Bar1
		self.ids.bar_value2.size_hint = (0, 0)  # Bar2


# ----------------------------------------------------- #
	def count_up1(self):  # Label text up

		if self.a == 100:
			self.ids.label_1.text = '100 %'
		else:
			self.a = self.a + 10
			self.ids.label_1.text = f'{str(self.a)} %'

		self.val1(self.a)


	def count_up2(self):  # Label text up

		if self.b == 100:
			self.ids.label_2.text = '100 %'
		else:
			self.b = self.b + 10
			self.ids.label_2.text = f'{str(self.b)} %'

		self.val2(self.b)


# ----------------------------------------------------- #
	def count_down1(self):  # Label text down

		if self.a == 0:
			self.ids.label_1.text = '0 %'
		else:
			self.a = self.a - 10
			self.ids.label_1.text = f'{str(self.a)} %'

		self.val1(self.a)


	def count_down2(self):  # Label text down

		if self.b == 0:
			self.ids.label_2.text = '0 %'
		else:
			self.b = self.b - 10
			self.ids.label_2.text = f'{str(self.b)} %'

		self.val2(self.b)


# ----------------------------------------------------- #
	def val1(self, value_y):  # Bar

		self.ids.bar_value1.size_hint = (0.5, (value_y/100))

		if value_y < 31:
			with self.ids.bar_value1.canvas:
				Color(rgba=[0, 1, 0, 1])

		elif value_y in range(32, 61):
			with self.ids.bar_value1.canvas:
				Color(rgba=[1, 1, 0, 1])

		elif value_y > 61:
			with self.ids.bar_value1.canvas:
				Color(rgba=[1, 0, 0, 1])


	def val2(self, value_y):  # Bar

		self.ids.bar_value2.size_hint = (0.5, (value_y/100))

		if value_y < 31:
			with self.ids.bar_value2.canvas:
				Color(rgba=[0, 1, 0, 1])

		elif value_y in range(32, 61):
			with self.ids.bar_value2.canvas:
				Color(rgba=[1, 1, 0, 1])

		elif value_y > 61:
			with self.ids.bar_value2.canvas:
				Color(rgba=[1, 0, 0, 1])


class Main(App):
	def build(self):
		return Principal()


if __name__ == '__main__':
	Main().run()
