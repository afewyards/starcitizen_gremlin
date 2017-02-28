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
from vjoy.vjoy import AxisName


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


class Axis(object):
    joystick_x = 1
    joystick_y = 2
    rudder_roll = 1
    throttle = 4
    throttle_vertical = 1
    throttle_horizontal = 2


class Button(object):
    joystick_fire_group_1 = 1
    joystick_fire_group_2 = 6
    joystick_fire_group_3 = 5
    joystick_fire_missiles = 2
    joystick_cycle_counter_measures = 3
    joystick_fire_counter_measures = 4

    joystick_target_reticle = 7
    joystick_target_cycle_hostile = 8
    joystick_target_nearest = 9
    joystick_target_cycle_pinned = 10
    joystick_target_cycle_all = 11
    joystick_target_cycle_friendly = 13

    joystick_hud_up = 15
    joystick_hud_right = 16
    joystick_hud_down = 17
    joystick_hud_left = 18
    joystick_hud_press = 19
    joystick_hat = 1

    throttle_reticle = 15
    throttle_brake = 7
    throttle_boost = 2
    throttle_hud_power_mode = 13
    throttle_hud_panel_mode = 14
    throttle_quantum_control = 27
    throttle_landing_control = 28
    throttle_engage = 26
    throttle_flapsu = 22
    throttle_flapsd = 23
    throttle_comstab = 11
    throttle_gforce = 12
    throttle_gimbal_lock = 21

    throttle_decoupled_fwd = 9
    throttle_decoupled_bck = 10

    throttle_missile_lock = 8

    throttle_quantum_control = 27
    throttle_landing_control = 28

    throttle_rdr_altm = 25
    throttle_eac = 24


class VjoyAxis(object):
    yaw = AxisName.X
    pitch = AxisName.Y
    roll = AxisName.RZ
    thrusters_vertical = AxisName.RX
    thrusters_horizontal = AxisName.RY
    throttle = AxisName.Z


class VjoyButton(object):
    fire_group_1 = 1
    fire_group_2 = 2
    fire_group_3 = 3

    missiles_fire = 4
    missiles_lock = 5
    missiles_cycle = 6

    flight_brake = 7
    flight_boost = 8
    flight_afterburner = 9
    flight_decoupled = 10
    flight_match_speed = 11

    flight_system_engage = 12
    flight_system_comstab = 13
    flight_system_gforce = 14
    fligth_system_landing = 15
    flight_system_quantum = 16

    hud_mode = 17
    hud_up = 18
    hud_right = 19
    hud_down = 20
    hud_left = 21

    target_nearest_hostile = 22
    target_reticle_focus = 23
    target_cycle_all_fwd = 24
    target_cycle_all_bck = 25
    target_cycle_friendly_fwd = 26
    target_cycle_friendly_bck = 27
    target_cycle_hostile_fwd = 28
    target_cycle_hostile_bck = 29
    target_cycle_pinned_fwd = 30
    target_cycle_pinned_bck = 31
    target_pin = 32

    systems_pip = 33
    systems_gimbal_lock_toggle = 34

    self_destruct = 35
    eject = 36

    counter_measures_cycle = 37
    counter_measures_fire = 38

    shield_raise_front = 39
    shield_raise_right = 40
    shield_raise_back = 41
    shield_raise_left = 42
    shield_reset = 43

    power_increase_weapon = 44
    power_increase_shield = 45
    power_increase_avionic = 46
    power_reset = 47
