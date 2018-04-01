import os
from IPython.lib import passwd

c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python2'
c.NotebookApp.password = 'sha1:3ffd63062d92:22280c10308262be6f55ab2b0f89d9b31b70be75'
