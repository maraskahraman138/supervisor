"""Mock of Network Manager Connection Settings service."""

from dbus_fast import Variant
from dbus_fast.service import PropertyAccess, dbus_property, signal

from .base import DBusServiceMock, dbus_method

BUS_NAME = "org.freedesktop.NetworkManager"
SETTINGS_FIXTURE = {
    "connection": {
        "id": Variant("s", "Wired connection 1"),
        "interface-name": Variant("s", "eth0"),
        "llmnr": Variant("i", 2),
        "mdns": Variant("i", 2),
        "permissions": Variant("as", []),
        "timestamp": Variant("t", 1598125548),
        "type": Variant("s", "802-3-ethernet"),
        "uuid": Variant("s", "0c23631e-2118-355c-bbb0-8943229cb0d6"),
    },
    "ipv4": {
        "address-data": Variant(
            "aa{sv}",
            [
                {
                    "address": Variant("s", "192.168.2.148"),
                    "prefix": Variant("u", 24),
                }
            ],
        ),
        "addresses": Variant("aau", [[2483202240, 24, 16951488]]),
        "dns": Variant("au", [16951488]),
        "dns-search": Variant("as", []),
        "gateway": Variant("s", "192.168.2.1"),
        "method": Variant("s", "auto"),
        "route-data": Variant(
            "aa{sv}",
            [
                {
                    "dest": Variant("s", "192.168.122.0"),
                    "prefix": Variant("u", 24),
                    "next-hop": Variant("s", "10.10.10.1"),
                }
            ],
        ),
        "routes": Variant("aau", [[8038592, 24, 17435146, 0]]),
    },
    "ipv6": {
        "address-data": Variant("aa{sv}", []),
        "addresses": Variant("a(ayuay)", []),
        "dns-search": Variant("as", []),
        "method": Variant("s", "auto"),
        "route-data": Variant("aa{sv}", []),
        "routes": Variant("a(ayuayu)", []),
        "addr-gen-mode": Variant("i", 0),
    },
    "proxy": {},
    "802-3-ethernet": {
        "assigned-mac-address": Variant("s", "preserve"),
        "auto-negotiate": Variant("b", False),
        "mac-address-blacklist": Variant("as", []),
        "s390-options": Variant("a{ss}", {}),
    },
    "802-11-wireless": {"ssid": Variant("ay", b"NETT")},
}


def setup(object_path: str | None = None) -> DBusServiceMock:
    """Create dbus mock object."""
    return ConnectionSettings()


# pylint: disable=invalid-name


class ConnectionSettings(DBusServiceMock):
    """Connection Settings mock.

    gdbus introspect --system --dest org.freedesktop.NetworkManager --object-path /org/freedesktop/NetworkManager/Settings/1
    """

    interface = "org.freedesktop.NetworkManager.Settings.Connection"
    object_path = "/org/freedesktop/NetworkManager/Settings/1"

    @dbus_property(access=PropertyAccess.READ)
    def Unsaved(self) -> "b":
        """Get Unsaved."""
        return False

    @dbus_property(access=PropertyAccess.READ)
    def Flags(self) -> "u":
        """Get Flags."""
        return 0

    @dbus_property(access=PropertyAccess.READ)
    def Filename(self) -> "s":
        """Get Unsaved."""
        return "/etc/NetworkManager/system-connections/Supervisor eth0.nmconnection"

    @signal()
    def Updated(self) -> None:
        """Signal Updated."""

    @signal()
    def Removed(self) -> None:
        """Signal Removed."""

    @dbus_method()
    def Update(self, properties: "a{sa{sv}}") -> None:
        """Do Update method."""
        self.Updated()

    @dbus_method()
    def UpdateUnsaved(self, properties: "a{sa{sv}}") -> None:
        """Do UpdateUnsaved method."""

    @dbus_method()
    def Delete(self) -> None:
        """Do Delete method."""
        self.Removed()

    @dbus_method()
    def GetSettings(self) -> "a{sa{sv}}":
        """Do GetSettings method."""
        return SETTINGS_FIXTURE

    @dbus_method()
    def GetSecrets(self, setting_name: "s") -> "a{sa{sv}}":
        """Do GetSecrets method."""
        return self.GetSettings()

    @dbus_method()
    def ClearSecrets(self) -> None:
        """Do ClearSecrets method."""

    @dbus_method()
    def Save(self) -> None:
        """Do Save method."""
        self.Updated()

    @dbus_method()
    def Update2(self, settings: "a{sa{sv}}", flags: "u", args: "a{sv}") -> "a{sv}":
        """Do Update2 method."""
        self.Updated()
        return {}
