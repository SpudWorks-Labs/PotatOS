"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
               Program Name: MaSH.
   Description: A custom terminal for the PotatOS system.
                  File: mash_ui.py
                 Date: 2026/10/01
              Version: 0.1.0-2026.10.01

===========================================================

         Copyright (C) 2026 SpudWorks Labs.

This program is free software: you can redistribute it
  and/or modify it under the terms of the GNU Affero
General Public License as published by the Free Software
   Foundation, either version 3 of the License, or
         (at your option) any later version.

This program is distributed in the hope that it will be
   useful, but WITHOUT ANY WARRANTY; without even the
  implied warranty of MERCHANTABILITY or FITNESS FOR A
 PARTICULAR PURPOSE.  See the GNU Affero General Public
              License for more details.

   You should have received a copy of the GNU Affero
    General Public License along with this program.
     If not, see <https://www.gnu.org/licenses/>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



import getpass
import socket
from pathlib import Path
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, RichLog, Input
from textual import on
from rich.text import Text


class MaSH(App):
    TITLE = "MaSH"
    BINDINGS = [
        Binding("ctrl+q", "quit", "Shut Down")
    ]
    CSS = """
    #output {
        border: round red;
    }
    #output:focus {
        border: round magenta;
    }
    #cmd {
        border: round red;
        height: 3;
        padding: 0 1;
    }
    #cmd:focus {
        border: round magenta;
        height: 3;
        padding: 0 1;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self.cwd: path = Path.cwd()

    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog(id="output")
        prompt = self.prompt()
        yield Input(id="cmd", placeholder=prompt)
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#cmd", Input).focus()

    def get_user(self):
        user = getpass.getuser()
        host = socket.gethostname()

        return f"{user}@{host}"

    def prompt(self) -> str:
        # self.query_one("#prompt", Static).update(str(self.cwd))
        userhost = self.get_user()
        prompt = f"{userhost} [{self.cwd}]"

        return prompt

    @on(Input.Submitted, "#cmd")
    def submit_command(self, event: Input.Submitted) -> None:
        line = event.value.strip()
        event.input.value = ""
        # Could make the $ check for root and in get_user()
        command = f"{self.get_user()}$ {line}"

        self.query_one("#output", RichLog).write(
            Text(command)
        )
        # self.execute(line)

if __name__ == '__main__':
    MaSH().run()
