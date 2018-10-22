# Circus Freak Collective
A clean, dark theme collection for Sublime Text and iTerm

##### CIRCUS FREAK
![](screenshots/freak_iterm.png)

##### MYSTERY
![](screenshots/mystery_iterm.png)

The font used in all screenshots is San Francisco Mono.

## MANIFESTO
Circus Freak was created with Fountain, Python and Lua in mind.  It supports [Fountainhead](https://packagecontrol.io/packages/Fountainhead).

Originally a single theme, Circus Freak has now been turned into a collection.

## INSTALLATION & SETTINGS
Package Control coming soon!

### SUBLIME
+ Download the [latest Sublime release](https://github.com/thehfd/circus-freak/releases).
+ Unzip and rename folder to `Circus Freak`.
+ Move folder inside the Packages directory: `Preferences > Browse packages...`
+ Use the command palette / preferences menu to set a Circus Freak theme and scheme, or paste the two lines below into your User Preferences (replace `Mystery` with your chosen theme):

```json
{
	"color_scheme": "Packages/Circus Freak/Mystery.sublime-color-scheme",
	"theme": "Mystery.sublime-theme",
}
```

### ITERM
+ Download the [latest iTerm release](https://github.com/thehfd/circus-freak/releases).
+ Unzip the file.
+ Navigate to `Preferences` > `Profiles` > `Colors`
+ In the bottom-right, select the `Color Presets` dropdown.
+ Use the `Import...` button, select the chosen theme and confirm.
+ Re-open the `Color Presets` dropdown to find the imported selection in the list.

## CUSTOMISATION
##### USER PREFERENCES
Tweak the sidebar icon and button with the one of the User Preferences presets below.  Not including one will default them to a shade of grey.

```json
{
	// Circus Freak
	"circus_accent_red": true,
	"circus_accent_yellow": true,
	"circus_accent_blue": true,
	"circus_accent_purple": true,
	"circus_accent_pink": true,

	// Mystery
	"mystery_accent_red": true,
	"mystery_accent_yellow": true,
	"mystery_accent_blue": true,
	"mystery_accent_purple": true,
	"mystery_accent_green": true,
}
```

##### FONT SETTINGS OVERRIDE
Paste the following into a file named after your chosen UI theme, i.e: "Mystery.sublime-theme", and save it to your user directory.  This is the setting used in the screenshots above to apply San Francisco Mono to the entire UI.  You can also manipulate the tab height.

```json
[
	// sidebar heading name font / size
	{
		"class": "sidebar_heading",
		"font.face": "SF Mono Light",
		"font.size": 12,
	},
	// sidebar file name font / size
	{
		"class": "sidebar_label",
		"font.face": "SF Mono Light",
		"font.size": 12,
	},
	// tab name font / size
	{
		"class": "tab_label",
		"font.face": "SF Mono Light",
		"font.size": 12,
	},
	// height of open tabs
	{
		"class": "tabset_control",
		"tab_height": 34
	}
]
```

##### CREDITATION
Circus Freak's UI theme is a fork of [amCoder](https://packagecontrol.io/packages/Theme%20-%20amCoder).

##### TO DO
Circus Freak themes are tested on large code bases that make expansive use of the syntax, to ensure the best possible highlighting is available for the most commonly used syntax packages.

The below list is comprises languages that have only been minimally tested, but are otherwise fully supported.  Do not hesitate to submit an issue if \<your favourite language feature\> is found lacking in this collection.

+ HTML / CSS / JS
+ C / C++ / C#