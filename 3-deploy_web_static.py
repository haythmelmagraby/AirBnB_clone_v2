#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import put, run, env
from os.path import exists
from datetime import datetime

env.hosts = ['35.153.232.112', '52.201.211.181']


def do_pack():
    """store the path of the created archive"""
    try:
        d = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fn = "versions/web_static_{}.tgz".format(d)
        local("tar -cvzf {} web_static".format(fn))
        return fn
    except:
        return None

def do_deploy(arch_path):
    """distributes the archive"""
    if exists(arch_path) is False:
        return False
    try:
        file_name = arch_path.split("/")[-1]
        notExit = file_n.split(".")[0]
        p = "/data/web_static/releases/"
        put(arch_path, '/tmp/')
        run('mkdir -p {}{}/'.format(p, notExit))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, p, notExit))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(p, notExit))
        run('rm -rf {}{}/web_static'.format(p, notExit))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(p, notExit))
        return True
    except:
        return False

def deploy():
    """distributes the archive"""
    arch_path = do_pack()
    if arch_path is None:
        return False
    return do_deploy(arch_path)
