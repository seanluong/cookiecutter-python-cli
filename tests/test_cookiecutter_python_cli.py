# from contextlib import ContextDecorator, ContextBaseClass
import os
from os.path import dirname, abspath
import shutil
import tempfile
import pytest
from cookiecutter.main import cookiecutter
import sys
import subprocess



@pytest.fixture
def tmp_dir_path():
    tmp_dir_path = tempfile.mkdtemp(suffix='cookiecutter', dir='/tmp')
    yield tmp_dir_path
    if os.path.exists(tmp_dir_path):
        shutil.rmtree(tmp_dir_path)


def test_project_tests_passed(tmp_dir_path):
    template = dirname(dirname(abspath(__file__)))
    extra_context = {
        'project_name': 'mycli'
    }

    result = cookiecutter(template,
                          no_input=True,
                          extra_context=extra_context,
                          output_dir=tmp_dir_path)

    assert subprocess.check_call(['pytest', os.path.join(tmp_dir_path, 'mycli')]) == 0


def test_project_no_license(tmp_dir_path):
    template = dirname(dirname(abspath(__file__)))
    extra_context = {
        'project_name': 'mycli',
        'open_source_license': 'Not open source'
    }

    result = cookiecutter(template,
                          no_input=True,
                          extra_context=extra_context,
                          output_dir=tmp_dir_path)

    assert subprocess.check_call(['pytest', os.path.join(tmp_dir_path, 'mycli')]) == 0
    assert not os.path.exists(os.path.join(tmp_dir_path, 'mycli', 'LICENSE'))
