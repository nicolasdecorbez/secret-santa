# Manage your Secret Santa with a CLI :santa:

This project was born back in 2021, when I was organizing a Secret Santa with by best freinds. I coded a small and trival script to make random pairs of peoples, and to send them a email automatically, to preserve the surprise.

After that, I decided to improve it for the next christmas ; and maybe you would be interested to manage your Secret Santa with your terminal, who knows ? 

This is still a serious work-in-progress projects, I am still refactoring methods to register people / specing on how to interact with the code.

## Installing dependancies

The recommended approach is to use `virtualenv` to install the project dependencies.

```console
$ pip install virtualenv
$ python -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install -e .
```

## Launching the project

To run the secret-santa package, just run this command with python 3.9 installed :
```console
$ secret-santa
```