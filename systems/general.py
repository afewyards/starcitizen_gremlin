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

from config import Macro
from controllers import controllers


class GeneralSystem:

    def __init__(self):
        controllers.throttle.addButtonEvent(self.abandon_ship_left, 31)
        controllers.throttle.addButtonEvent(self.abandon_ship_right, 32)

    def abandon_ship(self, event, joy):
        if event.is_pressed & joy[controllers.throttle.name].button(20).is_pressed & joy[controllers.throttle.name].button(31).is_pressed & joy[controllers.throttle.name].button(32).is_pressed:
            Macro.self_destruct.run()
            Macro.eject.run()

    def abandon_ship_left(self, event, joy):
        self.abandon_ship(event, joy)

    def abandon_ship_right(self, event, joy):
        self.abandon_ship(event, joy)
