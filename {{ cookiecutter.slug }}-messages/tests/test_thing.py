# SPDX-FileCopyrightText: {{ cookiecutter.year }} Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

"""Unit tests for the message schema."""

import pytest

from jsonschema import ValidationError
from ..thing import NewThingV1
from .utils import DUMMY_THING


def test_minimal():
    """
    Assert the message schema validates a message with the required fields.
    """
    body = {
        "agent": "dummy-user",
        "thing": DUMMY_THING,
    }
    message = NewThingV1(body=body)
    message.validate()
    assert message.url is None


def test_full():
    """
    Assert the message schema validates a message with the required fields.
    """
    thing = DUMMY_THING.copy()
    thing["url"] = "http://localhost/thing"
    body = {
        "agent": "dummy-user",
        "thing": thing,
    }
    message = NewThingV1(body=body)
    message.validate()
    assert message.url == "http://localhost/thing"


def test_missing_fields():
    """Assert an exception is actually raised on validation failure."""
    minimal_message = {
        "agent": "dummy-user",
        "thing": {"id": 1},
    }
    message = NewThingV1(body=minimal_message)
    with pytest.raises(ValidationError):
        message.validate()


def test_str():
    """Assert __str__ produces a human-readable message."""
    body = {
        "agent": "dummy-user",
        "thing": DUMMY_THING,
    }
    expected_str = "New Thing: dummy\nBy: dummy-user\n"
    message = NewThingV1(body=body)
    message.validate()
    assert expected_str == str(message)


def test_summary():
    """Assert the summary is correct."""
    body = {
        "agent": "dummy-user",
        "thing": DUMMY_THING,
    }
    expected_summary = 'dummy-user created thing "dummy" (1)'
    message = NewThingV1(body=body)
    assert expected_summary == message.summary
