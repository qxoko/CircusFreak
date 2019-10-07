import re
import sublime
import sublime_plugin

class CircusFreakSelectCommand(sublime_plugin.TextCommand):
	def run(self, action):
		self.list = [
			"Circus Freak",
			"Mystery",
			"Peach Fuzz",
			"Tetrachroma",
		]
		self.schemes = [
			"Packages/Circus Freak/Circus Freak.sublime-color-scheme",
			"Packages/Circus Freak/Mystery.sublime-color-scheme",
			"Packages/Circus Freak/Peach Fuzz.sublime-color-scheme",
			"Packages/Circus Freak/Tetrachroma.sublime-color-scheme",
		]
		self.themes = [
			"Circus Dark.sublime-theme",
			"Circus Dark.sublime-theme",
			"Circus Dark.sublime-theme",
			"Circus Dark.sublime-theme",
		]
		self.show_panel()

	def show_panel(self):
		self.view.window().show_quick_panel(self.list, self.on_done, on_highlight=self.on_highlighted)

	def on_done(self, index):
		theme = self.themes[index]
		self.set_scheme(self.schemes[index])
		self.set_theme(theme)
		self.save_settings(theme)

	def on_highlighted(self, index):
		self.set_scheme(self.schemes[index])
		self.set_theme(self.themes[index])

	def set_scheme(self, scheme):
		self.get_settings().set('color_scheme', scheme)

	def set_theme(self, theme):
		self.get_settings().set('theme', theme)

	def get_settings(self):
		return sublime.load_settings('Preferences.sublime-settings')

	def save_settings(self, theme):
		sublime.save_settings('Preferences.sublime-settings')
		sublime.status_message('Circus Freak: ' + theme)
		print('')
		print('[Circus Freak] ' +  theme)
		print('')