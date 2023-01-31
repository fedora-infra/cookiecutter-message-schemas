# Copyright (C) {{ cookiecutter.year }}  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

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
