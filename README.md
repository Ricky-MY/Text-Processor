# Text Processor

## Table of Contents
1. [General Info](#general-info)
2. [Documentation](#documentation)
3. [Installation](#how-can-i-run-this-project)

### General Info
This is an API to process `.txt` files.

### Documentation
Text Processor is an API written in python to process `.txt` files.

Quick Startup to find words:
```python
from textprocessor import TextProcessor

with TextProcessor('yourtextfile.txt') as ctx:
    ctx.render_lines()
    words = ctx.find_word("hello")
    print(words)
```
### Methods
Common Methods | Purpose
------------ | -------------
[render_lines](#render_lines) | Reading the file
[get_links](#get_links) | Filter out all links in the text file
[get_images](#get_images) | Get all images in the text file
[get_videos](#get_videos) | Get all videos in the text file
[get_outcasts](#get_outcasts) | Get all alienated links
[find_word](#find_words) |  To get statistics of key words
[save](#save) | Save scrapped data into a json file

#### render_lines(notation)
__Parameters__:
<br>***notation** - A character that you will use to render lines in. It is encouraged to leave this open for proper rendering.</br>

#### get_links(hint)
__Parameters__:
<br>
**hint** - An argument string of the website protocol and the domain.
</br>

#### get_images(hint)
__Parameters__:
<br>
**hint** - An argument string of the website protocol and the domain.
</br>

#### get_videos(hint)
__Parameters__:
<br>
**hint** - An argument string of the website protocol and the domain.
</br>

#### get_outcasts(hint)
__Parameters__:
<br>
**hint** - An argument string of the website protocol and the domain.
</br>

#### find_word(*kword)
__Parameters__:
<br>
***kword** - An argument list or a string of key-word(s) that the algorithm searches for in the word.
</br>

#### save(header, destination)
__Parameters__:
<br>
**header** - The main key that all the scrapped data sets will be under.
**destination** - The path of the output .json file.
</br>

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

**That is all you need to run this project. If you want to try out a pre-hosted bot, please navigate to this website https://top.gg/bot/768442873561481216** 

