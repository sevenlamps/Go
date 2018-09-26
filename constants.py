import numpy as np
from typing import NewType, List, Set
from collections import namedtuple


uint = np.uint32
Color = NewType('Color', str)
Vertex = NewType('Vertex', str)
Move = NewType('Move', str)
Point = namedtuple('Point', 'x y')

