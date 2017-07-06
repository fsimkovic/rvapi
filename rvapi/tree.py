
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity


class Tree(Entity):

    def __init__(self, parent, title, opened=False):
        self._identifier = self.unique_id("tree")
        super(Tree, self).__init__(parent)
        self._title = title
        self._opened = opened
        pyrvapi.rvapi_add_tree_widget(
            self._identifier, self._title, self._parent.identifier, 
            0, 0, 1, 1
        )

