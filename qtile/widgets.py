from libqtile.config import Screen
from libqtile import widget, bar
import os

colors = {
    "white": "#d8d8d8",
    "black": "#181818",
    "gray": "#282c34",
    "background": "#181818",
    "current_line": '#282828',
    "foreground": '#f8f8f2',
    "comment": '#535453',
    "red":     '#ab4642',
    "borderline": "#ab4642",
}

# Default Widget Settings
widget_defaults = dict(
        font = "JetBrainsMono Nerd Font",
        fontsize = 12,
        padding = 2,
        backgroud = colors["borderline"],
)
extension_defaults = widget_defaults.copy()


sep = widget.Sep(
    linewidth = 0,
    padding = 6,
    foreground = colors["white"],
    background = colors["gray"]
)

group_box = widget.GroupBox(
    font = "Ubuntu Bold",
    fontsize = 12,
    margin_y = 3,
    margin_x = 0,
    padding = 5,
    borderwidth = 3,
    active = colors['white'],
    inactive = colors['comment'],
    rounded = True,
    disable_drag = True,
    highlight_color = colors["gray"],
    highlight_method = "line",
    this_current_screen_border = colors['red'],
    this_screen_border = colors["red"],
    background = colors['background'],
    block_highlight_text_color = colors['red']
)

winname = widget.WindowName(
    foreground = colors['red'],
    background = colors["gray"],
    padding = 0
)

cpu = widget.CPU(
                padding = 5,
                foreground = colors["white"],
                background = colors["red"],
                format = 'CPU {load_percent}%'
                )

mem = widget.Memory(
                foreground = colors["white"],
                background = colors["gray"],
                padding = 5,
                format = 'MEM: {MemUsed:.0f}{mm}',
                )

class MyVolumeWidget(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ' %' + str(self.volume)
        if self.volume < 50:
            self.text = ' %' + str(self.volume)
        else:
            self.text = ' %' + str(self.volume)

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ' %' + str(self.volume)
        if self.volume < 50:
            self.text = ' %' + str(self.volume)
        else:
            self.text = ' %' + str(self.volume)
        self.draw()

        if wob:
            with open(self.wob, "a") as f:
                f.write(str(self.volume) + "\n")

vol = MyVolumeWidget(
    foreground = colors["white"],
    background = colors["red"],
    padding = 5
    )


battery = widget.Battery(
        battery = "BAT0",
                energy_now_file = 'charge_now',
                energy_full_file = 'charge_full',
                power_now_file = 'current_now',
                update_interval = 5,
                background = colors["gray"],
                format = '  {percent:2.0%}',
                low_percentage=0.15,
                notify_below=0.2
                )

clayouticon = widget.CurrentLayoutIcon(
                custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                foreground = colors["white"],
                background = colors["red"],
                padding = 0,
                scale = 0.7
                )

clayout = widget.CurrentLayout(
                foreground = colors["white"],
                background = colors["red"],
                padding = 5
                )

clock = widget.Clock(
                foreground = colors["white"],
                background = colors["gray"],
                format = "  %Y-%m-%d %H:%M "
                )

bar_widgets = [
    group_box,
    sep,
    winname,
    sep,
    cpu,
    mem,
    vol,
    battery,
    clayouticon,
    clayout,
    clock
]

screens = [
    Screen(
        top = bar.Bar(widgets = bar_widgets, opacity = 1.0, size = 24)
        ),
]
