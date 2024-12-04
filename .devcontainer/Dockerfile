FROM jupyter/minimal-notebook

USER jovyan

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install setuptools
RUN python3 -m pip install sphinx

WORKDIR "/workspaces/my-first-python-package"