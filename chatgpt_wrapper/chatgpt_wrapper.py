
import reflex as rx
from Backend import search
from rxconfig import config


class State(rx.State):
    text:str = ""
    output_text:str= ""
    count: int = 0
    def set_text(self, text:str):
        self.text = text
    def set_output_text(self):
        ob = search.GPT_search()
        self.output_text = ob.search(self.text)
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
def ouput_box():
    return rx.text(
        State.output_text,
        color_scheme='gold',
        size='9',
        weight='bold'
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
            inc_button(),
            spacing='4',
            align='center',
            justify='center'
    )
def text_box():
    return rx.input(
        placeholder="Search here",
        on_change=State.set_text,
        on_double_click=State.set_output_text,
        value = State.text
    )
def inc_button():
    return rx.vstack(
                rx.button(
                    "Decrement",
                    color_scheme='red',
                    on_click=State.decrement,
                ),
                rx.heading(State.count, font_size="2em"),
                rx.button(
                    "Increment",
                    color_scheme='green',
                    on_click=State.increment,
                ),
                rx.divider(
                    size='4'),
                rx.divider(size='4'),
                text_box(),
                rx.divider(size='4'),
                rx.divider(size='4'),
                ouput_box(),
                spacing='4',
                align='center',
                justify='center',
                
                
            )

        


app = rx.App()
app.add_page(index)
