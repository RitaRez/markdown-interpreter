# Markdown Interpreter

A simple _markdown_ interpreter made with python 3, [Tkinter](https://docs.python.org/3/library/tkinter.html), [tkhtmlview](https://pypi.org/project/tkhtmlview/) and _a lot_ of regex. Hosted with [github pages](http://ritarez.github.io/markdown-interpreter/)

Contributors
------------
- [Alexis Mariz](https://github.com/Adgmariz)
- [Luiz Philippe Pereira Amaral](https://github.com/luizppa)
- [Pedro Henrique Andrade](https://github.com/carbo6ufmg)
- [Rita Rezende Borges de Lima](https://github.com/RitaRez)


Installing
-------------
```pip3 install -r requirements.txt```

## Usage

Run the file _olf_main.py_ passing as argument the path to a markdown file, and optionally, a path to an output file. If the output file name is provided a HTML file well be created at the given location, otherwise, the markdown will be rendered in the tkinter window.

> Notice: The used library, tkhtmlview, does not support a lot of HTML features, therefore the tkinter rendered content might differ from what you would see in a web browser.

### Example:

```python3 main.py markdown-file.md```

You can also use the [hosted](http://ritarez.github.io/markdown-interpreter/) version with a simple interface, write your markdown on the text area click on preview and watch as the magic happens :)
