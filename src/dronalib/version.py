"""
This module defines the version number string and tuple for this version of dronalib.
The project's ``pyproject.toml`` inspects this file for a version number.
"""


import re

__version__ = "0.0.1rc1"
version = __version__
version_info = tuple(re.split(r"[-\.]", __version__))

del re
