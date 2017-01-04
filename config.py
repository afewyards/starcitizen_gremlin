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

from gremlin.spline import CubicBezierSpline
from gremlin.input_devices import macro

hold_time = 0.4
hold_long_time = 0.9


class DeviceConfig(object):

    joystick_name = 'Joystick - HOTAS Warthog'
    joystick_id = 72287234

    throttle_name = 'Throttle - HOTAS Warthog'
    throttle_id = 72287236

    rudder_name = 'VKBsim Black Box'
    rudder_id = 589103391


class Curve(object):
    pitch_yaw_curve = CubicBezierSpline([
        (-1.0, -1.0),
        (-1.0, 0.2),
        (1.0,  -0.2),
        (1.0,  1.0)
    ])
    pitch_yaw_curve_d = CubicBezierSpline([
        (-1.0, -0.61),
        (-1.0, 0.15),
        (1.0,  -0.15),
        (1.0,  0.61)
    ])
    thruster_curve_u = CubicBezierSpline([
        (-1.0, -1.0),
        (-1.0, 0.5),
        (1.0,  -0.5),
        (1.0,  1.0)
    ])
    thruster_curve = CubicBezierSpline([
        (-1.0, -0.65),
        (-1.0, 0.265),
        (1.0,  -0.265),
        (1.0,  0.65)
    ])
    thruster_curve_d = CubicBezierSpline([
        (-1.0, -0.6),
        (-1.0, 0.4),
        (1.0,  -0.4),
        (1.0,  0.6)
    ])


class AxisMapping(object):
    joystick_x = 1
    joystick_y = 2
    rudder_roll = 4
    throttle = 4
    throttle_vertical = 1
    throttle_horizontal = 2


class ButtonMapping(object):
    joystick_fire_group_1 = 1
    joystick_fire_group_2 = 6
    joystick_fire_group_3 = 5
    joystick_fire_missiles = 2
    joystick_fire_counter_measures = 3
    joystick_cycle_counter_measures = 4

    joystick_target_reticle = 7
    joystick_target_cycle_hostile = 8
    joystick_target_nearest = 9
    joystick_target_cycle_pinned = 10

    joystick_hud_up = 15
    joystick_hud_right = 16
    joystick_hud_down = 17
    joystick_hud_left = 18
    joystick_hud_press = 19

    throttle_boost = 2
    throttle_quantum_control = 27
    throttle_landing_control = 28
    throttle_engage = 26
    throttle_flapsu = 22
    throttle_flapsd = 23
    throttle_comstab = 11
    throttle_gforce = 12

    throttle_rdr_altm = 25
    throttle_eac = 24


# Do not edit below this line

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

    abandon_ship = macro.Macro()
    abandon_ship.press(macro.Keys.RAlt)
    abandon_ship.press(macro.Keys.Backspace)
    abandon_ship.pause(hold_time)
    abandon_ship.release(macro.Keys.Backspace)
    abandon_ship.release(macro.Keys.RAlt)
    abandon_ship.pause(hold_time)
    abandon_ship.press(macro.Keys.RAlt)
    abandon_ship.press(macro.Keys.L)
    abandon_ship.pause(hold_long_time)
    abandon_ship.release(macro.Keys.L)
    abandon_ship.release(macro.Keys.RAlt)

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
    flight_boost.press(macro.Keys.X)
    flight_boost_release = macro.Macro()
    flight_boost_release.release(macro.Keys.X)
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
