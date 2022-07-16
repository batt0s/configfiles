from libqtile.config import EzKey as Key, EzDrag as Drag, EzClick as Click
from libqtile.lazy import lazy
import os

keys = [
    # -- Essentials --
    # Exit QTile
    Key("M-C-q", lazy.shutdown()),
    # Restart QTile
    Key("M-C-r", lazy.restart()),
    # Kill focused window
    Key("M-q", lazy.kill()),
    # Run terminal (kitty)
    Key("M-<Return>", lazy.spawn("kitty")),
    # Run rofi
    Key("M-r", lazy.spawn("rofi -show run")),
    # Powermenu
    Key("M-C-x", lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/powermenu.sh"))),
    # Change layout
    Key("M-<Tab>", lazy.next_layout()),
    # Toggle between active groups
#    Key("M-<Tab>-j", lazy.screen.prev_group(skip_empty=True)),
#    Key("M-<Tab>-k", lazy.screen.next_group(skip_empty=True)),
    # -- Window controls --
    # Switch focus
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    Key("M-j", lazy.layout.down()),
    Key("M-k", lazy.layout.up()),
    # Move Window
    Key("M-S-h", lazy.layout.shuffle_left()),
    Key("M-S-l", lazy.layout.shuffle_right()),
    Key("M-S-j", lazy.layout.shuffle_down()),
    Key("M-S-k", lazy.layout.shuffle_up()),
    # Resize Window
    Key("M-C-h", lazy.layout.grow_left()),
    Key("M-C-l", lazy.layout.grow_right()),
    Key("M-C-j", lazy.layout.grow_down()),
    Key("M-C-k", lazy.layout.grow_up()),
]

mouse = [
    Drag("M-1", lazy.window.set_position_floating()),
    Click("M-2", lazy.window.bring_to_front()),
    Drag("M-3", lazy.window.set_size_floating()),
]
