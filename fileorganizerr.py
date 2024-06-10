import os
import shutil
from datetime import datetime

# Function to create a directory if it does not exist
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to move files to a specified folder and print success message
def move_and_report(folderName, files):
    for file in files:
        # Move the file to the specified folder
        print(f"Moving {file} to {folderName}")  # Debug print statement
        shutil.move(file, os.path.join(folderName, os.path.basename(file)))
    print(f"Files have been moved to {folderName} successfully")

# List of all files in the current directory, excluding directories
files = [f for f in os.listdir() if os.path.isfile(f)]
files.remove(os.path.basename(__file__))  # Exclude the script file itself

# Creating necessary directories
createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Movies')
createIfNotExist('Music')
createIfNotExist('Torrents')
createIfNotExist('Others')
createIfNotExist('Software')
createIfNotExist('Compressed')

# Categorizing files based on their extensions
imgExts = [".png", ".jpg", ".jpeg", ".gif", ".heic", ".bmp", ".ico", ".svg", ".webp"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".txt", ".docx", ".doc", ".pdf", ".xlsx", ".pptx", ".ppt", ".xls", ".csv", ".rtf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

movieExts = [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv", ".m4v", ".3gp", ".mpeg", ".mpg", ".webm", ".vob"]
movies = [file for file in files if os.path.splitext(file)[1].lower() in movieExts]

musicExts = [".mp3", ".wav", ".aac", ".wma", ".ogg", ".flac", ".m4a", ".opus"]
music = [file for file in files if os.path.splitext(file)[1].lower() in musicExts]

torrentExts = [".torrent", ".magnet"]
torrents = [file for file in files if os.path.splitext(file)[1].lower() in torrentExts]

softwareExts = [".exe", ".msi", ".dmg", ".app", ".bat", ".sh"]
software = [file for file in files if os.path.splitext(file)[1].lower() in softwareExts]

compressedExts = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".z"]
compressed = [file for file in files if os.path.splitext(file)[1].lower() in compressedExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in movieExts) and (ext not in musicExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in torrentExts) and (ext not in softwareExts) and (ext not in compressedExts) and os.path.isfile(file):
        others.append(file)

# Moving categorized files into their respective directories and printing success messages
move_and_report("Images", images)
move_and_report("Docs", docs)
move_and_report("Movies", movies)
move_and_report("Music", music)
move_and_report("Torrents", torrents)
move_and_report("Others", others)
move_and_report("Software", software)
move_and_report("Compressed", compressed)
