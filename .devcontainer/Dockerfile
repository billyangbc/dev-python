FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# default user is vscode from the base image
#USER vscode

WORKDIR /workspace

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp