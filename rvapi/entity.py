
import os
import uuid


class Entity(object):

    RESERVED_IDS = []

    def __init__(self, parent):
        self._parent = parent
        self._child_list = []
        self._child_dict = {}
        if parent:
            parent._add(self)

    def __contains__(self, identifier):
        return identifier in self._child_dict

    def __iter__(self):
        for e in self._child_list:
            yield e

    def __repr__(self):
        return "{}(identifier={})".format(self.__class__.__name__, self.identifier)

    def _add(self, child):
        if child.identifier in self.RESERVED_IDS:
            raise RuntimeError("Entity already present!")
        child._parent = self
        self._child_list += [child]
        self._child_dict[child.identifier] = child
        self.RESERVED_IDS += [child.identifier]
        return child

    @classmethod
    def absolute_path(cls, fname):
        if fname is None:
            return fname
        else:
            return os.path.abspath(fname)

    @classmethod
    def unique_id(cls, prefix):
        return prefix + str(uuid.uuid4())

    @property
    def identifier(self):
        return self._identifier

