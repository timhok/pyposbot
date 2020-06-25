# PyPOSBot
Telegram bot for POS Printer written in python

This project uses [ESCPOS python implementation](https://github.com/python-escpos/python-escpos) and [pyTelegramBotAPI (or telebot)](https://github.com/eternnoir/pyTelegramBotAPI) for Telegram bot functionality

Inspired by ["Дешёвая и быстрая печать на чековом термопринтере" article](https://habr.com/ru/post/486998/) by [@gbougakov](https://github.com/gbougakov/)

### What this bot can do?
Its all about printing stuff, so this bot can print for you:
* **Text** - useful for labeling things or make quick notes
* **Images** - PyPOSBot automatically fits images in paper width, you can print photos from your phone, just like using an instant camera
* **QR codes**
* **Barcodes** - such as ean13, upc-a, code39

## Prerequisites
Used POS (or thermal paper) Printers can be easily picked up for cheap off the flea markets.

Make sure you can communicate with your printer of choice with [supported methods](https://python-escpos.readthedocs.io/en/latest/user/usage.html#define-your-printer) and it's compatible with [ESC/POS](https://en.wikipedia.org/wiki/ESC/P)

> For my case with Citizen CT-S2000 it can switch between pure USB and built-in usb-to-serial converter.
> Using USB with Python on a Windows is a pain in the butt, so I changed it to serial in Citizen's "POS Printer Utility"

You should have your printer configured by Vendor software, for example - make sure to chose right density because escpos uses this information for text/image alignment

## Requirements
* Python 3.7 or higher
* [python-escpos](https://github.com/python-escpos/python-escpos) 3.0a8 or higher (can be installed with "pip install python-escpos --pre")
* [telebot](https://github.com/eternnoir/pyTelegramBotAPI#getting-started)
* Telegram Bot and its api token (use [BotFather](https://telegram.me/BotFather) to create new bot)
* [Pillow](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)

## Configuration
Copy or rename **config.py.example** to **config.py** and make changes as appropriate. I have provided comments for every variable.

Copy or rename profile for your printer - **config.yaml.example** to **config.yaml**. Use [this docs](https://python-escpos.readthedocs.io/en/latest/user/usage.html#the-printer-section) for help.

I also have provided two language versions of strings used by the bot.

If you happen to speak in Russian, in posbot.py change 
```python
from guitext_en import guitext
```
to 
```python
from guitext import guitext
```
## Run bot

```bash
$ python3 posbot.py
```
If you did everything correctly, the bot should be running. Go do `/start` to see if the bot is live and get information about available commands.

