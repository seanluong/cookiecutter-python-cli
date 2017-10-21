from cookiecutter.main import cookiecutter
import os
from os.path import dirname, abspath
import pytest


def test_project_tests_passed(tmpdir):
    template = dirname(dirname(abspath(__file__)))
    extra_context = {
        'project_name': 'mycli'
    }
    output_dir = str(tmpdir.realpath())
    result = cookiecutter(template,
                          no_input=True,
                          extra_context=extra_context,
                          output_dir=output_dir)

    assert pytest.main([os.path.join(output_dir, 'mycli')]) == 0
