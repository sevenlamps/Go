from math import sqrt, log
from utility import *
from go import *


UCT_CONSTANT: float = 0.0


class Node(object):
    def __init__(self, parent=None, child=None):
        self.parent: Node = parent
        self.child: List[Node] = child
        self.num_of_visit: int = 0

    def select_uct_child(self):
        return 

