#!/usr/bin/python3
from fabric.api import local
from datetime import date
from time import strftime


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
