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
from gremlin.util import extract_ids
from gremlin.util import SingletonDecorator


class Device(object):

    def __init__(self, name, device_id, mode):
        self.name = name
        self.mode = mode
        self.device_id = device_id
        self.hid, self.wid = extract_ids(device_id)

    def addButtonEvent(self, callback, id):
        event = event_handler.Event(
            event_type=event_handler.InputType.JoystickButton,
            hardware_id=self.hid,
            windows_id=self.wid,
            identifier=id
        )
        callback_registry.add(callback, event, self.mode, False)

    def addAxisEvent(self, callback, id):
        event = event_handler.Event(
            event_type=event_handler.InputType.JoystickAxis,
            hardware_id=self.hid,
            windows_id=self.wid,
            identifier=id
        )
        callback_registry.add(callback, event, self.mode, False)

    def addHatEvent(self, callback, id):
        event = event_handler.Event(
            event_type=event_handler.InputType.JoystickHat,
            hardware_id=self.hid,
            windows_id=self.wid,
            identifier=id
        )
        callback_registry.add(callback, event, self.mode, False)


@SingletonDecorator
class Controllers:

    def __init__(self):
        self.rudder = Device(
            name="VKBsim Black Box",
            device_id=589103391,
            mode="Default"
        )

        self.joystick = Device(
            name="Joystick - HOTAS Warthog",
            device_id=72287234,
            mode="Default"
        )

        self.throttle = Device(
            name="Throttle - HOTAS Warthog",
            device_id=72287236,
            mode="Default"
        )

controllers = Controllers()
