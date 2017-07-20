# MIT License
# 
# Copyright (c) 2017 Felix Simkovic
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = "Felix Simkovic"
__date__ = "06 Jul 2017"

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
    def add(self, value):
        """Add a value to the graph

        Parameters
        ----------
        value : int, float
           The value to add

        """
        if isinstance(value, int):
            pyrvapi.rvapi_add_graph_int1(self._identifier, value)
        else:
            pyrvapi.rvapi_add_graph_real1(self._identifier, value, "%g")


class GraphPlot(Entity):

    def __init__(self, parent, title, xlabel=None, ylabel=None):
        self._identifier = parent._identifier + "/" + self.unique_id("graphPlot")
        super(GraphPlot, self).__init__(parent)
        self._title = title
        self._xlabel = xlabel
        self._ylabel = ylabel
        pyrvapi.rvapi_add_graph_plot1(self._identifier, self._title, self._xlabel, self._ylabel)

