# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Installing

Clone the repository:

```sh
$ git clone {{ cookiecutter.github_repository }}
```

Set up a virtual environment for the project and activate it.
> Even though we recommend python3 [venv](https://docs.python.org/3/library/venv.html)
> module feel free to use you prefer.

```sh
$ cd {{ cookiecutter.project_slug }}
$ python3 -m venv venv
$ source venv/bin/activate
```

Using `virtualenv`

```sh
$ cd {{ cookiecutter.project_slug }}
$ virtualenv [--python=python3.6] venv
$ source venv/bin/activate
```

Using `virtualwrapper`:

```sh
$ mkvirtualenv {{ cookiecurret.project_slug }}
```

The app provides a `make` command as an interface to the most common tasks.

> Run `make help` to see the available commands!

To initialize the environment simply execute:

```sh
$ make install
```

🍪 You're ready ! try it with:


```sh
$ make run
```

## Running Tests

To run all tests, simply run:

```sh
$ make test
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [maxrodrigo/cookiecutter-chalice](https://github.com/maxrodrigo/cookiecutter-chalice) project template.

