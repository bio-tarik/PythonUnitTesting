"""
SOURCE: https://github.com/okken/markdown.py

 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re


def convert_strong(text):
    """
        Convert double asterisk or underscore pairs to strong tags
    """
    text = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*)__', r'<strong>\1</strong>', text)
    return text


def convert_em(text):
    """
        Convert single asterisk or underscore pairs to em tags
    """
    text = re.sub(r'\*(.*)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*)_', r'<em>\1</em>', text)
    return text


for line in fileinput.input():
    line = line.rstrip()
    line = convert_strong(line)
    line = convert_em(line)
    print('<p>' + line + '</p>')
