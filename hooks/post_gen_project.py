#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{ cookiecutter.use_pre-commit  }}" != "y":
        remove_file(".pre-commit-config.yaml")

    if "{{ cookiecutter.use_editorconfig }}" != "y":
        remove_file(".editorconfig")

    if "Not open source" == "{{ cookiecutter.open_source_license  }}":
        remove_file("LICENSE")
