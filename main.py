import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Flet"
    page.theme_mode = "light"

    result = ft.Text(value="0", size=32)

    current_input = ""

    def button_click(e):
        nonlocal current_input
        value = e.control.text

        if value == "C":
            current_input = ""
            result.value = "0"
        elif value == "=":
            try:
                current_input = str(eval(current_input))
                result.value = current_input
            except:
                result.value = "Error"
                current_input = ""
        else:
            current_input += value
            result.value = current_input

        page.update()

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]

    layout = [
        ft.Row([result], alignment="center")
    ]

    for row in buttons:
        layout.append(
            ft.Row(
                [ft.ElevatedButton(text=txt, width=70, on_click=button_click) for txt in row],
                alignment="center"
            )
        )

    page.add(*layout)

ft.app(target=main)
