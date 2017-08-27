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
"""OO-Interface to `pyrvapi.so` file in CCP4

Examples
--------

1. Creating a document

.. code-block:: python

   from rvapi import GuiDocument
   main = GuiDocument("GUI", "jsrview", "Main")

2. Create a tab

.. code-block:: python

   from rvapi import Tab
   tab = Tab(main, "Summary Tab", opened=True)
   tab.add_text("hello World")

3. Create a section

.. code-block:: python

   from rvapi import Section
   section = Section(tab, "Summary Section", opened=True)
   section.add_text("Hello World")


4. Create a table in the tab

.. code-block:: python

   from rvapi import Table
   table = Table(tab, "Summary Table")
   table.add_col_header("one,two,three".split(","))
   table.add_row("1,2,3".split(","))
   table.add_row("3,4,5".split(","))


5. Create a section with a tab

.. code-block:: python

   section2 = Section(tab, "Summary Section 2", opened=True)
   table2 = Table(section2, "Summary Table 2")
   table2.add_col_header("one,two,three".split(","))
   table2.add_row("1,2,3".split(","))
   table2.add_row("3,4,5".split(","))

Add something to the previous table with time delay

.. code-block:: python

   import time
   time.sleep(5)
   table.add_row("10,11,12".split(","))

6. Add some data to the section

.. code-block:: python

   from rvapi import Data
   data = Data(section2, "Example File")
   data.add_data("foobar.txt", "text")

Another example of a PDB file

.. code-block:: python

   data2 = Data(tab, "Some Structure", opened=True)
   data2.add_data("structure.pdb", "xyz")

7. Add a tree

.. code-block:: python

   from rvapi import Tree
   tree = Tree(section2, "Tree Example", opened=True)
   Section(tree, "Section 1").set_tree_node()
   tree_section2 = Section(tree, "Section 2")
   tree_section2.set_tree_node()
   tree_section2a = Section(tree, "Section 2a")
   tree_section2a.set_tree_node(parent_node=tree_section2)
   tree_section2b = Section(tree, "Section 2b")
   tree_section2b.set_tree_node(parent_node=tree_section2)

Add some text to the tree sections

.. code-block:: python

   for i, section in enumerate(tree):
       section.add_text("Hello World {}".format(i))

8. Adding a radar figure

.. code-block:: python

   from rvapi import Radar
   tab2 = Tab(main, "Figure Tab")
   radar = Radar(tab2, "What's the best?", opened=True)
   radar.add_property("Option 1", 0.1)
   radar.add_property("Option 2", 0.2)
   radar.add_property("Option 3", 1.0)


9. Adding a plot figure

.. code-block:: python

   from rvapi import Graph, GraphData, GraphDataset
   graph = Graph(tab2)
   graph_data = GraphData(graph, "Trigonometry")
   dataset1 = GraphDataset(graph_data, "x", "argument")
   dataset2 = GraphDataset(graph_data, "sin(x)", "Sine")
   dataset3 = GraphDataset(graph_data, "cos(x)", "Cosine")


Add some data to the plot

.. code-block:: python

   from math import sin, cos
   for i in range(1, 21):
       dataset1.add_int(i)
       dataset2.add_real(sin(i*6.28/19.0))
       dataset3.add_real(cos(i*6.28/19.0))

"""

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

