
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity


class Radar(Entity):

    def __init__(self, parent, title, opened=False):
        self._identifier = self.unique_id("radar")
        super(Radar, self).__init__(parent)
        self._title = title
        self._opened = opened
        pyrvapi.rvapi_add_radar(self._identifier, self._title, self._parent.identifier, 1, 0, 1, 1, self._opened)
    
    @rvapi_flush
    def add_property(self, name, value):
        """Add a property to the radar plot

        Parameters
        ----------
        name : str
           The name of the property
        value : int, float
           The value of the property

        """
        pyrvapi.rvapi_add_radar_property(self._identifier, name, value)

