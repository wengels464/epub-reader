# EPUB Reader (In Development)

## Project Description
A utility that uses PaddlePaddle to convert EPUBs into MP3 Audiobooks with several voice models.

## Rationale

Audiobooks are extraordinarily expensive, and EPUBs represent the best and most modern format for electronic books.

Therefore, we should be able to create rudimentary audiobooks using DNNs and voice models for free, without paying for expensive APIs or relying on bad concatenative converters.

## Intended Use Cases

- As a Calibre plugin.
- As a standalone, extensible epub-to-audiobook utility.
- As a way to use a different/more suitable voice than one provided commercially.

## Future Features
- PDF Support.
- Ability to divide by chapter.
- User trainable voice model.

## To-Do's:
- Find a (edge-tolerant) way to convert epubs to plaintext, excluding metadata and non-textual content.
- Train a few (~2-3) models with different voice prints using CC-licensed audiobooks with corresponding Public Domain text.
- Run those voice models against the standardized text and create chapters.
- Export those chapters using ffmpeg to MP3 (VBR, Q3) or Opus.
- Embed the relevant metadata (author, title, chapter number, chapter name) into the ID3 tag of those files.

## Specific Packaages Used
- PaddlePaddle
- epub2txt
- ffmpeg
