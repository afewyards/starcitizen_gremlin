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

from config import Curve, AxisMapping, ButtonMapping, BindedNames
from utils import Utils
from controllers import controllers
from vjoy.vjoy import AxisName


throttle_name = controllers.throttle.name
util = Utils()


class FlightSystem:

    def __init__(self):
        self._afterburner = False
        self._landing_mode = False
        self._quantum_mode = False
        self._active_pitch_yaw_curve = Curve.pitch_yaw_curve
        self._active_thruster_curve = Curve.thruster_curve
        self._active_rudder_curve = Curve.pitch_yaw_curve

        self.addListeners()

    def addListeners(self):
        controllers.joystick.addAxisEvent(self.yaw, AxisMapping.joystick_x)
        controllers.joystick.addAxisEvent(self.pitch, AxisMapping.joystick_y)
        controllers.rudder.addAxisEvent(self.roll, AxisMapping.rudder_roll)
        controllers.throttle.addAxisEvent(self.thrusters_vertical, AxisMapping.throttle_vertical)
        controllers.throttle.addAxisEvent(self.thrusters_horizontal, AxisMapping.throttle_horizontal)
        controllers.throttle.addAxisEvent(self.throttle_control, AxisMapping.throttle)

        controllers.throttle.addButtonEvent(self.brake, ButtonMapping.throttle_brake)
        controllers.throttle.addButtonEvent(self.boost, ButtonMapping.throttle_boost)
        # controllers.throttle.addButtonEvent(self.quantum_control, ButtonMapping.throttle_quantum_control)
        controllers.throttle.addButtonEvent(self.landing_control, ButtonMapping.throttle_landing_control)
        controllers.throttle.addButtonEvent(self.engage, ButtonMapping.throttle_engage)
        controllers.throttle.addButtonEvent(self.set_flaps, ButtonMapping.throttle_flapsu)
        controllers.throttle.addButtonEvent(self.set_flaps, ButtonMapping.throttle_flapsd)
        controllers.throttle.addButtonEvent(self.toggle_comstab, ButtonMapping.throttle_comstab)
        controllers.throttle.addButtonEvent(self.toggle_gforce, ButtonMapping.throttle_gforce)
        controllers.throttle.addButtonEvent(self.toggle_decoupled, ButtonMapping.throttle_decoupled_fwd)
        controllers.throttle.addButtonEvent(self.toggle_decoupled, ButtonMapping.throttle_decoupled_bck)

    def yaw(self, event, vjoy):
        vjoy[1].axis(AxisName.X).value = self._active_pitch_yaw_curve(event.value)

    def pitch(self, event, vjoy):
        vjoy[1].axis(AxisName.Y).value = self._active_pitch_yaw_curve(event.value)

    def roll(self, event, vjoy):
        vjoy[1].axis(AxisName.RZ).value = self._active_rudder_curve(event.value)

    def thrusters_vertical(self, event, vjoy):
        vjoy[1].axis(AxisName.RX).value = self._active_thruster_curve(event.value)

    def thrusters_horizontal(self, event, vjoy):
        vjoy[1].axis(AxisName.RY).value = self._active_thruster_curve(event.value)

    def brake(self, event, vjoy):
        vjoy[1].button(BindedNames.flight_brake).is_pressed = event.is_pressed

    def boost(self, event, vjoy):
        vjoy[1].button(BindedNames.flight_boost).is_pressed = event.is_pressed

    def landing_control(self, event, vjoy, joy):
        self._landing_mode = event.is_pressed
        self.set_flaps(event, vjoy, joy)

    def engage(self, event, vjoy, joy):
        if joy[throttle_name].button(ButtonMapping.throttle_quantum_control).is_pressed:
            util.short_long_press(event, vjoy[1].button(BindedNames.flight_system_quantum), vjoy[1].button(BindedNames.flight_system_engage))
        elif joy[throttle_name].button(ButtonMapping.throttle_landing_control).is_pressed:
            util.short_long_press(event, vjoy[1].button(BindedNames.fligth_system_landing), vjoy[1].button(BindedNames.flight_system_engage))

    def throttle_control(self, event, vjoy, joy):
        divider = 3
        max_value = 2
        part = max_value / divider
        pos = max_value - (joy[throttle_name].axis(AxisMapping.throttle).value + 1)

        if joy[throttle_name].button(ButtonMapping.throttle_flapsu).is_pressed and self._landing_mode is False:
            if (pos > (part * (divider - 1)) + part / (7 - divider)):
                pos = pos - (part * (divider - 1))
                pos = (pos / part) * max_value

                if self._afterburner == False:
                    vjoy[1].button(BindedNames.flight_afterburner).is_pressed = True
                    self._afterburner = True
            else:
                pos = (pos / (part * (divider - 1))) * max_value

                if self._afterburner:
                    vjoy[1].button(BindedNames.flight_afterburner).is_pressed = False
                    self._afterburner = False
        else:
            if self._afterburner:
                vjoy[1].button(BindedNames.flight_afterburner).is_pressed = False
                self._afterburner = False

        vjoy[1].axis(AxisName.Z).value = pos - 1

    def set_flaps(self, event, vjoy, joy):
        self.throttle_control(event, vjoy, joy)
        if joy[throttle_name].button(ButtonMapping.throttle_flapsu).is_pressed and self._landing_mode is False:
            self._active_pitch_yaw_curve = Curve.pitch_yaw_curve
            self._active_thruster_curve = Curve.thruster_curve_u
        elif joy[throttle_name].button(ButtonMapping.throttle_flapsd).is_pressed or self._landing_mode is True:
            self._active_pitch_yaw_curve = Curve.pitch_yaw_curve_d
            self._active_thruster_curve = Curve.thruster_curve_d
        else:
            self._active_pitch_yaw_curve = Curve.pitch_yaw_curve
            self._active_thruster_curve = Curve.pitch_yaw_curve

    def toggle_comstab(self, event, vjoy):
        vjoy[1].button(BindedNames.flight_system_comstab).is_pressed = event.is_pressed

    def toggle_gforce(self, event, vjoy):
        vjoy[1].button(BindedNames.flight_system_gforce).is_pressed = event.is_pressed

    def toggle_decoupled(self, event, vjoy):
        vjoy[1].button(BindedNames.flight_decoupled).is_pressed = event.is_pressed
