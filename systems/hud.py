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


from utils import Utils
from config import Button, VjoyButton
from controllers import controllers
from gremlin.macro import _send_key_down, _send_key_up
import gremlin

utils = Utils()

class HudMode(object):
    VIEW_MODE_CLEAR = 0
    VIEW_MODE_HUDENTRY = 1
    VIEW_MODE_HEADLOOK = 2


class HudSystem:

    def __init__(self):
        self._hud_headlook_lock = HudMode.VIEW_MODE_CLEAR

        controllers.throttle.addButtonEvent(self.mode_switch, Button.throttle_hud_panel_mode)
        controllers.throttle.addButtonEvent(self.mode_switch, Button.throttle_hud_power_mode)

        controllers.joystick.addButtonEvent(self.mode_top, Button.joystick_hud_up)
        controllers.joystick.addButtonEvent(self.mode_right, Button.joystick_hud_right)
        controllers.joystick.addButtonEvent(self.mode_down, Button.joystick_hud_down)
        controllers.joystick.addButtonEvent(self.mode_left, Button.joystick_hud_left)
        controllers.joystick.addButtonEvent(self.mode_press, Button.joystick_hud_press)
        controllers.joystick.addHatEvent(self.hat_to_buttons, Button.joystick_hat)

    def mode_press_fn(self, event, joy, vjoy, shield_key, power_key = 0, hud_key = 0):
        key = shield_key
        if joy[controllers.throttle.name].button(Button.throttle_hud_power_mode).is_pressed:
            key = power_key
        if joy[controllers.throttle.name].button(Button.throttle_hud_panel_mode).is_pressed:
            key = hud_key

        if key == 0:
            return

        if type(key) is tuple:
            for k in key:
                vjoy[1].button(k).is_pressed = event.is_pressed
        else:
            vjoy[1].button(key).is_pressed = event.is_pressed


    def mode_press(self, event, joy, vjoy):
        self.mode_press_fn(event, joy, vjoy, VjoyButton.shield_reset, VjoyButton.power_reset)

    def mode_top(self, event, joy, vjoy):
        self.mode_press_fn(event, joy, vjoy, VjoyButton.shield_raise_front, (VjoyButton.power_increase_weapon,VjoyButton.power_increase_shield), VjoyButton.hud_up)

    def mode_left(self, event, joy, vjoy):
        self.mode_press_fn(event, joy, vjoy, VjoyButton.shield_raise_left, VjoyButton.power_increase_weapon, VjoyButton.hud_left)

    def mode_right(self, event, joy, vjoy):
        self.mode_press_fn(event, joy, vjoy, VjoyButton.shield_raise_right, VjoyButton.power_increase_shield, VjoyButton.hud_right)

    def mode_down(self, event, joy, vjoy):
        self.mode_press_fn(event, joy, vjoy, VjoyButton.shield_raise_back, VjoyButton.power_increase_avionic, VjoyButton.hud_down)

    def mode_switch(self, event, joy, vjoy):
        if joy[controllers.throttle.name].button(Button.throttle_hud_panel_mode).is_pressed:
            vjoy[1].button(VjoyButton.hud_mode).is_pressed = True
            utils.tap_delayed(vjoy[1].button(VjoyButton.hud_down), 0.1)
        else:
            vjoy[1].button(VjoyButton.hud_mode).is_pressed = False


    # TODO: add hat
    def hat_to_buttons(self, event, joy, vjoy):
        xas, yas = event.value

        if xas is 0 and yas is 1:
            # top
            # utils.tap(vjoy[1].button(VjoyButton.zoom_in))
            pass
        elif xas is 1 and yas is 0:
            # right
            pass
        elif xas is 0 and yas is -1:
            # bottom
            # utils.tap(vjoy[1].button(VjoyButton.zoom_out))
            pass
        elif xas is -1 and yas is 0:
            # left
            pass
