import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simple"
    page.theme_mode = ft.ThemeMode.LIGHT
    result = ft.Text(value="0", size=32)

    current_input = ""

    def update_result():
        result.value = current_input if current_input else "0"
        page.update()

    def button_click(e):
        nonlocal current_input
        data = e.control.data

        if data == "=":
            try:
                current_input = str(eval(current_input))
            except:
                current_input = "Error"
        elif data == "C":
            current_input = ""
        else:
            current_input += data
        update_result()

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C"]
    ]

    controls = []
    for row in buttons:
        controls.append(
            ft.Row(
                controls=[
                    ft.ElevatedButton(text=btn, data=btn, on_click=button_click, width=70)
                    for btn in row
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    page.add(
        ft.Column(
            [
                result,
                ft.Divider(),
                *controls
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
