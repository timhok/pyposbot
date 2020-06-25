# -*- coding: utf-8 -*-
guitext = {
	"commands": {
#		"<command>": {
#			"help": "<replied if command has no parameters>",
#			"reply": "<replied if the action was a success>",
#			"error": "<replied on error, for example if wrong parameter is passed>"
#		},
		"start": {
			"help": "Hi there!" + "\n\n" +
					"You can send me image or text for printing" + "\n\n" +
					"Or you can also use these commands:",
		},
		"qr": {
			"help": "*/qr text* - print QR code with text",
			"reply": "Printing qr: ",
			"error": "This command requires an argument!"
		},
		"ean13": {
			"help": "*/ean13 number* - print ean13 of this number",
			"reply": "Printing ean13: ",
			"error": "This command requires an argument!"
		},
		"more": {
			"help": "*/more [amount]* - print last image again",
			"reply": "Printing last image again\nAmount: ",
			"error": "You requested too much! Maximum amount - "
		},
	},
	"actions": {
		"image": {
			"help": "",
			"reply": "Printing this image",
			"error": "You didnt sent me any images!"
		},
		"text": {
			"help": "",
			"reply": "Printing this text",
			"error": ""
		},
		"barcode": {
			"help": "",
			"reply": "Printing this barcode",
			"error": "Wrong format for this barcode"
		},
	},
}