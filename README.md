# Python Markdown Auto Direction

[![pypi](https://img.shields.io/pypi/v/markdown-autodirection.svg?style=flat)][pypi-url]
[![](https://img.shields.io/pypi/l/markdown-autodirection.svg?style=flat)][license-url]
[![](https://img.shields.io/pypi/dm/markdown-autodirection.svg?style=flat)][pypi-url]
[![Build Status](https://travis-ci.org/aliva/python-markdown-autodirection.svg?branch=master)][travis-url]

[pypi-url]: https://pypi.org/project/markdown-autodirection/
[license-url]: LICENSE
[travis-url]: https://travis-ci.org/aliva/python-markdown-autodirection

Adds `dir="auto"` attribute to paragraphs,
This will help browser to set text direction based on the content of current paragraphs

## Install

```
pip install markdown-autodirection
```

## Use

```python
text = "Text"
from markdown import markdown
html = markdown(text, extensions=['autodirection'])
print(html)
# <p dir="auto">Text</p>
```
