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

from .decorator import rvapi_flush
from .entity import Entity


class Table(Entity):

    def __init__(self, parent, title, column_sort_index=None, opened=False):
        self._identifier = parent.identifier + "/" + self.unique_id("table")
        super(Table, self).__init__(parent)

        self._content = []
        self._opened = opened
        self._column_sort_index = column_sort_index 
        self._title = title

        pyrvapi.rvapi_add_table1(self._identifier, self._title, 1, 0, 1, 1, self._opened) 

    @property
    def nrows(self):
        return len(self._content)

    @property
    def column_sort_index(self):
        return self._column_sort_index

    @column_sort_index.setter
    def column_sort_index(self, column_sort_index):
        self._column_sort_index = column_sort_index

    @rvapi_flush
    def add_col_header(self, header, description=None):
        if description and len(header) != len(description):
            raise ValueError("Header and descriptions do not match in length")
        identifier = self._identifier.split("/")[1]
        for i, h in enumerate(header):
            desc = description[i] if description else "" 
            pyrvapi.rvapi_put_horz_theader(identifier, h, desc, i)

    @rvapi_flush
    def add_row_header(self, header, description=None):
        if description and len(header) != len(description):
            raise ValueError("Header and descriptions do not match in length")
        identifier = self._identifier.split("/")[1]
        for j, h in enumerate(header):
            desc = description[i] if description else ""
            pyrvapi.rvapi_put_vert_theader(identifier, h, desc, j)
    
    @rvapi_flush
    def add_row(self, row):
        identifier = self._identifier.split("/")[1]
        self._content += [row]
        self._update_table()

    @rvapi_flush
    def insert_row(self, index, row):
        identifier = self._identifier.split("/")[1]
        self._content.insert(index, row)
        self._update_table()

    @rvapi_flush
    def edit_cell(self, i, j, content):
        if i > len(self._content):
            raise ValueError("Row index not defined in table")
        elif j > len(self._content[i]):
            raise ValueError("Column index not defined in table")
        identifier = self._identifier.split("/")[1]
        self._content[i][j] = content
        self._update_table()

    def _update_table(self):
        identifier = self._identifier.split("/")[1]
        if self._column_sort_index:
            self._sort_content()
        for i, row in enumerate(self._content):
            for j, cell_content in enumerate(row):
                pyrvapi.rvapi_put_table_string(identifier, str(cell_content), i, j)

    def _sort_content(self):
        if self._column_sort_index > len(self._content[0]):
            raise ValueError("Column sort index out of range")
        self._content = sorted(self._content, key=lambda x: x[self._column_sort_index])

