from typing import List  # noqa: F401
from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import os
import socket
import subprocess

from modules.widgets import *



mod = "mod4"
terminal = "kitty"
myBrowser = "firefox"

keys = [

        # Essentials
        Key([mod], "Return",
            lazy.spawn(terminal),
            desc="Launches terminal"
            ),
        Key([mod], "r",
            lazy.spawn("rofi -show run"),
            desc="Runs launcher"
            ),
        Key([mod], "b",
            lazy.spawn(myBrowser),
            desc="Runs browser"
            ),
        Key([mod], "q",
            lazy.window.kill(),
            desc="Kill focused window"
            ),
        Key([mod, "control"], "q",
            lazy.shutdown(),
            desc="Exit QTile"
            ),
        Key([mod, "control"], "r",
            lazy.restart(),
            desc="Restart QTile"
            ),

        Key([mod, "control"], "x",
            lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/powermenu.sh")),
            desc="Power Menu"
            ),

        # Window Controls
        Key([mod], "m",
            lazy.layout.maximize(),
            desc="Toggle window between min and max size"
            ),
        Key([mod], "n",
            lazy.layout.normalize(),
            desc="Normalize"
            ),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Toggle between active groups
    Key([mod], "Right", lazy.screen.next_group(skip_empty=True), desc="Next group (skip empty)"),
    Key([mod], "Left", lazy.screen.prev_group(skip_empty=True), desc="Prev gorup (skip empty)"),

    #Key([], "XFAudioRaiseVolume", lazy.spawn('amixer -c 0 -q set Master 2dB+')),

]

groups = [
    Group("WWW"),
    Group("DEV"),
    Group("SYS"),
    Group("DOC"),
    Group("CHAT"),
    Group("VBOX"),
    Group("VID"),
    Group("MUS"),
    Group("GFX"),
]

keynames = [i for i in "123456789"]

# mod + i, moves screen to groups[i]
# mod + shift + i, moves screen with active tab to groups[i]
for keyname, group in zip(keynames, groups):
    keys.extend([
        Key([mod], keyname, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], keyname, lazy.window.togroup(group.name)),
    ])



layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4, margin=5),
    layout.Max(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4, margin=5),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus=['#d75f5f','#8f3d3d'], border_width=3, margin=3),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(border_focus=['#d75f5f', '#8f3d3d'], border_width=4, margin=5),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Prompt
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# Colors for widgets
colors = [#["#282c34", "#282c34"], # panel background
          ["#0c0c0c", "#0c0c0c"],
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
#          ["#4f76c7", "#4f76c7"],
#          ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#87181a", "#87181a"],
          ["#282c34", "#282c34"],
          #["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens

# Default Widget Settings
widget_defaults = dict(
        font = "Ubuntu Mono",
        fontsize = 12,
        padding = 2,
        backgroud = colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widget_list():
    widget_list = [
            widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[2],
                background = colors[0]
                ),
            widget.GroupBox(
                font = "Ubuntu Bold",
                fontsize = 9,
                margin_y = 3,
                margin_x = 0,
                padding_y = 5,
                padding_x = 3,
                borderwidth = 3,
                active = colors[2],
                inactive = colors[7],
                rounded = False,
                highlight_color = colors[1],
                highlight_method = "line",
                this_current_screen_border = colors[6],
                this_screen_border = colors [4],
                other_current_screen_border = colors[6],
                other_screen_border = colors[4],
                foreground = colors[2],
                background = colors[0]
                ),
            widget.Prompt(
                prompt = prompt,
                padding = 10,
                foreground = colors[3],
                background = colors[0]
                ),
            widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[2],
                background = colors[0]
                ),
            widget.WindowName(
                foreground = colors[6],
                background = colors[0],
                padding = 0
                ),
            widget.Systray(
                background = colors[0],
                padding = 5
                ),
            widget.Sep(
                linewidth = 0,
                padding = 6,
                foreground = colors[2],
                background = colors[0]
                ),
            widget.TextBox(
                text = '',
                background = colors[0],
                foreground = colors[5],
                padding = 0,
                fontsize = 37
                ),
             widget.Net(
                interface = "enp2s0",
                format = '{down} ↓↑ {up}',
                foreground = colors[2],
                background = colors[5],
                padding = 5
                ),
              widget.TextBox(
                text = '',
                background = colors[5],
                foreground = colors[4],
                padding = 0,
                fontsize = 37
                ),
             widget.CPU(
                padding = 5,
                foreground = colors[2],
                background = colors[4]
                ),
             widget.TextBox(
                text = " 🌡",
                padding = 2,
                foreground = colors[2],
                background = colors[4],
                fontsize = 11
                ),
              widget.ThermalSensor(
                foreground = colors[2],
                background = colors[4],
                threshold = 70,
                padding = 5,
                tag_sensor = "CPU"
                ),
              widget.TextBox(
               text = '',
               background = colors[4],
               foreground = colors[5],
               padding = 0,
               fontsize = 37
               ),
              widget.TextBox(
                text = " 🖬",
                foreground = colors[2],
                background = colors[5],
                padding = 0,
                fontsize = 14
                ),
              widget.Memory(
                foreground = colors[2],
                background = colors[5],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                padding = 5
                ),
              widget.TextBox(
                text = '',
                background = colors[5],
                foreground = colors[4],
                padding = 0,
                fontsize = 37
                ),
              #widget.TextBox(
                #text = " ",
                #foreground = colors[2],
                #background = colors[4],
                #padding = 0
                #),
              VolumeWidget,
              #widget.Volume(
              # foreground = colors[2],
              # background = colors[4],
              # padding = 5
              # ),
              widget.TextBox(
               text = '',
               background = colors[4],
               foreground = colors[5],
               padding = 0,
               fontsize = 37
               ),
              widget.Battery(
                      #text = " Power:",
                      energy_now_file = 'charge_now',
                      energy_full_file = 'charge_full',
                      power_now_file = 'current_now',
                      update_interval = 5,
                      background = colors[5],
                      format = ' {percent:2.0%}'
                ),
              widget.TextBox(
               text = '',
               background = colors[5],
               foreground = colors[4],
               padding = 0,
               fontsize = 37
               ),
              widget.CurrentLayoutIcon(
                custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                foreground = colors[0],
                background = colors[4],
                padding = 0,
                scale = 0.7
                ),
              widget.CurrentLayout(
                foreground = colors[2],
                background = colors[4],
                padding = 5
                ),
              widget.TextBox(
                text = '',
                background = colors[4],
                foreground = colors[5],
                padding = 0,
                fontsize = 37
                ),
              widget.Clock(
                foreground = colors[2],
                background = colors[5],
                format = " %Y-%m-%d %H:%M "
                ),
               widget.TextBox(
                text = '',
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu/powermenu.sh'))},
                foreground = colors[2],
                backgroud = colors[5],
                padding = 8
               )
            ]
    return widget_list

screens = [
    Screen(
        top=bar.Bar(widgets=init_widget_list(), opacity=1.0, size=20)
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
