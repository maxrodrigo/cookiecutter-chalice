# Cookiecutter Chalice API

[![Build Status](https://travis-ci.org/maxrodrigo/cookiecutter-chalice.svg?branch=master)](https://travis-ci.org/maxrodrigo/cookiecutter-chalice)

A [Cookiecutter](https://github.com/audreyr/cookiecutter) poject template for creating an [AWS Chalice](https://github.com/aws/chalice/) based API.

## Demo

![Installation](./assets/demo.svg)

## Requirements

- Python 3.6+
- [Cookiecutter](https://github.com/audreyr/cookiecutter)

## Usage

1. [Install Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

```sh
$ pip install --user cookiecutter
```

1. Create your application

```sh
$ cookiecutter gh:maxrodrigo/cookiecutter-chalice
```

1. All set! Follow the instruction inside the project README.

## Example

Creating the project will generate this folders:

```
my_awesome_api
├── .chalice
│   └── config.json
├── .editorconfig
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── Makefile
├── README.md
├── app.py
├── requirements.txt
├── requirements_dev.txt
└── test
    ├── __init__.py
    ├── conftest.py
    └── test_my_awesome_api.py
```

## Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

## License

Distributed under the terms of the [MIT license](http://opensource.org/licenses/MIT), Cookiecutter Chalice is free and open source software.
