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

from gremlin import event_handler
from gremlin.input_devices import callback_registry
from gremlin.util import extract_ids, SingletonDecorator
from config import DeviceConfig


class Device(object):

    def __init__(self, name, device_id, mode):
        self.name = name
        self.mode = mode
        self.device_id = device_id
        self.hid, self.wid = extract_ids(device_id)

    def addEvent(self, event_type, id, callback):
        event = event_handler.Event(
            event_type=event_type,
            hardware_id=self.hid,
            windows_id=self.wid,
            identifier=id
        )
        callback_registry.add(callback, event, self.mode, False)

    def addButtonEvent(self, callback, id):
        self.addEvent(event_handler.InputType.JoystickButton, id, callback)

    def addAxisEvent(self, callback, id):
        self.addEvent(event_handler.InputType.JoystickAxis, id, callback)

    def addHatEvent(self, callback, id):
        self.addEvent(event_handler.InputType.JoystickHat, id, callback)


@SingletonDecorator
class Controllers:

    def __init__(self):

        self.joystick = Device(
            name=DeviceConfig.joystick_name,
            device_id=DeviceConfig.joystick_id,
            mode="Default"
        )

        self.throttle = Device(
            name=DeviceConfig.throttle_name,
            device_id=DeviceConfig.throttle_id,
            mode="Default"
        )

        self.rudder = Device(
            name=DeviceConfig.rudder_name,
            device_id=DeviceConfig.rudder_id,
            mode="Default"
        )

controllers = Controllers()
