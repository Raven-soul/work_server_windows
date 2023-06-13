#
#  temp.py
#  development of an online flower shop
#
#  Created by Artem Kozyrev on 19.04.2023.
#

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

print(os.path.join(BASE_DIR, 'flower/'))