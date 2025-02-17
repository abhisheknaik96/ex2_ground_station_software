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
 * @file cli.py
 * @author Robert Taylor
 * @date 2022-07-21
'''

from groundStation import GroundStation
from options import optionsFactory

class cli(GroundStation):
    """Runs all the time to get a command as input and execute it."""
    def run(self):
        while(1):
            # 'to send: ' is the prompt seen by the CLI user
            inStr = self.inputHandler.getInput("to send: ")
            try:
                # For a command like "EX2.TIME_MANAGEMENT.SET_TIME(1598385718)",
                # the interactiveHandler returns the set_time 'transaction object'
                # which is then executed.
                transactObj = self.interactive.getTransactionObject(inStr, self.networkManager)
                ret = transactObj.execute()
                # Print the output.
                print()
                if type(ret) == dict:
                    for key, value in ret.items():
                        print("{} : {}".format(key, value))
                elif type(ret) == list:
                    for r in ret:
                        for key, value in r.items():
                            print("{} : {}".format(key, value))
                else:
                    print(repr(ret)) # last, try to find a representation
                print()
            except Exception as e:
                print(e)
                continue

if __name__ == "__main__":
    opts = optionsFactory("basic")
    cliRunner = cli(opts.getOptions())
    cliRunner.run()
