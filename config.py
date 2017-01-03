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

import enum
from gremlin.spline import CubicBezierSpline
from gremlin.input_devices import macro

hold_time = 0.4
hold_long_time = 0.9


class Curve(object):
    pitch_yaw_curve = CubicBezierSpline([
        (-1.0, -1.0),
        (-1.0, -0.0),
        (1.0,  -0.0),
        (1.0,  1.0)
    ])
    pitch_yaw_curve_d = CubicBezierSpline([
        (-1.0, -1.0),
        (-1.0, -0.6),
        (1.0,  0.6),
        (1.0,  1.0)
    ])
    thruster_curve_u = CubicBezierSpline([
        (-1.0, -1.0),
        (-1.0, -0.3),
        (1.0,  0.3),
        (1.0,  1.0)
    ])
    thruster_curve = CubicBezierSpline([
        (-1.0, -0.7),
        (-1.0, -0.185),
        (1.0,  0.185),
        (1.0,  0.7)
    ])
    thruster_curve_d = CubicBezierSpline([
        (-1.0, -0.5),
        (-1.0, -0.3),
        (1.0,  0.3),
        (1.0,  0.5)
    ])


class Button(enum.Enum):
    throttle_rdr_altm = 25
    throttle_eac = 24


class Macro(object):
    shield_raise_front = macro.Macro()
    shield_raise_front.tap(macro.Keys.KP8)
    shield_raise_right = macro.Macro()
    shield_raise_right.tap(macro.Keys.KP6)
    shield_raise_back = macro.Macro()
    shield_raise_back.tap(macro.Keys.KP2)
    shield_raise_left = macro.Macro()
    shield_raise_left.tap(macro.Keys.KP4)
    shield_reset = macro.Macro()
    shield_reset.tap(macro.Keys.KP5)

    power_increase_weapon_shield = macro.Macro()
    power_increase_weapon_shield.tap(macro.Keys.Num1)
    power_increase_weapon_shield.tap(macro.Keys.Num2)
    power_increase_weapon = macro.Macro()
    power_increase_weapon.tap(macro.Keys.Num1)
    power_increase_shield = macro.Macro()
    power_increase_shield.tap(macro.Keys.Num2)
    power_increase_avionic = macro.Macro()
    power_increase_avionic.tap(macro.Keys.Num2)
    power_reset = macro.Macro()
    power_reset.tap(macro.Keys.Num0)
    power_switch_weapon = macro.Macro()
    power_switch_weapon.tap(macro.Keys.Num4)
    power_switch_shield = macro.Macro()
    power_switch_shield.tap(macro.Keys.Num5)
    power_switch_avionic = macro.Macro()
    power_switch_avionic.tap(macro.Keys.Num6)

    target_nearest_hostile = macro.Macro()
    target_nearest_hostile.tap(macro.Keys.T)
    target_reticle_focus = macro.Macro()
    target_reticle_focus.tap(macro.Keys.R)
    target_cycle_all_fwd = macro.Macro()
    target_cycle_all_fwd.tap(macro.Keys.I)
    target_cycle_all_bck = macro.Macro()
    target_cycle_all_bck.tap(macro.Keys.K)
    target_cycle_friendly_fwd = macro.Macro()
    target_cycle_friendly_fwd.tap(macro.Keys.U)
    target_cycle_friendly_bck = macro.Macro()
    target_cycle_friendly_bck.tap(macro.Keys.J)
    target_cycle_hostile_fwd = macro.Macro()
    target_cycle_hostile_fwd.tap(macro.Keys.Y)
    target_cycle_hostile_bck = macro.Macro()
    target_cycle_hostile_bck.tap(macro.Keys.H)
    target_cycle_pinned_fwd = macro.Macro()
    target_cycle_pinned_fwd.tap(macro.Keys.O)
    target_cycle_pinned_bck = macro.Macro()
    target_cycle_pinned_bck.tap(macro.Keys.L)
    target_pin = macro.Macro()
    target_pin.tap(macro.Keys.P)

    systems_cycle_ifcs = macro.Macro()
    systems_cycle_ifcs.tap(macro.Keys.V)
    systems_esp_toggle = macro.Macro()
    systems_esp_toggle.press(macro.Keys.RAlt)
    systems_esp_toggle.tap(macro.Keys.O)
    systems_esp_toggle.release(macro.Keys.RAlt)
    systems_pip = macro.Macro()
    systems_pip.tap(macro.Keys.Period)
    systems_comstab_toggle = macro.Macro()
    systems_comstab_toggle.press(macro.Keys.LAlt)
    systems_comstab_toggle.tap(macro.Keys.J)
    systems_comstab_toggle.release(macro.Keys.LAlt)
    systems_gforce_toggle = macro.Macro()
    systems_gforce_toggle.press(macro.Keys.LAlt)
    systems_gforce_toggle.tap(macro.Keys.K)
    systems_gforce_toggle.release(macro.Keys.LAlt)

    self_destruct = macro.Macro()
    self_destruct.press(macro.Keys.RAlt)
    self_destruct.press(macro.Keys.Backspace)
    self_destruct.pause(hold_time)
    self_destruct.release(macro.Keys.Backspace)
    self_destruct.release(macro.Keys.RAlt)

    eject = macro.Macro()
    eject.press(macro.Keys.RAlt)
    eject.press(macro.Keys.L)
    eject.pause(hold_long_time)
    eject.release(macro.Keys.L)
    eject.release(macro.Keys.RAlt)

    flight_engage = macro.Macro()
    flight_engage.tap(macro.Keys.F)
    flight_landing_mode = macro.Macro()
    flight_landing_mode.tap(macro.Keys.N)
    flight_autoland = macro.Macro()
    flight_autoland.press(macro.Keys.N)
    flight_autoland.pause(hold_time)
    flight_autoland.release(macro.Keys.N)
    flight_quantum_travel = macro.Macro()
    flight_quantum_travel.tap(macro.Keys.B)
    flight_decoupled_mode = macro.Macro()
    flight_decoupled_mode.tap(macro.Keys.C)
    flight_match_target_speed = macro.Macro()
    flight_match_target_speed.tap(macro.Keys.M)
    flight_boost = macro.Macro()
    flight_boost.tap(macro.Keys.X)
    flight_afterburner = macro.Macro()
    flight_afterburner.press(macro.Keys.LShift)
    flight_afterburner_release = macro.Macro()
    flight_afterburner_release.release(macro.Keys.LShift)
    flight_spacebrake = macro.Macro()
    flight_spacebrake.press(macro.Keys.LAlt)
    flight_spacebrake.tap(macro.Keys.X)
    flight_spacebrake.release(macro.Keys.LAlt)

    counter_measures_cycle = macro.Macro()
    counter_measures_cycle.press(macro.Keys.G)
    counter_measures_cycle.pause(hold_time)
    counter_measures_cycle.release(macro.Keys.G)
    counter_measures_fire = macro.Macro()
    counter_measures_fire.tap(macro.Keys.G)

    hud_headlock_mode = macro.Macro()
    hud_headlock_mode.tap(macro.Keys.Z)
    hud_interact_toggle = macro.Macro()
    hud_interact_toggle.tap(macro.Keys.F3)

    hud_panel_up = macro.Macro()
    hud_panel_up.tap(macro.Keys.W)
    hud_panel_down = macro.Macro()
    hud_panel_down.tap(macro.Keys.S)
    hud_panel_right = macro.Macro()
    hud_panel_right.tap(macro.Keys.D)
    hud_panel_left = macro.Macro()
    hud_panel_left.tap(macro.Keys.A)
    hud_panel_confirm = macro.Macro()
    hud_panel_confirm.tap(macro.Keys.F)
