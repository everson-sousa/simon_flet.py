import flet as ft
import math

# Mapeamento de cores (podemos usar as mesmas que já tínhamos)
CORES = {
    "verde_escuro": "#00C800",
    "vermelho_escuro": "#C80000",
    "amarelo_escuro": "#C8C800",
    "azul_escuro": "#0000C8",
    "verde_claro": "#64FF64",
    "vermelho_claro": "#FF6464",
    "amarelo_claro": "#FFFF96",
    "azul_claro": "#9696FF",
    "preto": "#000000",
    "cinza": "#646464",
}

def main(page: ft.Page):
    page.title = "Genius com Flet"
    page.window_width = 600
    page.window_height = 650
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # O Canvas é a nossa "tela" de desenho
    canvas = ft.Canvas(
        width=402,
        height=402,
        content=ft.Stack(
            [
                # Quadrante Verde (0)
                ft.canvas.Rect(x=0, y=0, width=200, height=200, paint=ft.Paint(color=CORES["verde_escuro"]), border_radius=ft.border_radius.only(top_left=200)),
                # Quadrante Vermelho (1)
                ft.canvas.Rect(x=202, y=0, width=200, height=200, paint=ft.Paint(color=CORES["vermelho_escuro"]), border_radius=ft.border_radius.only(top_right=200)),
                # Quadrante Amarelo (2)
                ft.canvas.Rect(x=0, y=202, width=200, height=200, paint=ft.Paint(color=CORES["amarelo_escuro"]), border_radius=ft.border_radius.only(bottom_left=200)),
                # Quadrante Azul (3)
                ft.canvas.Rect(x=202, y=202, width=200, height=200, paint=ft.Paint(color=CORES["azul_escuro"]), border_radius=ft.border_radius.only(bottom_right=200)),
                
                # Círculo central "vazio"
                ft.canvas.Circle(x=201, y=201, radius=90, paint=ft.Paint(color=page.bgcolor, style=ft.PaintingStyle.FILL)),
                
                # Círculo central com o botão
                ft.canvas.Circle(x=201, y=201, radius=80, paint=ft.Paint(color=CORES["preto"])),
                
                # Texto "Genius"
                ft.canvas.Text(x=201, y=201, text="GENIUS", text_align=ft.TextAlign.CENTER, text_style=ft.TextStyle(size=30, color="white")),
            ]
        ),
    )

    # Adicionamos o canvas e um placar de texto à página
    page.add(
        ft.Text("Pontos: 0", size=24, weight=ft.FontWeight.BOLD),
        canvas,
        ft.Text("Clique em GENIUS para iniciar", size=18)
    )

    page.update()

# Para rodar como um aplicativo de desktop
# ft.app(target=main)

# Para rodar diretamente no navegador
ft.app(target=main, view=ft.WEB_BROWSER)