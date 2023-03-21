import sys
import os
from pathlib import Path
from ebooklib import epub
from gtts import gTTS

if len(sys.argv) < 3:
    print("Please provide an EPUB filename and number of words as arguments")
    sys.exit()

filename = sys.argv[1]
file_path = Path(filename).resolve()

book = epub.read_epub(file_path)
book_html = book.EpubHtml

text = book_html.get_body_content()

num_words = int(sys.argv[2])
file_content_words = text.split()[:num_words]
file_content_short = " ".join(file_content_words)

tts = gTTS(text=file_content_short, lang='en')
mp3_path = os.path.splitext(file_path)[0] + '.mp3'
tts.save(mp3_path)

print(f"MP3 file saved at: {mp3_path}")
