#!/usr/bin/env ccp4-python

# Creating a document
from rvapi import Document
main = Document("GUI", "jsrview", "Main")

# Create a tab
from rvapi import Tab
tab = Tab(main, "Summary Tab", opened=True) 
tab.add_text("hello World")

# Create a section
from rvapi import Section
section = Section(tab, "Summary Section", opened=True)
section.add_text("Hello World")

# Create a table in the tab
from rvapi import Table
table = Table(tab, "Summary Table")
table.add_col_header("one,two,three".split(","))
table.add_row("1,2,3".split(","))
table.add_row("3,4,5".split(","))

# Create a section with a tab
section2 = Section(tab, "Summary Section 2", opened=True)
table2 = Table(section2, "Summary Table 2")
table2.add_col_header("one,two,three".split(","))
table2.add_row("1,2,3".split(","))
table2.add_row("3,4,5".split(","))

#Add something to the previous table with time delay
import time
time.sleep(5)
table.add_row("10,11,12".split(","))

# Add some data to the section
from rvapi import Data
data = Data(section2, "Example File")
data.add_data("foobar.txt", "text")

# Another example of a PDB file
data2 = Data(tab, "Some Structure", opened=True)
data2.add_data("structure.pdb", "xyz")

# Add a tree
from rvapi import Tree
tree = Tree(section2, "Tree Example", opened=True)
Section(tree, "Section 1").set_tree_node()
tree_section2 = Section(tree, "Section 2")
tree_section2.set_tree_node()
tree_section2a = Section(tree, "Section 2a")
tree_section2a.set_tree_node(parent_node=tree_section2)
tree_section2b = Section(tree, "Section 2b")
tree_section2b.set_tree_node(parent_node=tree_section2)
# Add some text to the tree sections
for i, section in enumerate(tree):
    section.add_text("Hello World {}".format(i))

# Adding a radar figure
from rvapi import Radar
tab2 = Tab(main, "Figure Tab")
radar = Radar(tab2, "What's the best?", opened=False)
radar.add_property("Option 1", 0.1)
radar.add_property("Option 2", 0.2)
radar.add_property("Option 3", 1.0)

# Adding a plot figure
from rvapi import Graph, GraphData, GraphDataset, GraphPlot
graph = Graph(tab2)
graph_data = GraphData(graph, "Trigonometry")
dataset1 = GraphDataset(graph_data, "x", "argument")
dataset2 = GraphDataset(graph_data, "sin(x)", "Sine")
dataset3 = GraphDataset(graph_data, "cos(x)", "Cosine")
# Add some data to the plot
from math import sin, cos
for i in range(1, 21):
    dataset1.add(i)
    dataset2.add(sin(i*6.28/19.0))
    dataset3.add(cos(i*6.28/19.0))
# Add the plot
gplot = GraphPlot(graph, "Test", "X-label here", "y-label here")
from pyrvapi import *
rvapi_add_plot_line1(
    graph_data.identifier + "/" + gplot.identifier.rsplit("/")[-1], 
    dataset1.identifier.rsplit("/")[-1], 
    dataset2.identifier.rsplit("/")[-1]
)

