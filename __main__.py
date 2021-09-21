# Required
from __const__ import PATH, HAS_ARGS
from __func__ import print_error, print_end, get_dir, move_file

# Optionals
from time import time as timedelta
from win10toast import ToastNotifier

### Functions
def __main__() -> None:
    # Show Windows 10 notification
    toaster = ToastNotifier()
    toaster.show_toast( "Folder Organizer",
                    f"Organizing {PATH} files into folders...",
                    duration=7,
                    threaded=True
                    )
    # Do magic
    for file in PATH.iterdir():
        path_absolute = file.absolute()

        if file.is_file():
            directory_to: str = get_dir(file)
            destination_folder: Path = PATH / directory_to

            move_file(path_absolute, destination_folder)

### Main process
if __name__ == "__main__":
    if (not HAS_ARGS) or (PATH == None):
        print_error("You should drop a folder or pass it as argument on cmd!")
        print_end()

    time_ini: float = timedelta()
    __main__()
    time_end: float = timedelta()

    print(  "=" * 64,
            f"\nFinished on {(time_end - time_ini) * 1000} ms!"
        )

    print_end()