# -*- coding: utf-8 -*-
import telebot
import time
import PIL
import os.path
from escpos.printer import *
from escpos import config
from config import *
from guitext_en import guitext

c = config.Config()
c.load("config.yaml")
p = c.printer()
p.charcode(printer_charcode)
# for some reason escpos does not registering width value from printer config
p.profile.profile_data["media"]["width"]["pixels"] = printer_basewidth
bot = telebot.TeleBot(telegram_bot_token)


def pos_image(image_file, cut):
	p.image(image_file)
	if cut:
		p.cut()

def convert_image(image_file):
	# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio/451580#451580
	img = PIL.Image.open(image_file)
	wpercent = (printer_basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	# resize to fit printer_basewidth
	img = img.resize((printer_basewidth, hsize), PIL.Image.ANTIALIAS)
	# rotating images gives more esthetic look when printing
	if settings_images_rotate:
		img = img.rotate(180)
	img.save(image_file)

@bot.message_handler(commands=["start", "help"])
def start(message):
	commands_help = ""
	for command in guitext["commands"]:
		commands_help = commands_help + "\n" + guitext["commands"][command]["help"]
	bot.reply_to(message, commands_help, parse_mode= "Markdown")

@bot.message_handler(commands=["qr", "ean13", "ean8", "upc-a", "upc-e", "code39", "itf", "nw7"])
def print_barcodes(message):
	barcode_type = str(message.text.split()[0])[1:]
	if len(message.text.split()) > 1:
		param = str(message.text.split(maxsplit=1)[1])
		# TODO: qr settings
		if barcode_type == "qr":
			p.qr(param, size=13, center=True)
			p.cut()
		else:
			try:
				p.barcode(param, barcode_type.upper())
				p.cut()
			except:
				bot.reply_to(message, guitext["actions"]["barcode"]["error"], parse_mode= "Markdown")
				return
		# im too lazy to fill guitext for every barcode, so lets just skip this reply
		try:
			bot.reply_to(message, guitext["commands"][barcode_type]["reply"] + param, parse_mode= "Markdown")
		except KeyError:
			bot.reply_to(message, guitext["actions"]["barcode"]["reply"], parse_mode= "Markdown")
	else:
		bot.reply_to(message, guitext["commands"][barcode_type]["error"] + "\n" + guitext["commands"][barcode_type]["help"], parse_mode= "Markdown")

@bot.message_handler(commands=["ewe", "more", "repeat"])
def print_moreimages(message):
	image_file = settings_images_storepath + str(message.from_user.id) + ".jpg"
	if os.path.isfile(image_file):
		if len(message.text.split()) > 1:
			param = str(message.text.split(maxsplit=1)[1])
			if int(param) <= settings_moreimages_max:
				for b in range(0, int(param)):
					pos_image(image_file, settings_moreimages_cuteach)
				if not settings_moreimages_cuteach:
					p.cut()
				bot.reply_to(message, guitext["commands"]["more"]["reply"] + param, parse_mode= "Markdown")
			else:
				bot.reply_to(message, guitext["commands"]["more"]["error"] + str(settings_moreimages_max), parse_mode= "Markdown")
		else:
			pos_image(image_file, True)
			bot.reply_to(message, guitext["commands"]["more"]["reply"] + "1", parse_mode= "Markdown")
	else:
		bot.reply_to(message, guitext["actions"]["image"]["error"], parse_mode= "Markdown")


@bot.message_handler(content_types=["text"])
def print_text(message):
	# TODO: more config options
	p.set(align="left", double_height=settings_text_doublesize, double_width=settings_text_doublesize)
	# sometimes printer can not get enough feed speed in time and prints is scuffed,
	# so adding empty line before text helps with that
	p.text("\n")
	p.text(str(message.text))
	p.text("\n")
	p.cut()
	bot.reply_to(message, guitext["actions"]["text"]["reply"], parse_mode= "Markdown")

@bot.message_handler(content_types=["photo"])
def print_image(message):
	if message.content_type == "photo":
		# download image from message
		image_file = settings_images_storepath + str(message.from_user.id) + ".jpg"
		photo_file = bot.get_file(message.photo[-1].file_id)
		downloaded_file = bot.download_file(photo_file.file_path)
		with open(image_file,"wb") as new_file:
			new_file.write(downloaded_file)
		# every sleep here is for FS sync
		time.sleep(1)
		convert_image(image_file)
		time.sleep(1)
		pos_image(image_file, True)
		bot.reply_to(message, guitext["actions"]["image"]["reply"] + "\n" + guitext["commands"]["more"]["help"], parse_mode= "Markdown")

bot.polling()