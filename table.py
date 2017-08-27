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


class Table(Entity):

    def __init__(self, parent, title, opened=False):
        self._identifier = parent.identifier + "/" + self.unique_id("table")
        super(Table, self).__init__(parent)

        self._nrows = 0
        self._title = title
        self._opened = opened

        pyrvapi.rvapi_add_table1(self._identifier, self._title, 1, 0, 1, 1, self._opened) 

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
        for j, e in enumerate(row):
            pyrvapi.rvapi_put_table_string(identifier, e, self._nrows, j)
        self._nrows += 1

