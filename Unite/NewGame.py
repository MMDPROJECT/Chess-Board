from flet import *

class Newgame(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        
    def build(self):
        return Column(
            controls=[
                Container(
                    height=800,width=200,
                    bgcolor='red',
                    content=Column(
                        controls=[
                            Text('hi'),
                            Container(
                                on_click= lambda _: self.page.go('/LoadGame'),
                                content=Text('back',size=20,color='black')
                                
                            )
                        ]
                    )
                )
            ]
        )