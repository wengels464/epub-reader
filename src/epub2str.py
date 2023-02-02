#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:08:02 2023

@author: william
"""

import collections.abc

# the update to Python 3.10 changed the way that imports work
# I had to add this ugly boilerplate to get around errors from the import
# scheme used by epub2txt, if the dev fixes this, flip the debugger off:

debug_collections = True

def debug_collections():
    collections.Iterable = collections.abc.Iterable
    collections.Mapping = collections.abc.Mapping
    collections.MutableMapping = collections.abc.MutableMapping
    collections.MutableSet = collections.abc.MutableSet
    collections.Callable = collections.abc.Callable
    return None

if debug_collections:
    debug_collections()
    
from epub2txt import epub2txt
from pathlib import Path

# Input Function

def get_title() -> str:
    title = input("Please enter the filename without .epub: ")
    return title

# User Variables

cwd = Path.cwd() # set cwd with Pathlib for greater interops
input_dir = cwd.parent / 'static' / 'input'
output_dir = cwd.parent / 'static' / 'output'
filetype_in = '.epub'
filetype_out = '.txt'


def title2filename(title: str, ftype: str) -> str:
    if ftype == '.epub' or ftype == '.txt': 
        return title + filetype_in
    else: 
        print("title2filename invalid ftype, options epub or txt")
        return None

def filename2path(filename: str, ftype: str) -> Path:
    if filename[-5:] == '.epub': # last 5 chars are .epub
        return input_dir / filename
    else: # is txt file
        return output_dir / filename

def get_epub_str(epub_path: Path) -> str:
    return epub2txt(epub_path)

def get_output_path(filename: str) -> Path:
    full_txt_filename = title + filetype_out # output is txt
    output_path = output_dir / full_txt_filename
    return output_path

def dump_epub_str(epub_str: str, output_path: Path) -> None:
    with open(output_path, 'w') as fp:
        fp.write(epub_str)
    fp.close()
    return None

# Orchestration

def get_epub_path(title: str) -> Path:
    filename = title2filename(title, '.epub')
    epub_path = filename2path(filename, '.epub')
    return epub_path

def write_str_to_file(epub_str: str, filename: str) -> None:
    output_path = get_output_path(filename)
    dump_epub_str(epub_str, output_path)
    return None

if __name__ == '__main__':    
    title = get_title()
    epub_path = get_epub_path(title)
    epub_str = get_epub_str(epub_path)
    filename = title2filename(title, '.txt')
    write_str_to_file(epub_str, filename)
    print("Program complete!")

    