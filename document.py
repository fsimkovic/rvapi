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

import os
import pyrvapi

from .decorator import rvapi_flush
from .entity import Entity 


class GuiDocument(Entity):
    
    CCP4_ENV = os.environ["CCP4"]
    SHARE_JSRVIEW = os.path.join(CCP4_ENV, "share", "jsrview")

    def __init__(self, identifier, jsrview_dir, title, mode=1, layout=7, help_fname=None, html_fname=None, task_fname=None, webserver_uri=None):
        super(GuiDocument, self).__init__(None)
        self._identifier = identifier
        self._title = title
        self._mode = mode
        self._layout = layout
        self._jsrview_dir = self.absolute_path(jsrview_dir)
        self._help_fname = self.absolute_path(help_fname)
        self._html_fname = self.absolute_path(html_fname)
        self._task_fname = self.absolute_path(task_fname)
        self._webserver_uri = None
        
        if not os.path.isdir(self._jsrview_dir):
            os.mkdir(self._jsrview_dir)
        
        pyrvapi.rvapi_init_document(
            self._identifier, self._jsrview_dir, self._title, self._mode, 
            self._layout, self.SHARE_JSRVIEW, self._help_fname, self._html_fname, 
            self._task_fname, None
        ) 
    
        if webserver_uri:
            self._webserver_start = len(jsrview_dir) + 1
        else:
            jsrview = os.path.join(self.CCP4_ENV, "libexec", "jsrview")
            if self._html_fname is None:
                self._html_fname = os.path.join(self._jsrview_dir, "index.html")
            import subprocess
            subprocess.Popen([jsrview, self._html_fname])
        
        pyrvapi.rvapi_add_header(title)
        self.refresh()
    
    @rvapi_flush
    def refresh(self):
        pass


class MockDocument(Entity):
    
    def __init__(self, *args, **kwargs):
        super(MockDocument, self).__init__(None)
    
    @rvapi_flush
    def refresh(self):
        pass

