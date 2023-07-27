#!/usr/bin/python3
from os import path
from datetime import date
from time import strftime
from fabric.api import put, run, local, env

env.hosts = ["54.160.101.122", "54.237.51.149"]


def do_pack():
    """
    Will generate a .tgz archive form contents of web_static
    folder of my repo (this one)
    """

    f_name = strftime('%Y%m%d%H%M%S')
    try:
        local("mkdir -p versions")

        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(f_name))

        return "versions/web_static_{}.tgz".format(f_name)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Will distribute an archive to my web servers
    """

    if not path.exists(archive_path):
        return False
    try:
        tgz_file = archive_path.split("/")[-1]
        print(tgz_file)
        filename = tgz_file.split(".")[0]
        print(filename)
        pathname = "/data/web_static/releases/" + filename
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -zxvf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgz_file, filename))
        run("rm /tmp/{}".format(tgz_file))
        run("mv /data/web_static/releases/{}/web_static/* "
            " /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except Exception as e:
        return False


def deploy():
    """
    Will create and distribute an archive to my web servers, using
    the function deploy
    """

    path = do_pack()
    if not path:
        return False

    return do_deploy(path)
