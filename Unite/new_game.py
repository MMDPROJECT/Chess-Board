import flet as ft


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
                    # height=800,width=800,
                    # bgcolor='dark blue',
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
                                    ft.Image(
                                        src="Shared/Classes/Image/player1_color.png",
                                        width=550,
                                        height=100,
                                        fit=ft.ImageFit.CONTAIN,
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
                                    # on_click=lambda _: page.go(
                                    #     "location start"
                                    # ),  # TODO
                                ),
                            ),
                        ],
                    ),
                )
            ]
        )
