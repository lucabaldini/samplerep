# Copyright (C) 2023 luca.baldini@pi.infn.it
#
# For the license terms see the file LICENSE, distributed along with this
# software.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""General utilities.
"""

from typing import Union

import numpy as np


def square(value : Union[int, float, np.ndarray]) -> Union[float, np.ndarray]:
    """Return the square of a given number.

    This will accept any imput that support the ** operators, including
    integers, floating point numbers and numpy array.

    The function will raise a TypeError for incompatible types (e.g.,
    string).

    Arguments
    ---------
    value : number
        The input value to square.

    Return
    ------
        The square of the input value. : float
    """
    return value**2.
