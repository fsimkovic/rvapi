
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

