
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity


class Tab(Entity):

    def __init__(self, parent, title, opened=False):
        self._identifier = self.unique_id("tab")
        super(Tab, self).__init__(parent)
        self._title = title
        self._opened = opened
        pyrvapi.rvapi_add_tab(self._identifier, self._title, self._opened)

    @rvapi_flush
    def add_content(self, content):
        pyrvapi.rvapi_append_content(content, True, self._identifier)

    @rvapi_flush
    def add_text(self, content):
        pyrvapi.rvapi_add_text(content, self._identifier, 0, 0, 1, 1)
