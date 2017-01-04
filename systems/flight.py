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

from config import Macro, Curve, AxisMapping, ButtonMapping
from utils import Utils
from controllers import controllers
from vjoy.vjoy import AxisName


throttle_name = controllers.throttle.name
util = Utils()


class FlightSystem:

    def __init__(self):
        self._mode = 0
        self._afterburner = False
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

        controllers.throttle.addButtonEvent(self.boost, ButtonMapping.throttle_boost)
        controllers.throttle.addButtonEvent(self.quantum_control, ButtonMapping.throttle_quantum_control)
        controllers.throttle.addButtonEvent(self.landing_control, ButtonMapping.throttle_landing_control)
        controllers.throttle.addButtonEvent(self.engage, ButtonMapping.throttle_engage)
        controllers.throttle.addButtonEvent(self.set_flaps, ButtonMapping.throttle_flapsu)
        controllers.throttle.addButtonEvent(self.set_flaps, ButtonMapping.throttle_flapsd)
        controllers.throttle.addButtonEvent(self.toggle_comstab, ButtonMapping.throttle_comstab)
        controllers.throttle.addButtonEvent(self.toggle_gforce, ButtonMapping.throttle_gforce)

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

    def boost(self, event):
        if event.is_pressed:
            Macro.flight_boost.run()
        else:
            Macro.flight_boost_release.run()

    def quantum_control(self, event):
        if event.is_pressed:
            self._mode = 1
        else:
            if self._mode == 0:
                return
            self._mode = 0
        Macro.flight_quantum_travel.run()

    def landing_control(self, event):
        if event.is_pressed:
            self._mode = 2
        else:
            if self._mode == 0:
                return
            self._mode = 0
        Macro.flight_landing_mode.run()

    def engage(self, event, joy):
        if joy[throttle_name].button(27).is_pressed:
            if event.is_pressed:
                Macro.flight_engage.run()
        elif joy[throttle_name].button(28).is_pressed:
            util.short_long_press(event, Macro.flight_engage, Macro.flight_autoland)

    def throttle_control(self, event, vjoy, joy):
        divider = 3
        max_value = 2
        part = max_value / divider
        pos = max_value - (joy[throttle_name].axis(4).value + 1)

        if joy[throttle_name].button(22).is_pressed:
            if (pos > (part * (divider - 1)) + part / (7 - divider)):
                pos = pos - (part * (divider - 1))
                pos = (pos / part) * max_value

                if self._afterburner == False:
                    Macro.flight_afterburner.run()
                    self._afterburner = True
            else:
                pos = (pos / (part * (divider - 1))) * max_value

                if self._afterburner:
                    Macro.flight_afterburner_release.run()
                    self._afterburner = False
        else:
            if self._afterburner:
                Macro.flight_afterburner_release.run()
                self._afterburner = False

        # invert the axis as sc does that by default
        vjoy[1].axis(AxisName.Z).value = max_value - pos - 1

    def set_flaps(self, event, vjoy, joy):
        self.throttle_control(event, vjoy, joy)
        if joy[throttle_name].button(22).is_pressed:
            self._active_pitch_yaw_curve = Curve.pitch_yaw_curve
            self._active_thruster_curve = Curve.thruster_curve_u
        elif joy[throttle_name].button(23).is_pressed:
            self._active_pitch_yaw_curve = Curve.pitch_yaw_curve_d
            self._active_thruster_curve = Curve.thruster_curve_d
        else:
            self._active_pitch_yaw_curve = Curve.pitch_yaw_curve
            self._active_thruster_curve = Curve.pitch_yaw_curve

    def toggle_comstab(self, event):
        if event.is_pressed:
            Macro.systems_comstab_toggle.run()

    def toggle_gforce(self, event):
        if event.is_pressed:
            Macro.systems_gforce_toggle.run()
