# Copyright (c) 2017 Thierry Kleist
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from config import Macro, ButtonMapping, BindedNames
from utils import Utils
from controllers import controllers

util = Utils()


class TargetSystem:

    def __init__(self):
        controllers.joystick.addButtonEvent(self.nearest_target, ButtonMapping.joystick_target_nearest)
        controllers.joystick.addButtonEvent(self.reticle_target, ButtonMapping.joystick_target_reticle)
        controllers.joystick.addButtonEvent(self.target_cycle_hostile, ButtonMapping.joystick_target_cycle_hostile)
        controllers.joystick.addButtonEvent(self.target_cycle_pinned, ButtonMapping.joystick_target_cycle_pinned)
        controllers.joystick.addButtonEvent(self.target_cycle_all, ButtonMapping.joystick_target_cycle_all)
        controllers.joystick.addButtonEvent(self.target_cycle_friendly, ButtonMapping.joystick_target_cycle_friendly)

        controllers.throttle.addButtonEvent(self.missile_lock, ButtonMapping.throttle_missile_lock)


    def missile_lock(self, event, vjoy):
        util.short_long_press(event, vjoy[1].button(BindedNames.cycle_missiles), vjoy[1].button(BindedNames.missile_lock))

    def nearest_target(self, event):
        util.short_long_press(event, Macro.target_nearest_hostile, Macro.target_pin)

    def reticle_target(self, event):
        util.short_long_press(event, Macro.target_reticle_focus, Macro.target_pin)

    def target_cycle_hostile(self, event):
        util.short_long_press(event, Macro.target_cycle_hostile_fwd, Macro.target_cycle_hostile_bck)

    def target_cycle_pinned(self, event):
        util.short_long_press(event, Macro.target_cycle_pinned_fwd, Macro.target_cycle_pinned_bck)

    def target_cycle_all(self, event):
        util.short_long_press(event, Macro.target_cycle_all_fwd, Macro.target_cycle_all_bck)

    def target_cycle_friendly(self, event):
        util.short_long_press(event, Macro.target_cycle_friendly_fwd, Macro.target_cycle_friendly_bck)

    # left (14) - right (12) - hud
