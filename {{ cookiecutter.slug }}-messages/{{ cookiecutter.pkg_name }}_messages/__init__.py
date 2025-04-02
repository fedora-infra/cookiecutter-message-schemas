# SPDX-FileCopyrightText: {{ cookiecutter.year }} Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import importlib.metadata

from .thing import NewThingV1


__version__ = importlib.metadata.version("{{ cookiecutter.pkg_name }}_messages")
