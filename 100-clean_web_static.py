#!/usr/bin/python3
from fabric.api import put, run, local, env
import os

env.hosts = ['54.160.101.122', '54.237.51.149']


def do_clean(number=0):
    """
    Will delete out-of-date archives using the function
    do_clean

    Arguments:
            number (int): The number of archives to store

    If number is 0 or 1, keep only most recent archive.
    If number is 2, keep the most recent and 2nd most recent versions.
    """

    number = 1 if int(number) == 0 else int(number)

    arch_1 = sorted(os.listdir("versions"))
    [arch_1.pop() for x in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(y)) for y in arch_1]

    with cd("/data/web_static/releases"):
        arch_1 = run("ls -tr").split()
        arch_1 = [y for y in arch_1 if "web_static_" in y]
        [arch_1.pop() for x in range(number)]
        [run("rm -rf ./{}".format(y)) for y in arch_1]
