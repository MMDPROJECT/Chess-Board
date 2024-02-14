from tracemalloc import start
import flet as ft
import importlib.util
import os

import subprocess

# from Shared.Classes.Pieces import start


class NewGame(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.all_data = ft.Column()
        self.player1_black = ft.TextField(
            label="BLACK",
            border=ft.InputBorder.UNDERLINE,
            filled=True,
            hint_text="Enter your name",
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
        )
        self.player2_white = ft.TextField(
            label="WHITE",
            border=ft.InputBorder.UNDERLINE,
            filled=True,
            hint_text="Enter your name",
            prefix_icon=ft.icons.PERSON_2_OUTLINED,
        )

    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        "Player 1",
                                        ft.TextStyle(
                                            size=50,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                ],
                            ),
                            self.player1_black,
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        "Player 2",
                                        ft.TextStyle(
                                            size=50,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                ],
                            ),
                            self.player2_white,
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.ElevatedButton(
                                    content=ft.Text("READY!!", size=13, weight="bold"),
                                    style=ft.ButtonStyle(
                                        shape={
                                            "": ft.RoundedRectangleBorder(radius=8),
                                        },
                                        color={
                                            "": "blue",
                                        },
                                        bgcolor={"": "#181818"},
                                    ),
                                    height=42,
                                    width=320,
                                    on_click=lambda _: self.start_game(),
                                ),
                            ),
                        ],
                    ),
                )
            ]
        )

    def start_game(self):
        player1 = self.player1_black
        player2 = self.player2_white
        # Get the path of the current script
        project_dir_to_start_path = os.path.sep.join("\Chess-Board\Shared\Classes\Pieces\start.py".split("\\"))
        abs_start_path = os.path.dirname(os.getcwd()) + project_dir_to_start_path
        subprocess.run(["python", abs_start_path])
        # start(player1, player2)