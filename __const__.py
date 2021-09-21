from sys import argv
from pathlib import Path

### Check if arguments has been passed into
HAS_ARGS: bool = True

try:
    print(f"Starting work on <{argv[1]}>")
    print("=" * 64)
except Exception:
    HAS_ARGS: bool = False

### Setup constants
# Path to organize folders
PATH: Path = Path(argv[1]) if HAS_ARGS else None

# Extensions for every folder and subfolder
EXTENSIONS: dict = {
    "Images" : ["png", "jpg", "jpeg", "bmp", "gif", "tiff", "webp", "svg"],
    "Videos" : ["mp4", "webm", "mkv", "mov", "flv", "3gp", "avi"],
    "Audio"  : {
        "Songs" : ["mp3", "ogg", "flac", "mp2", "aif"],
        "SFX"   : ["wav"],
        "MIDI"   : ["mid", "xm", "mod", "sid", "tm8", "s3m", "it"]
    },
    "Documents" : {
        "PDF"   : ["pdf"],
        "Word"  : ["doc", "docx"],
        "Excel" : ["xls", "xlsx", "csv"],
        "Text"  : ["txt", "xml"],
        "PPT"   : ["ppt"]
    },
    "Other" : {
        "Compressed": ["zip", "rar", "7z"],
        "GM-Engines" : ["gex", "gmx", "gmz", "gm8", "gmez", "gml", "gmk", "yyz", "yymp"]
    }
}