from flet import *
from pages.NewGame import Newgame
def handler(page):
    return{
        '/':View(
        route='/',
        controls=[
            Newgame(page)
            ]
        ),
    }