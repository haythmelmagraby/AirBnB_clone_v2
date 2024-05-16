#!/usr/bin/python3
"""Module deletes out-of-date archives"""

import os
from fabric.api import *
env.hosts = ['35.153.232.112', '52.201.211.181']


def do_clean(n=0):
    """do clean"""
    if int(n) == 0:
        n = 1

    arch = sorted(os.listdir("versions"))
    [arch.pop() for i in range(n)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arch]

    with cd("/data/web_static/releases"):
        archs = run("ls -tr").split()
        archs = [f for f in archs if "web_static_" in f]
        [archs.pop() for i in range(n)]
        [run("rm -rf ./{}".format(f)) for f in archs]
