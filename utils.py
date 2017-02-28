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


from threading import Timer
from gremlin.input_devices import macro
import gremlin

long_press_delay = 0.3 # in seconds


class Utils:

    def __init__(self):
        self._timers = {}

    def get_id(self, event):
        return str(event.hardware_id) + "_" + str(event.identifier)

    def tap(self, button):
        button.is_pressed = True
        timer = Timer(0.1, self.set_button_false, [button])
        timer.start()

    def set_button_false(self, button):
        button.is_pressed = False

    def run_macro_or_button_tap(self, macro_or_button):
        if isinstance(macro_or_button, macro.Macro):
            macro_or_button.run()
        else:
            self.tap(macro_or_button)

    def short_long_press(self, event, short_macro, long_macro):
        if event.is_pressed == False:
            if self._timers[self.get_id(event)] and self._timers[self.get_id(event)].is_alive():
                self._timers[self.get_id(event)].cancel()
                self.run_macro_or_button_tap(short_macro)

        else:
            self._timers[self.get_id(event)] = Timer(long_press_delay, self.run_macro_or_button_tap, [long_macro])
            self._timers[self.get_id(event)].start()
