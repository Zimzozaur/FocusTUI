import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from platformdirs import user_data_dir

#############################
#       Custom Types        #
#############################

VolumeType = Literal["alarm_volume", "signal_volume", "ambient_volume", "test_volume"]
SoundType = Literal["alarm", "signal", "ambient"]
LengthType = Literal["short", "long"]


#############################
#      Custom Settings      #
#############################

load_dotenv(override=True)

# is Debug mode on
FK_DEBUG: bool = os.getenv("FK_DEBUG") == "True"

# Number of seconds in a minute
_minute = os.getenv("FK_DEBUG_MINUTE")
is_custom = FK_DEBUG and _minute is not None
MINUTE: int = int(_minute) if is_custom else 60

# Min number of minutes that session has to take at minimum
_min_sessions_len = os.getenv("FK_DEBUG_MIN_SESSION_LEN")
is_custom = FK_DEBUG and _min_sessions_len is not None
MIN_SESSION_LEN = int(_min_sessions_len) if is_custom else 5
MAX_SESSION_LEN: int = 300


#############################
#      Default Settings     #
#############################

# Root
MAIN_DIR_PATH: Path = Path(user_data_dir()) / "focus-keeper"

# Sounds path
SOUNDS_PATH: Path = MAIN_DIR_PATH / "sounds"
SHORT_PATH: Path = SOUNDS_PATH / "shorts"
LONGS_PATH: Path = SOUNDS_PATH / "longs"

# Others
THEMES_PATH: Path = MAIN_DIR_PATH / "themes"
QUEUES_PATH: Path = MAIN_DIR_PATH / "queues"

# Files
DB_FILE_PATH: Path = MAIN_DIR_PATH / "focus_keeper.db"
CONFIG_FILE_PATH: Path = MAIN_DIR_PATH / "config.json"

# Default sounds
DEFAULT_ALARM_NAME: str = "Woohoo"
DEFAULT_SIGNAL_NAME: str = "Landing"
DEFAULT_AMBIENT_NAME: str = "Woodpecker_Forest"

# Reserved Sounds
RESERVED_SHORTS: set = {
    "Acid_Bassline.flac",
    "Braam.flac",
    "Landing_Forcefield.flac",
    "Woohoo.flac",
}
RESERVED_LONG: set = {"Mexican_Forest.wav", "Woodpecker_Forest.flac"}
RESERVED_ALL_SOUNDS: set = RESERVED_SHORTS | RESERVED_LONG

MIN_VOLUME_LEVEL: int = 1
MAX_VOLUME_LEVEL: int = 100

DEFAULT_CONFIG = {
    "alarm": {
        "name": DEFAULT_ALARM_NAME,
    },
    "signal": {
        "name": DEFAULT_SIGNAL_NAME,
    },
    "ambient": {
        "name": DEFAULT_AMBIENT_NAME,
    },
    "alarm_volume": 50,
    "signal_volume": 50,
    "ambient_volume": 50,
    "test_volume": 50,
    "session_length": 45,
}


DISCORD_INVITATION = "https://discord.gg/a2TyMhXQ"
PROJECT_GITHUB = "https://github.com/Zimzozaur/FocusKeeper-TUI"
SIMONS_X_ACCOUNT = "https://x.com/zimzozaur"
