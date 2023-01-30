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

title = get_title()

# User Variables

cwd = Path.cwd() # set cwd with Pathlib for greater interops
input_dir = cwd.parent / 'static' / 'input'
output_dir = cwd.parent / 'static' / 'output'
filetype_in = '.epub'
filetype_out = '.txt'




def title2filename(title: str, ftype: str) -> None:
    if ftype == 'epub': 
        filename_epub = title + filetype_in
        return None
    elif ftype == 'txt':
        filename_txt = title + filetype_out
        return None
    else: 
        print("Invalid ftype provided, options epub or txt")
        return None

def filename2path(filename: str, ftype: str) -> Path:
    if ftype == 'epub':
        epub_path = input_dir / filename_epub
        return None
    else:
        txt_path = output_dir / filename_txt

def epub2str(epub_path: Path) -> str:
    return epub2txt(epub_path)

def get_output_path(filename: str) -> Path:
    full_txt_filename = title + filetype_out
    output_path = output_dir / full_txt_filename
    return output_path

def dump_epub_str(epub_str: str) -> None:
    output_path = get_output_path(filename_txt)
    with open(output_path, 'w') as fp:
        fp.write(epub_str)
    fp.close()
    return None

def set_paths() -> None:
    title2filename(title, 'epub')
    title2filename(title, 'txt')
    
    filename2path(filename_epub, 'epub')
    filename2path(filename_txt, 'txt')

if __name__ == '__main__':
    
    set_paths() # where everything is, where it will go
    str_out = epub2str(epub_path)
    dump_epub_str(str_out)
    