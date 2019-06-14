# Circus Freak Collective
A clean, dark theme collection for Sublime Text and iTerm

#### Circus Freak

###### CLEAN PROJECT
![](https://i.imgur.com/VSBOzwp.png)

###### MESSY PROJECT
![](https://i.imgur.com/LLZmbLQ.png)

#### Mystery

###### CLEAN PROJECT
![](https://i.imgur.com/RV3al9w.png)

###### MESSY PROJECT
![](https://i.imgur.com/THW0ncG.png)

#### Peach Fuzz

###### CLEAN PROJECT
![](https://i.imgur.com/yh8voGM.png)

###### MESSY PROJECT
![](https://i.imgur.com/hqoYvaq.png)

The font used in all screenshots is San Francisco Mono.

## Installation and Settings

#### Sublime Text 3
+ Download the [latest Sublime release](https://github.com/qxoko/CircusFreak/releases).
+ Unzip and rename the folder to `Circus Freak`.
+ Move folder inside the Packages directory: `Preferences > Browse packages...`
+ Search for `Circus Freak: Set Theme` in the command palette to preview and set the themes.
+ Alternatively, you can paste the two lines below into your User Preferences (replace `Mystery` with your chosen theme):

```json
{
	"color_scheme": "Packages/Circus Freak/Mystery.sublime-color-scheme",
	"theme": "Circus Dark.sublime-theme",
}
```

#### iTerm
+ Download the [latest iTerm release](https://github.com/qxoko/CircusFreak/releases).
+ Unzip the file.
+ Navigate to `Preferences` > `Profiles` > `Colors`
+ In the bottom-right, select the `Color Presets` dropdown.
+ Use the `Import...` button, select the chosen theme and confirm.
+ Re-open the `Color Presets` dropdown to find the imported selection in the list.

## Customisation
#### Font Settings
Paste the following into a file named `Circus Dark.sublime-theme`, and save it to your `User` directory.  This is the setting used in the screenshots above to apply San Francisco Mono to the entire UI.  You can also manipulate the tab height.  This list of settings is not exhaustive.  You can consult the theming documentation for Sublime Text 3 to change other single settings.

```json
[
	{
		"class": "tab_label",
		"font.face": "SF Mono Light",
		"font.size": 13,
	},
	{
		"class": "tabset_control",
		"tab_height": 34
	},
	{
		"class": "sidebar_heading",
		"font.face": "SF Mono Light",
		"font.size": 13,
	},
	{
		"class": "sidebar_label",
		"font.face": "SF Mono Light",
		"font.size": 13,
	},
	{
		"class": "quick_panel_label",
		"font.face": "SF Mono Light",
		"font.size": 13,
	},
	{
		"class": "quick_panel_path_label",
		"font.face": "SF Mono Light",
		"font.size": 11,
	},
	{
		"class": "quick_panel_score_label",
		"font.face": "SF Mono Light",
	},
	{
		"class": "label_control",
		"font.face": "SF Mono Light",
	}
]
```

## Creditation
Circus Freak's UI theme began as a fork of [amCoder](https://packagecontrol.io/packages/Theme%20-%20amCoder).