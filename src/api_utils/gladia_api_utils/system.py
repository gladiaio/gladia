from genericpath import isdir
import os
from pathlib import Path
from posixpath import isabs
import distutils.dir_util
import shutil
import subprocess
import sys

from icecream import ic


def copy(source, destination):
    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not isabs(Path(source)):
        source = os.path.join(root_path, source)
    if not isabs(Path(destination)):
        destination = os.path.join(root_path, destination)

    return distutils.dir_util.copy_tree(source, destination)


def get_cwd():
    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))
    return root_path


def path_to_absolute(path):
    if not isabs(Path(path)):
        # used for relative paths
        namespace = sys._getframe(1).f_globals
        cwd = os.getcwd()
        rel_path = namespace["__file__"]
        root_path = os.path.dirname(os.path.join(cwd, rel_path))
        path = os.path.join(root_path, path)
    return path


def run(*argv):
    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    cmd = f"cd {root_path} &&"
    for arg in argv:
        cmd += f" {arg}"

    return subprocess.run([cmd], shell=True, capture_output=True)


def remove(*paths):
    for path in paths:
        if isinstance(path, str):
            path = Path(path)
            if not isabs(path):
                namespace = sys._getframe(1).f_globals
                cwd = os.getcwd()
                rel_path = namespace["__file__"]
                root_path = os.path.dirname(os.path.join(cwd, rel_path))
                path = os.path.join(root_path, path)
            if isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
