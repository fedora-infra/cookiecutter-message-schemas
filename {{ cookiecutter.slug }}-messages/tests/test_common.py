# SPDX-FileCopyrightText: {{ cookiecutter.year }} Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""Unit tests for common properties of the message schemas."""

from {{ cookiecutter.pkg_name }}_messages.thing import NewThingV1
from .utils import DUMMY_THING


def test_properties():
    """Assert some properties are correct."""
    body = {
        "agent": "dummy-user",
        "thing": DUMMY_THING,
    }
    message = NewThingV1(body=body)

    assert message.app_name == "{{ cookiecutter.name }}"
    assert (
        message.app_icon
        == "https://apps.fedoraproject.org/img/icons/{{ cookiecutter.slug }}.png"
    )
    assert message.agent_name == "dummy-user"
    assert message.agent_avatar == (
        "https://seccdn.libravatar.org/avatar/"
        "18e8268125372e35f95ef082fd124e9274d46916efe2277417fa5fecfee31af1"
        "?s=64&d=retro"
    )
    assert message.usernames == ["dummy-user"]
