#!/usr/bin/python3
"""Module generates archive"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """generates archive """
    time_now = datetime.now()
    arch = 'web_static_' + time_now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    f = local('tar -cvzf versions/{} web_static'.format(arch))
    if f is not None:
        return arch
    else:
        return None
