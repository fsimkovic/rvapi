
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

__author__ = “Felix Simkovic”
__date__ = “06 Jul 2017”

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

