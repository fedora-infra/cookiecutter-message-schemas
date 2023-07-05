# SPDX-FileCopyrightText: {{ cookiecutter.year }} Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from fedora_messaging import message


SCHEMA_URL = "http://fedoraproject.org/message-schema/"

THING_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "foobar": {"type": ["string", "null"]},
        "url": {"type": "string", "format": "uri"},
    },
    "required": ["id", "name"],
}


class {{ cookiecutter.camel_name }}Message(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by {{ cookiecutter.name }}.
    """

    @property
    def app_name(self):
        return "{{ cookiecutter.name }}"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/{{ cookiecutter.slug }}.png"

    @property
    def url(self):
        try:
            return self.body["thing"]["url"]
        except KeyError:
            return None

    @property
    def agent_name(self):
        """The username of the user who initiated the action that generated this message."""
        return self.body.get("agent")

    @property
    def usernames(self):
        """List of users affected by the action that generated this message."""
        return [self.agent_name]

    @property
    def groups(self):
        """List of groups affected by the action that generated this message."""
        group = self.body.get("group")
        return [group] if group else []

    @property
    def packages(self):
        """List of packages affected by the action that generated this message."""
        return []

    @property
    def containers(self):
        """List of containers affected by the action that generated this message."""
        return []

    @property
    def modules(self):
        """List of modules affected by the action that generated this message."""
        return []

    @property
    def flatpaks(self):
        """List of flatpaks affected by the action that generated this message."""
        return []
