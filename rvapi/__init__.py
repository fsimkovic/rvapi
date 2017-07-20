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
    """A :obj:`Data <rvapi.data.Data>` class"""
    from rvapi.data import Data
    return Data(*args, **kwargs)


def Document(*args, **kwargs):
    """A :obj:`Document <rvapi.document.Document` class"""
    from rvapi.document import Document
    return Document(*args, **kwargs)


def Graph(*args, **kwargs):
    """A :obj:`Graph <rvapi.graph.Graph>` class"""
    from rvapi.graph import Graph
    return Graph(*args, **kwargs)


def GraphData(*args, **kwargs):
    """A :obj:`GraphData <rvapi.graph.GraphData>` class"""
    from rvapi.graph import GraphData
    return GraphData(*args, **kwargs)


def GraphDataset(*args, **kwargs):
    """A :obj:`GraphDataset <rvapi.graph.GraphDataset>` class"""
    from rvapi.graph import GraphDataset
    return GraphDataset(*args, **kwargs)


def GraphPlot(*args, **kwargs):
    """A :obj:`GraphPlot <rvapi.graph.GraphPlot>` class"""
    from rvapi.graph import GraphPlot
    return GraphPlot(*args, **kwargs)


def Radar(*args, **kwargs):
    """A :obj:`Radar <rvapi.radar.Radar>` class"""
    from rvapi.radar import Radar
    return Radar(*args, **kwargs)


def Section(*args, **kwargs):
    """A :obj:`Section <rvapi.section.Section>` class"""
    from rvapi.section import Section
    return Section(*args, **kwargs)


def Tab(*args, **kwargs):
    """A :obj:`Tab <rvapi.tab.Tab>` class"""
    from rvapi.tab import Tab
    return Tab(*args, **kwargs)


def Table(*args, **kwargs):
    """A :obj:`Table <rvapi.table.Table>` class"""
    from rvapi.table import Table
    return Table(*args, **kwargs)


def Tree(*args, **kwargs):
    """A :obj:`Tree <rvapi.tree.Tree>` class"""
    from rvapi.tree import Tree
    return Tree(*args, **kwargs)

