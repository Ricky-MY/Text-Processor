# Text Processor

## Table of Contents

1. [General Info](#general-info)
2. [Documentation](#documentation)
3. [Installation](#Installation)

### General Info

This is an API to process `.txt` files.

### Documentation

Text Processor is an API written in python to process `.txt` files.

**Quick Startup to find words**:

```python
from textprocessor import TextProcessor

with TextProcessor('yourtextfile.txt') as ctx:
    ctx.render_lines()
    words = ctx.find_word("hello")
    print(words)
```

**Don't do this**:

```python
from textprocessor import TextProcessor

ctx = TextProcessor('yourtextfile.txt')
ctx.render_lines()
```

### Methods

| Common Methods                            | Purpose                               |
| ----------------------------------------- | ------------------------------------- |
| [render_lines](#render_lines(notation)) | Reading the file                      |
| [get_links](#get_links(hint))           | Filter out all links in the text file |
| [get_images](#get_images(hint))         | Get all images in the text file       |
| [get_videos](#get_videos(hint))         | Get all videos in the text file       |
| [get_outcasts](#get_outcasts(hint))     | Get all alienated links               |
| [find_word](#find_words(*kword))        | To get statistics of key words        |
| [save](#save(header,destination))       | Save scrapped data into a json file   |

### class TextProcessor
    
<hr WIDTH="100%" SIZE="1" align="center" noshade>
<span>

#### render_lines(notation)

**Parameters**:
<br>

- **notation** - A character that you will use to render lines in. It is encouraged to leave this open for proper rendering.
</br>
</span>
<hr width="100%" size="1" align="center">
<span>

#### get_links(hint)

**Parameters**:
<br>

- **hint** - An argument string of the website protocol and the domain.
</br>
</span>
<hr width="100%" size="1" align="center">
<span>

#### get_images(hint)

**Parameters**:
<br>

- **hint** - An argument string of the website protocol and the domain.
</br>
</span>
<hr width="100%" size="1" align="center">
<span>

#### get_videos(hint)

**Parameters**:
<br>

- **hint** - An argument string of the website protocol and the domain.
</br>

_Example_:

```python
from textprocessor import TextProcessor

with TextProcessor('yourtextfile.txt') as ctx:
    ctx.render_lines()
    words = ctx.get_videos("https://youtube.com/")
    print(words)
```
</span>
<hr width="100%" size="1" align="center">
<span>

#### get_outcasts(hint)

**Parameters**:
<br>

- **hint** - An argument string of the website protocol and the domain.
</br>
</span>
<hr width="100%" size="1" align="center">
<span>

#### find_word(\*kword)

**Parameters**:

- **\*kword** - An argument list or a string of key-word(s) that the algorithm searches for in the word.
</span>
<hr width="100%" size="1" align="center">
<span>

#### save(header,destination)

**Parameters**:

- **header** - The main key that all the scrapped data sets will be under.
- **destination** - The path of the output .json file.
</span>
<hr width="100%" size="1" align="center">

### Wordy Explanation

...

### Installation

Use pip to install:

You can get the library directly from PyPI:
<br>
On macOS:

```
python3 -m pip install -U textprocessor
```

If you are using Windows, then the following should be used instead:

```
py -3 -m pip install -U textprocessor
```
