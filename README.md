
# OO-Interface to the pyrvapi.so file in CCP4

1. Creating a document
```python
from rvapi import GuiDocument
main = GuiDocument("GUI", "jsrview", "Main")
```

2. Create a tab
```python
from rvapi import Tab
tab = Tab(main, "Summary Tab", opened=True) 
tab.add_text("hello World")
```

3. Create a section
```python
from rvapi import Section
section = Section(tab, "Summary Section", opened=True)
section.add_text("Hello World")
```

4. Create a table in the tab
```python
from rvapi import Table
table = Table(tab, "Summary Table")
table.add_col_header("one,two,three".split(","))
table.add_row("1,2,3".split(","))
table.add_row("3,4,5".split(","))
```

5. Create a section with a tab
```python
section2 = Section(tab, "Summary Section 2", opened=True)
table2 = Table(section2, "Summary Table 2")
table2.add_col_header("one,two,three".split(","))
table2.add_row("1,2,3".split(","))
table2.add_row("3,4,5".split(","))
```
Add something to the previous table with time delay
```python
import time
time.sleep(5)
table.add_row("10,11,12".split(","))
```

6. Add some data to the section
```python
from rvapi import Data
data = Data(section2, "Example File")
data.add_data("foobar.txt", "text")
```
Another example of a PDB file
```python
data2 = Data(tab, "Some Structure", opened=True)
data2.add_data("structure.pdb", "xyz")
```

7. Add a tree
```python
from rvapi import Tree
tree = Tree(section2, "Tree Example", opened=True)
Section(tree, "Section 1").set_tree_node()
tree_section2 = Section(tree, "Section 2")
tree_section2.set_tree_node()
tree_section2a = Section(tree, "Section 2a")
tree_section2a.set_tree_node(parent_node=tree_section2)
tree_section2b = Section(tree, "Section 2b")
tree_section2b.set_tree_node(parent_node=tree_section2)
```
Add some text to the tree sections
```python
for i, section in enumerate(tree):
    section.add_text("Hello World {}".format(i))
```

8. Adding a radar figure
```python
from rvapi import Radar
tab2 = Tab(main, "Figure Tab")
radar = Radar(tab2, "What's the best?", opened=True)
radar.add_property("Option 1", 0.1)
radar.add_property("Option 2", 0.2)
radar.add_property("Option 3", 1.0)
```

9. Adding a plot figure
```python
from rvapi import Graph, GraphData, GraphDataset
graph = Graph(tab2)
graph_data = GraphData(graph, "Trigonometry")
dataset1 = GraphDataset(graph_data, "x", "argument")
dataset2 = GraphDataset(graph_data, "sin(x)", "Sine")
dataset3 = GraphDataset(graph_data, "cos(x)", "Cosine")
```
Add some data to the plot
```python
from math import sin, cos
for i in range(1, 21):
    dataset1.add_int(i)
    dataset2.add_real(sin(i*6.28/19.0))
    dataset3.add_real(cos(i*6.28/19.0))

