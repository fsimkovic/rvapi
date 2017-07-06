
import os
import pyrvapi

from rvapi.decorator import rvapi_flush
from rvapi.entity import Entity 


class Document(Entity):
    
    CCP4_ENV = os.environ["CCP4"]
    SHARE_JSRVIEW = os.path.join(CCP4_ENV, "share", "jsrview")

    def __init__(self, identifier, jsrview_dir, title, mode=1, layout=7, help_fname=None, html_fname=None, task_fname=None, webserver_uri=None):
        super(Document, self).__init__(None)
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

