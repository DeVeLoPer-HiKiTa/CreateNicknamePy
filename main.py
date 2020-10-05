from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 300)
Config.set("graphics", "height", 200)

#name - nickname in Cyrillic
#alternation_of_characters - do we need to alternate case
def create_nickname(name, alternation_of_characters):
	#result
	res_name = ""
	#big letter or small
	upper_case = True
	permissible_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
	lowercase_symbols = {
		'а': 'a',   'п': 'ri',  'л': 'JI',
		'б': '6',   'р': 'p',   'ю': 'l0',
		'в': 'B',   'с': 'c',   'я': '9l',
		'г': 'r',   'т': 'rri', 'д': 'g',
	    'у': 'y',   'е': 'е',   'ф': 'olo',
		'ж': 'JK',  'х': 'x',   'з': '3',
	    'ц': 'LL',  'и': 'U',   'ч': '4',
		'к': 'K',   'ш': 'LLI', 'э': '3', 
		'щ': 'LIL', 'м': 'M',   'ъ': 'b',
		'н': 'H',   'ы': 'bl',  'о': 'o', 
		'ь': 'b',   ' ': '_',   'й': 'U',
		'ё': 'е'
	}
	uppercase_symbols = {
		'а': 'A',   'п': 'ri',  'л': 'JI',
		'б': '6',   'р': 'P',   'ю': 'lO',
		'в': 'l3',  'с': 'C',   'я': '9l',
		'г': 'r',   'т': 'T',   'д': 'D',
	    'у': 'y',   'е': 'E',   'ф': 'olo',
		'ж': 'JK',  'х': 'X',   'з': '3',
	    'ц': 'LL',  'и': 'U',   'ч': '4',
		'к': 'K',   'ш': 'LLI', 'э': '3', 
		'щ': 'LIL', 'м': 'M',   'ъ': 'b',
		'н': 'H',   'ы': 'bl',  'о': 'O', 
		'ь': 'b',   ' ': '_',   'й': 'U',
		'ё': 'E'
	}
	i = 0
	size = len(name)
	while i < size:
		if name[i] in permissible_symbols:
			if alternation_of_characters:
				if upper_case:
					#if "р" is in the middle of the nickname
					if (name[i] == 'р' or name[i] == 'P') and i > 0:
						res_name += 'R'
					else:
						res_name += uppercase_symbols[name[i]]
				else:
					if name[i] == 'Р' and i > 0:
						res_name += 'p'
					else:
						res_name += lowercase_symbols[name[i]]
			else:
				res_name += lowercase_symbols[name[i]]
		else:
			res_name += name[i]
		if name[i] == ' ':
			upper_case = True
		else:
			upper_case = not upper_case
		i += 1

	return res_name


class MyApp(App):
	def build(self):
		self.title = "Create the nickname"
		self.icon = "icon.png"
		floatlayout = FloatLayout(size = (300, 200))

		button = Button(
			text      = "создать никнейм", 
			font_size = 20,
			on_press  = self.button_press,
			size = (200, 50),
			size_hint=(None, None),
			pos = (50, 40)
			)
		self.nameInput = TextInput(
			text = "игрок",
			cursor_color = [0, 0, 0, 1],
			multiline = False,
			height = 30,
			width = 290,
			size_hint=(None, None),
			pos = (5, 165)
				)
		self.nameOutput = TextInput(
			text = "UrRoK",
			cursor_color = [0, 0, 0, 1],
			multiline = False,
			height = 30,
			width = 290,
			size_hint=(None, None),
			pos = (5, 125)
				)
		#to check whether the register needs to be alternated
		self.checkBox = CheckBox(
			pos = (10, 105),
			size_hint=(None, None),
			height = 15,
			width = 15,
			)
		label_for_check_box = Label(
			text = "чередовать регистр(АаАа)",
			size_hint=(None, None),
			height = 30,
			width = 200,
			pos = (20, 95)
			)

		floatlayout.add_widget(button)
		floatlayout.add_widget(self.nameInput)
		floatlayout.add_widget(self.nameOutput)
		floatlayout.add_widget(self.checkBox)
		floatlayout.add_widget(label_for_check_box)
		
		return floatlayout

	def button_press(self, instance):
		self.nameOutput.text = create_nickname(self.nameInput.text, self.checkBox.active)

if __name__ == "__main__":
	MyApp().run()