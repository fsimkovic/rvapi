
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity


class Data(Entity):

    def __init__(self, parent, title, opened=False):
        self._identifier = parent.identifier + "/" + self.unique_id("data")
        super(Data, self).__init__(parent)
        self._title = title
        self._opened = opened

    @rvapi_flush
    def add_data(self, data, format):
        pyrvapi.rvapi_add_data1(self._identifier, self._title, data, format, 1, 0, 1, 1, self._opened) 

