#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin('pypi:pybuilder_pytest')


name = "applienv"
default_task = "verify"
version = '1.0.0'

@init
def set_properties(project):
    project.set_property("dir_source_pytest_python","src/pytest/python")
    project.get_property("pytest_extra_args").append("--html=test_report.html")
