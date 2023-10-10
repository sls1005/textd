# Text Decoder

Is "А" (by its code point) a Latin alphabet, or a Greek Alpha?
Is "ー" a Chinese letter, a Bopomofo, or a Kana long-vowel sign?

In the age of Unicode, it has become harder to distinguish between those characters of different code points.
Sometimes it doesn't matter, but sometimes it does, because we have to check if the character usage is correct, or because we want to ensure that a URL can be trusted.

Here is a simple tool that can display the code point(s) of the input text, so that you'll know if two similar characters are same.

### Requirements

+ Python 3 or later

### Usage

Use stdin as input:
```sh
python textd.py
```
Specify a file and its encoding ("Latin-1" in this example):
```sh
python textd.py -f file.txt -e Latin-1
```
Decode the file but do not show the Unicode points:
```sh
python textd.py -f file.txt -e Latin-1 --no-codepoint
```

