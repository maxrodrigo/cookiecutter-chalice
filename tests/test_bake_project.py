# -*- coding: utf-8 -*-

""" Try the cookies """


def test_bake_project(cookies):
    context = {"project_name": "Hello World"}
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "hello_world"
    assert result.project.isdir()
