# -*- coding: utf-8 -*-
guitext = {
	"commands": {
#		"<command>": {
#			"help": "<replied if command has no parameters>",
#			"reply": "<replied if the action was a success>",
#			"error": "<replied on error, for example if wrong parameter is passed>"
#		},
		"start": {
			"help": "Дарова!" + "\n\n" +
					"Ты можешь просто прислать мне текст или картинку для печати" + "\n\n" +
					"Или использовать доступные команды:",
		},
		"qr": {
			"help": "*/qr текст* - печать QR с указанным текстом",
			"reply": "Печатаем qr: ",
			"error": "Для этой команды нужен параметр!"
		},
		"ean13": {
			"help": "*/ean13 номер* - печать ean13 с указанным номером",
			"reply": "Печатаем ean13: ",
			"error": "Для этой команды нужен параметр!"
		},
		"more": {
			"help": "*/ewe [количество]* - напечатать картинку ещё раз",
			"reply": "Ещё раз печатаем последнюю картинку\nКоличество: ",
			"error": "Ты слишком много хочешь, максимальное количество - "
		},
	},
	"actions": {
		"image": {
			"help": "",
			"reply": "Печатаем эту картинку",
			"error": "Ты не присылал мне картинок!"
		},
		"text": {
			"help": "",
			"reply": "Печатаем этот текст",
			"error": ""
		},
		"barcode": {
			"help": "",
			"reply": "Печатаем этот штрихкод",
			"error": "Неверный формат"
		},
	},
}