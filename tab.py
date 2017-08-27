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
