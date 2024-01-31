import flet as ft

class NewGame(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        
    def build(self):
        return ft.Column(
            controls=[
                ft.Container(
                    height=800,width=200,
                    bgcolor='red',
                    content=ft.Column(
                        controls=[
                            ft.Text('hi'),
                            ft.Container(
                                on_click= lambda _: self.page.go('/LoadGame'),
                                content=ft.Text('back',size=20,color='black')
                                
                            )
                        ]
                    )
                )
            ]
        )