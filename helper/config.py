#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("22606849", cast=int)
    API_HASH = config("ef85493cd32eadcb5309b5957d8d1b86")
    BOT_TOKEN = config("7279728762:AAGOel3zhLLYa5x0v9EOFHmzjvDQ9dmgfV4")
    OWNER = config("6440021089", default=1322549723, cast=int)
    LOG = config("-1002134572304", cast=int)
except Exception as e:




    
