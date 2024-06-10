# File Organiser

## Description

This Python script organizes files in a specified directory into different folders based on their file extensions. It categorizes files into folders such as Images, Docs, Media, Torrents, and Others. Additionally, it moves files with specific extensions into folders with clear names, such as Images for .gif and .heic files, Docs for .xlsx files, Torrents for .torrent files, Software for .exe files, and Compressed for .zip and .rar files.

## How to Use

1. Place the script in the directory containing the files you want to organize.
2. Run the script.
3. The script will categorize and move the files into the respective folders based on their extensions.

## Dependencies

- Python 3.x
- `os` module
- `shutil` module
- `datetime` module

## Example

```bash
$ python file_organizer.py
