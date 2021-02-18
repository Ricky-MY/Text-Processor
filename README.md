# Text Processor

## Table of Contents
* 1. [General Info](#general-info)
* 2. [Documentation](#documentation)
    - [render_lines](#render-lines)

    - [get_links](#get-links)
    - [get_images](#get-images)
    - [get_videos](#get-videos)
    - [get_outcasts](#get-outcasts)
    - [find_word](#find-words)

    - [save](#save)
* 3. [Installation](#how-can-i-run-this-project)

### General Info
This is an API to process `.txt` files.

### Documentation
* Text Processor is an API written in python to process `.txt` files.

Quick Startup to find words:
~~~
from textprocessor import TextProcessor

with TextProcessor('yourtextfile.txt') as ctx:
    ctx.render_lines()
    words = ctx.find_word("hello")
    print(words)
~~~







### Wordy Explanation 
...

### How can I run this project?
Create a virtualenv and install all dependencies inside `requirements.txt`.

> If you are unfamiliar with virtualenv, follow the steps below.

To run this project manually, follow these steps:

* 1. Install the discord.py module (USE PYTHON 3.8 OR ABOVE)

You can get the library directly from PyPI:
On macOS:
```
python3 -m pip install -U discord.py
```
If you are using Windows, then the following should be used instead:
```
py -3 -m pip install -U discord.py
```

* 2. Install the menus extension of the discord.py module
```
py -3 -m pip install -U git+https://github.com/Rapptz/discord-ext-menus
```
If you don't have git, make sure to install it before the menus extension.

* 3. Setup dotenv for token feeding

a. Install python-dotenv
macOS:
```
python3 -m pip install python-dotenv
```
Windows:
```
py -3 -m pip install python-dotenv
```
b. Create a `.env` file in the root directory
This must be in the same directory as `__main__.py`

d. Insert in your token
~~~
TOKEN="YOUR_TOKEN"
~~~


