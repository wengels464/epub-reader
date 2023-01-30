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

# User Variables

cwd = Path.cwd() # set cwd with Pathlib for greater interops
input_dir = cwd.parent / 'static' / 'input'
output_dir = cwd.parent / 'static' / 'output'
filename = 'frankenstein' # the exact filename without file extension
filetype_in = '.epub'
filetype_out = '.txt'

# Temp Variables

demo_path = cwd.parent / 'demo' / 'frankenstein.epub'

# User Functions

def epub_exists(epub_path: Path) -> bool:
    return epub_path.suffix == '.epub'

def input2path(epub_str_path: str) -> Path:
    filename = epub_str_path + filetype_in
    full_path = input_dir / filename
    return full_path

def epub2str(epub_path: Path) -> str:
    return epub2txt(epub_path)

def get_output_path(filename: str) -> Path:
    full_filename = filename + filetype_out
    output_path = output_dir / full_filename
    return output_path

def export_to_UTF8(epub_text: str, output_dir: Path) -> None:
    full_filename = 
    export_path = output_dir / filename + filetype_out
    text_out = open(export_path, "w")
    text_out.write(epub_text)
    text_out.close()
    return None    

if __name__ == '__main__':
    target = input("Please enter the name of the book without .epub: ")
    input_epub_path = input2path(target)
    if epub_exists(input_epub_path):
        output_path = get_output_path(target)
        str_epub = epub2str(input_epub_path)
        
        export_to_UTF8(str_epub, output_path)
    else: print("EPUB Not Found!")
        
    

