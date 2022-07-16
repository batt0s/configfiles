from libqtile.config import Group, EzKey as Key
from libqtile.lazy import lazy

from keys import keys

groups = [
    Group("WWW"),
    Group("SYS"),
    Group("DEV"),
    Group("DOC"),
    Group("VIRT"),
    Group("VID"),
    Group("MUS"),
    Group("CHAT"),
    Group("GFX"),
]

keynames = [i for i in "123456789"]

for keyname, group in zip(keynames, groups):
    keys.extend([
        Key("M-"+keyname, lazy.group[group.name].toscreen()),
        Key("M-S-"+keyname, lazy.window.togroup(group.name)),
        ])
