
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity


class Graph(Entity):

    def __init__(self, parent):
        self._identifier = self.unique_id("graph")
        super(Graph, self).__init__(parent)
        pyrvapi.rvapi_add_loggraph(self._identifier, self._parent.identifier, 1, 0, 1, 1)

