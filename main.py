import flet as ft

# Datos simulados
clientes = [
    {"nombre": "Ana", "deuda": 50},
    {"nombre": "Luis", "deuda": 0},
    {"nombre": "Pedro", "deuda": 25}
]

productos = [
    {"nombre": "Queso", "precio": 1000},
    {"nombre": "Pollo", "precio": 20},
    {"nombre": "Verdura", "precio": 5}
]

def main(page: ft.Page):
    page.title = "Panadería"
    page.padding = 20
    page.scroll = True  # Activar scroll si el contenido crece

    # Título arriba a la derecha
    titulo = ft.Row(
        controls=[
            ft.Text("Panadería", size=30, weight="bold", color="blue")
        ],
        alignment=ft.MainAxisAlignment.END
    )

    # Contenedor para mostrar contenido dinámico
    contenido = ft.Column(spacing=10)

    # Funciones para mostrar secciones
    def mostrar_productos(e):
        contenido.controls.clear()
        contenido.controls.append(ft.Text("🛒 Productos disponibles:", size=20, weight="bold"))
        for p in productos:
            contenido.controls.append(ft.Text(f"- {p['nombre']}: ${p['precio']}"))
        page.update()

    def mostrar_clientes(e):
        contenido.controls.clear()
        contenido.controls.append(ft.Text("👤 Clientes y deudas:", size=20, weight="bold"))
        for c in clientes:
            contenido.controls.append(ft.Text(f"- {c['nombre']}: ${c['deuda']}"))
        page.update()

    def mostrar_deudas_pagadas(e):
        contenido.controls.clear()
        contenido.controls.append(ft.Text("✅ Clientes con deudas pagadas:", size=20, weight="bold"))
        sin_deuda = [c for c in clientes if c["deuda"] == 0]
        if sin_deuda:
            for c in sin_deuda:
                contenido.controls.append(ft.Text(f"- {c['nombre']}"))
        else:
            contenido.controls.append(ft.Text("Ningún cliente ha pagado su deuda."))
        page.update()

    # Botones de navegación
    botones = ft.Row(
        controls=[
            ft.ElevatedButton("Clientes", on_click=mostrar_clientes),
            ft.ElevatedButton("Deudas pagadas", on_click=mostrar_deudas_pagadas),
            ft.ElevatedButton("Productos", on_click=mostrar_productos),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    # Agregar elementos a la página
    page.add(
        titulo,
        ft.Divider(),
        botones,
        ft.Divider(),
        contenido
    )

# PARA DESPLIEGUE EN RENDER.COM: usar puert
ft.app(target=main, view=ft.WEB_BROWSER)
