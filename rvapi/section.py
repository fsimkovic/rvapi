
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity


class Section(Entity):

    def __init__(self, parent, title, opened=False):
        self._identifier = self.unique_id("section")
        super(Section, self).__init__(parent)
        self._title = title
        self._opened = opened
        pyrvapi.rvapi_add_section(
            self._identifier, self._title, self._parent.identifier, 
            0, 0, 1, 1, self._opened
        )

    @rvapi_flush
    def add_content(self, content):
        pyrvapi.rvapi_append_content(content, True, self._identifier)

    @rvapi_flush
    def add_text(self, content):
        pyrvapi.rvapi_add_text(content, self._identifier, 0, 0, 1, 1)

    @rvapi_flush
    def set_tree_node(self, parent_node=None):
        parent_node_identifier = parent_node.identifier if parent_node else ""
        pyrvapi.rvapi_set_tree_node(self._parent.identifier, self._identifier, self._title, "auto", parent_node_identifier)

