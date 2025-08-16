import flet as ft
# --- CORREÇÃO 1: O IMPORT CORRETO ---
# Importamos as classes de formas que vamos usar
from flet.canvas import Canvas, Rect, Circle, Text

# Mapeamento de cores
CORES = {
    "verde_escuro": "#00C800",
    "vermelho_escuro": "#C80000",
    "amarelo_escuro": "#C8C800",
    "azul_escuro": "#0000C8",
    "preto": "#000000",
    "cinza": "#646464",
    "branco": "#FFFFFF"
}

def main(page: ft.Page):
    page.title = "Genius com Flet"
    page.window_width = 600
    page.window_height = 650
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#EAEAEA"

    def ao_clicar(e: ft.TapEvent):
        """Esta função será chamada quando o usuário clicar no tabuleiro."""
        print(f"Clique detectado nas coordenadas: ({e.local_x}, {e.local_y})")
        # Futuramente, aqui vamos chamar a lógica do jogo
        page.update()

    # O Canvas com todas as suas formas (agora sem o 'ft.canvas.')
    canvas_jogo = Canvas(
        width=402,
        height=402,
        shapes=[
            Rect(x=0, y=0, width=200, height=200, paint=ft.Paint(color=CORES["verde_escuro"]), border_radius=ft.border_radius.only(top_left=200)),
            Rect(x=202, y=0, width=200, height=200, paint=ft.Paint(color=CORES["vermelho_escuro"]), border_radius=ft.border_radius.only(top_right=200)),
            Rect(x=0, y=202, width=200, height=200, paint=ft.Paint(color=CORES["amarelo_escuro"]), border_radius=ft.border_radius.only(bottom_left=200)),
            Rect(x=202, y=202, width=200, height=200, paint=ft.Paint(color=CORES["azul_escuro"]), border_radius=ft.border_radius.only(bottom_right=200)),
            Circle(x=201, y=201, radius=90, paint=ft.Paint(color=page.bgcolor, style=ft.PaintingStyle.FILL)),
            Circle(x=201, y=201, radius=80, paint=ft.Paint(color=CORES["preto"])),
            Text(
                x=201, y=201, 
                text="Micro Genius", 
                text_align=ft.TextAlign.CENTER, 
                style=ft.TextStyle(size=25, color=CORES["branco"], weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center
            ),
        ],
    )

    # --- CORREÇÃO 2: ADICIONANDO INTERATIVIDADE ---
    # Envolvemos nosso Canvas em um GestureDetector para capturar cliques
    tabuleiro_interativo = ft.GestureDetector(
        content=canvas_jogo,
        on_tap_down=ao_clicar,
    )

    page.add(
        ft.Text("Pontos: 0", size=24, weight=ft.FontWeight.BOLD),
        tabuleiro_interativo, # Adicionamos o tabuleiro interativo, não o canvas diretamente
        ft.Text("Clique em Micro Genius para iniciar ou reiniciar partida", size=18)
    )
    page.update()

# Para rodar diretamente no navegador
ft.app(target=main, view=ft.WEB_BROWSER)