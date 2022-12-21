FROM mcr.microsoft.com/devcontainers/python:3.10

COPY . /workspaces/xgns/
RUN pip3 --disable-pip-version-check --no-cache-dir install -e "/workspaces/xgns/[dev]"
