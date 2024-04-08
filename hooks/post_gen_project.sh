#!/bin/sh

set -e
set -x

git init -b main .
git commit --allow-empty -s -m "Initial empty commit"
git add .
git commit -s -m "Project creation from the cookiecutter template"
pre-commit install
