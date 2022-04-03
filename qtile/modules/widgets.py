from libqtile import qtile, widget

# Colors for widgets
colors = [#["#282c34", "#282c34"], # panel background
          ["#0c0c0c", "#0c0c0c"],
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#87181a", "#87181a"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#282c34", "#282c34"], # color for the 'even widgets'
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


        

VolumeWidget = MyVolumeWidget(
    foreground = colors[2],
    background = colors[4],
    padding = 5,
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
