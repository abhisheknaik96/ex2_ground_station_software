'''
 * Copyright (C) 2022  University of Alberta
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
'''
'''
 * @file inputHandler.py
 * @author Robert Taylor
 * @date 2022-07-21
'''

class InputHandler():
    """Logs every command that is entered and passes it on to the CLI."""
    def __init__(self):
        self.historyFile = open("command_history.log", "a")
    def getInput(self, prompt):
        inStr = input(prompt)
        self.historyFile.write(inStr + '\n')
        return inStr
