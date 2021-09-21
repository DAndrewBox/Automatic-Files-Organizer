from __const__ import EXTENSIONS, PATH
from shutil import move
from colorama import init, Fore, Back, Style

init()

### Print and messages
def print_warning(text: str) -> None:
    """ Prints a warning. """
    print(Style.DIM + Back.YELLOW + Fore.BLACK + "[/!\\] " + text)
    print(Style.RESET_ALL, end="")

def print_error(text: str) -> None:
    """ Prints an error. """
    print(Style.BRIGHT + Back.RED + Fore.WHITE + "[!] " + text)
    print(Style.RESET_ALL, end="")

def print_end() -> None:
    """ Print quit message. """
    print(Style.BRIGHT + Fore.BLACK + "You can close this prompt now", end="")
    input(". . .")
    exit()

def get_print_format(text: str) -> str:
    """ Returns a formated text with colours and styles. """
    return f"<{Fore.BLACK}{Style.BRIGHT}{text}{Style.NORMAL}{Fore.WHITE}>"

### File functions
def get_dir(file: str) -> str:
    """ Returns the directory associated to the file extension"""
    file_extension: str = file.suffix[1:].lower()

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
        print_warning(f"Folder {path_to} does not exists!")
        print(f"{Fore.GREEN}Creating folder <{path_to}>...")
        path_to.mkdir()

    print(f"{Fore.WHITE}Moving file {get_print_format(path_abs.name)} to {get_print_format(path_to)}.")
    move(str(path_abs), str(path_to))