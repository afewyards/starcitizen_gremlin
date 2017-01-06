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


from config import Macro, ButtonMapping
from controllers import controllers
import gremlin

class HudMode(object):
    VIEW_MODE_CLEAR = 0
    VIEW_MODE_HUDENTRY = 1
    VIEW_MODE_HEADLOOK = 2


class HudSystem:

    def __init__(self):
        self._hud_headlook_lock = HudMode.VIEW_MODE_CLEAR
        controllers.joystick.addButtonEvent(self.mode_top, ButtonMapping.joystick_hud_up)
        controllers.joystick.addButtonEvent(self.mode_right, ButtonMapping.joystick_hud_right)
        controllers.joystick.addButtonEvent(self.mode_down, ButtonMapping.joystick_hud_down)
        controllers.joystick.addButtonEvent(self.mode_left, ButtonMapping.joystick_hud_left)
        controllers.joystick.addButtonEvent(self.mode_press, ButtonMapping.joystick_hud_press)

        controllers.throttle.addButtonEvent(self.mode_switch, 14)

    # def switch_hudent(self, joy):
    #     if (joy[controllers.throttle.name].button(24).is_pressed & self._hud_headlook_lock == HudMode.VIEW_MODE_CLEAR) or (joy[controllers.throttle.name].button(24).is_pressed == False & self._hud_headlook_lock == HudMode.VIEW_MODE_HUDENTRY):
    #         Macro.hud_interact_toggle.run()
    #         # self._hud_headlook_lock = self._hud_headlook_lock ^ HudMode.VIEW_MODE_HUDENTRY

    def mode_switch(self, event, joy):
        if self._hud_headlook_lock is HudMode.VIEW_MODE_CLEAR and event.is_pressed:
            self._hud_headlook_lock = HudMode.VIEW_MODE_HEADLOOK
            Macro.hud_headlock_mode.run()
        elif self._hud_headlook_lock is HudMode.VIEW_MODE_HEADLOOK and event.is_pressed is False:
            self._hud_headlook_lock = HudMode.VIEW_MODE_CLEAR
            Macro.hud_headlock_mode_release.run()

    def mode_press_fn(self, event, joy, hud_macro, power_macro, shield_macro):
        if event.is_pressed:
            if joy[controllers.throttle.name].button(24).is_pressed is False:
                hud_macro.run()
            else:
                if joy[controllers.throttle.name].button(13).is_pressed:
                    power_macro.run()
                elif self._hud_headlook_lock == HudMode.VIEW_MODE_HEADLOOK:
                    hud_macro.run()
                else:
                    shield_macro.run()

    def mode_press(self, event, joy):
        self.mode_press_fn(event, joy, Macro.hud_panel_confirm, Macro.power_reset, Macro.shield_reset)

    def mode_top(self, event, joy):
        self.mode_press_fn(event, joy, Macro.hud_panel_up, Macro.power_increase_weapon_shield, Macro.shield_raise_front)

    def mode_left(self, event, joy):
        self.mode_press_fn(event, joy, Macro.hud_panel_left, Macro.power_increase_weapon, Macro.shield_raise_left)

    def mode_right(self, event, joy):
        self.mode_press_fn(event, joy, Macro.hud_panel_right, Macro.power_increase_shield, Macro.shield_raise_right)

    def mode_down(self, event, joy):
        self.mode_press_fn(event, joy, Macro.hud_panel_down, Macro.power_increase_avionic, Macro.shield_raise_back)
