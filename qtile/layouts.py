from libqtile import layout
from libqtile.config import Match

layout_defaults = dict(
    margin = 5,
    border_width = 4,
    grow_amout = 3,
    border_focus = "#D75F5F",
        )

floating_layout_defaults = layout_defaults.copy()
floating_layout_defaults["border_width"] = 1

layouts = [
    layout.MonadTall(**layout_defaults),
    layout.Tile(**layout_defaults),
    layout.Floating(**floating_layout_defaults)
        ]

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
