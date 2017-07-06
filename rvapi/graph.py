
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity


class Graph(Entity):
    """A graph entity"""
    def __init__(self, parent):
        self._identifier = self.unique_id("graph")
        super(Graph, self).__init__(parent)
        pyrvapi.rvapi_add_loggraph(self._identifier, self._parent.identifier, 0, 0, 1, 1)


class GraphData(Entity):
    """A graph data entity"""
    def __init__(self, parent, title):
        self._identifier = parent._identifier + "/" + self.unique_id("graphData")
        super(GraphData, self).__init__(parent)
        self._title = title
        pyrvapi.rvapi_add_graph_data1(self._identifier, self._title)


class GraphDataset(Entity):
    """A graph dataset"""
    def __init__(self, parent, title, description):
        self._identifier = parent._identifier + "/" + self.unique_id("graphDataset")
        super(GraphDataset, self).__init__(parent)
        self._description = description
        self._title = title
        pyrvapi.rvapi_add_graph_dataset1(self._identifier, self._title, self._description)

    @rvapi_flush
    def add_int(self, i):
        """Add an integer value to the graph

        Parameters
        ----------
        i : int
           The value to add

        """
        pyrvapi.rvapi_add_graph_int1(self._identifier, i)

    @rvapi_flush
    def add_real(self, i, f="%g"):
        """Add a real value to the graph

        Parameters
        ----------
        i : float
           The value to add
        f : string, optional
           The string formatter to use

        """
        pyrvapi.rvapi_add_graph_real1(self._identifier, i, f)

