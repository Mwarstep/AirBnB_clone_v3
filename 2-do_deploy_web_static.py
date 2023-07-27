#!/usr/bin/python3
from fabric.api import put, run, local, env
from os import path


env.hosts = ["54.160.101.122", "54.237.51.149"]


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
