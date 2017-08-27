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
# FITNESS FOR A :obj:PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = "Felix Simkovic"
__date__ = "06 Jul 2017"
__version__ = "0.0dev1"


def Data(*args, **kwargs):
    """A :obj:`Data <.data.Data>` class"""
    from .data import Data
    return Data(*args, **kwargs)


def GuiDocument(*args, **kwargs):
    """A :obj:`GuiDocument <.document.GuiDocument>` class"""
    from .document import GuiDocument
    return GuiDocument(*args, **kwargs)


def MockDocument(*args, **kwargs):
    """A :obj:`MockDocument <.document.MockDocument>` class"""
    from .document import MockDocument
    return MockDocument(*args, **kwargs)


def Graph(*args, **kwargs):
    """A :obj:`Graph <.graph.Graph>` class"""
    from .graph import Graph
    return Graph(*args, **kwargs)


def GraphData(*args, **kwargs):
    """A :obj:`GraphData <.graph.GraphData>` class"""
    from .graph import GraphData
    return GraphData(*args, **kwargs)


def GraphDataset(*args, **kwargs):
    """A :obj:`GraphDataset <.graph.GraphDataset>` class"""
    from .graph import GraphDataset
    return GraphDataset(*args, **kwargs)


def GraphPlot(*args, **kwargs):
    """A :obj:`GraphPlot <.graph.GraphPlot>` class"""
    from .graph import GraphPlot
    return GraphPlot(*args, **kwargs)


def Radar(*args, **kwargs):
    """A :obj:`Radar <.radar.Radar>` class"""
    from .radar import Radar
    return Radar(*args, **kwargs)


def Section(*args, **kwargs):
    """A :obj:`Section <.section.Section>` class"""
    from .section import Section
    return Section(*args, **kwargs)


def Tab(*args, **kwargs):
    """A :obj:`Tab <.tab.Tab>` class"""
    from .tab import Tab
    return Tab(*args, **kwargs)


def Table(*args, **kwargs):
    """A :obj:`Table <.table.Table>` class"""
    from .table import Table
    return Table(*args, **kwargs)


def Tree(*args, **kwargs):
    """A :obj:`Tree <.tree.Tree>` class"""
    from .tree import Tree
    return Tree(*args, **kwargs)

