from sys import argv
from pathlib import Path
from shutil import move
from time import time as timedelta
from win10toast import ToastNotifier

# Check if path was called, if not, end the program.
if (len(argv) < 1):
    exit

# Setup constants
EXTENSIONS = {
    "Images" : ["png", "jpg", "jpeg", "bmp", "gif", "tiff", "webp"],
    "Videos" : ["mp4", "webm", "mkv", "mov", "flv", "3gp", "avi"],
    "Audio"  : ["mp3", "ogg", "wav", "flac", "mp2", "aif"],
    "Documents" : ["pdf", "doc", "docx", "txt", "ppt", "xls", "xlsx", "csv", "xml"],
    "Other" : {
        "Compressed": ["zip", "rar", "7z"],
        "GM-Engines" : ["gex", "gmx", "gmz", "gm8", "gmez", "gml", "gmk", "yyz", "yymp"]
    }
}

PATH = Path(argv[1]) # Path to organize folders

# Functions
def get_dir(file: str) -> str:
    """ Returns the directory associated to the file extension"""
    file_extension = file.suffix[1:].lower()
    for directory in EXTENSIONS.keys():
        if (isinstance(EXTENSIONS[directory], list)):
            if (file_extension in EXTENSIONS[directory]):
                return directory
        elif (isinstance(EXTENSIONS[directory], dict)):
            for subdir in EXTENSIONS[directory].keys():
                if (file_extension in EXTENSIONS[directory][subdir]):
                    return directory + "\\"  + subdir

    return "Other"

def move_file(path_abs: str, path_to: str) -> None:
    """ Move a file to a folder and create it if doesn't exists. """
    if not (path_to.exists()):
        print(f"Folder {path_to} does not exists!")
        print(f"Creating folder <{path_to}>...")
        path_to.mkdir()

    print(f"Moving from <{path_abs}> to <{path_to}>.")
    move(str(path_abs), str(path_to))

def __main__():
    # Show Windows 10 notification
    toaster = ToastNotifier()
    toaster.show_toast( "Folder Organizer",
                    f"Organizing {PATH} files into folders...",
                    duration=7,
                    threaded=True
                    )

    time_ini = timedelta()

    # Do magic
    for file in PATH.iterdir():
        path_absolute = file.absolute()

        if file.is_file():
            directory_to = get_dir(file)
            destination_folder = PATH / directory_to

            move_file(path_absolute, destination_folder)
            
    time_end = timedelta()

    print(f"Finished on {time_end - time_ini} seconds!")
    input("Press any key to exit . . .")

__main__()