from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import random

KV = '''
MDScreen:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "Dice Roller"
            md_bg_color: 18/255, 0/255, 255/255, 1
            
    Image:
        id: dice_state
        size_hint_y: 0.4
        size_hint_x: 0.4
        pos_hint: {'center_x' :0.5, 'center_y':0.5}
        source: "assets/dice_1.png"
    MDRaisedButton:
        id: 'roll_button'
        text: "ROLL"
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        md_bg_color: 18/255, 0/255, 255/255, 1
        on_release: app.play()
'''


class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen

    def play(self):
        dice_face = random.choice(
            ["dice_1.png", "dice_2.png", "dice_3.png", "dice_4.png", "dice_5.png", "dice_6.png", ])
        file_name = "assets/" + dice_face
        self.kvs.ids.dice_state.source = file_name


ma = MainApp()
ma.run()