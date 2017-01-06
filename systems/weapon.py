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


from config import ButtonMapping, BindedNames, Macro
from controllers import controllers


class WeaponSystem:

    def __init__(self):
        controllers.joystick.addButtonEvent(self.fire_primary_active_group, ButtonMapping.joystick_fire_group_1)
        controllers.joystick.addButtonEvent(self.fire_secondary_active_group, ButtonMapping.joystick_fire_group_2)
        controllers.joystick.addButtonEvent(self.fire_third_active_group, ButtonMapping.joystick_fire_group_3)
        controllers.joystick.addButtonEvent(self.fire_missiles, ButtonMapping.joystick_fire_missiles)
        controllers.joystick.addButtonEvent(self.fire_counter_measures, ButtonMapping.joystick_fire_counter_measures)
        controllers.joystick.addButtonEvent(self.cycle_counter_measures, ButtonMapping.joystick_cycle_counter_measures)

    def fire_primary_active_group(self, event, vjoy, joy):
        if joy[controllers.throttle.name].button(ButtonMapping.throttle_rdr_altm).is_pressed:
            vjoy[1].button(BindedNames.fire_group_1).is_pressed = event.is_pressed
        else:
            vjoy[1].button(BindedNames.fire_group_2).is_pressed = event.is_pressed

    def fire_secondary_active_group(self, event, vjoy, joy):
        if joy[controllers.throttle.name].button(ButtonMapping.throttle_rdr_altm).is_pressed:
            vjoy[1].button(BindedNames.fire_group_2).is_pressed = event.is_pressed
        else:
            vjoy[1].button(BindedNames.fire_group_1).is_pressed = event.is_pressed

    def fire_third_active_group(self, event, vjoy):
        vjoy[1].button(BindedNames.fire_group_3).is_pressed = event.is_pressed

    def fire_missiles(self, event, vjoy):
        vjoy[1].button(BindedNames.fire_missiles).is_pressed = event.is_pressed

    def fire_counter_measures(self, event):
        if event.is_pressed:
            Macro.counter_measures_fire.run()

    def cycle_counter_measures(self, event):
        if event.is_pressed:
            Macro.counter_measures_cycle.run()
