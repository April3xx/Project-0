from __future__ import print_function
from __future__ import division
import numpy as np
import platform
_is_python_2 = int(platform.python_version_tuple()[0]) == 2
m = '1' if _is_python_2 else '2000'
print(m)