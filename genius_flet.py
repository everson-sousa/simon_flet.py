# import flet as ft
# from flet.canvas import Canvas, Rect, Circle, Text
# from random import randrange
# import os
# from pathlib import Path
# import time # Usaremos time em vez de asyncio

# # --- CONSTANTES ---
# CORES_ESCURO = ["#009600", "#960000", "#969600", "#000096"]
# CORES_CLARO = ["#00FF00", "#FF0000", "#FFFF00", "#0000FF"]
# PRETO, BRANCO, CINZA = "#000000", "#FFFFFF", "#EAEAEA"
# BASE_DIR = Path(__file__).resolve().parent
# ARQUIVO_RECORDE = BASE_DIR / "recorde.txt"

# # --- CLASSE PARA A LÓGICA DO JOGO ("CÉREBRO") ---
# class JogoGenius:
#     def __init__(self):
#         self.sequencia = []
#         self.resposta_jogador = []
#         self.estado = "INICIO"
#         self.recorde = self.carregar_recorde()

#     def carregar_recorde(self):
#         if not os.path.exists(ARQUIVO_RECORDE): return 0
#         with open(ARQUIVO_RECORDE, "r") as f:
#             try: return int(f.read().strip())
#             except: return 0

#     def salvar_recorde(self):
#         pontos = len(self.sequencia) - 1
#         if pontos > self.recorde:
#             self.recorde = pontos
#             with open(ARQUIVO_RECORDE, "w") as f: f.write(str(self.recorde))

#     def iniciar_novo_jogo(self):
#         self.sequencia = [randrange(4)]
#         self.resposta_jogador = []
#         self.estado = "MOSTRANDO"

#     def proximo_nivel(self):
#         self.sequencia.append(randrange(4))
#         self.resposta_jogador = []
#         self.estado = "MOSTRANDO"

#     def registrar_jogada(self, cor_id):
#         if self.estado != "JOGANDO": return
#         self.resposta_jogador.append(cor_id)
#         if self.resposta_jogador[-1] != self.sequencia[len(self.resposta_jogador) - 1]:
#             self.salvar_recorde()
#             self.estado = "FIM_DE_JOGO"
#             return
#         if len(self.resposta_jogador) == len(self.sequencia):
#             self.proximo_nivel()

# # --- CLASSE PARA A APLICAÇÃO FLET ("ROSTO") ---
# class AppGenius(ft.Column):
#     def __init__(self):
#         super().__init__()
#         self.jogo = JogoGenius()

#         self.texto_pontos = ft.Text(f"Recorde: {self.jogo.recorde}", size=24, weight=ft.FontWeight.BOLD)
#         self.texto_status = ft.Text("Clique em Micro Genius para iniciar", size=18)
        
#         self.quadrantes = {
#             i: Rect(paint=ft.Paint(color=CORES_ESCURO[i]), **kwargs)
#             for i, kwargs in enumerate([
#                 {"x": 0, "y": 0, "width": 200, "height": 200, "border_radius": ft.border_radius.only(top_left=200)},
#                 {"x": 202, "y": 0, "width": 200, "height": 200, "border_radius": ft.border_radius.only(top_right=200)},
#                 {"x": 0, "y": 202, "width": 200, "height": 200, "border_radius": ft.border_radius.only(bottom_left=200)},
#                 {"x": 202, "y": 202, "width": 200, "height": 200, "border_radius": ft.border_radius.only(bottom_right=200)},
#             ])
#         }
        
#         self.canvas_jogo = Canvas(width=402, height=402, shapes=self.criar_formas_base())
        
#         self.tabuleiro_interativo = ft.GestureDetector(
#             content=self.canvas_jogo,
#             on_tap_down=self.ao_clicar,
#         )

#         self.controls = [
#             self.texto_pontos,
#             self.tabuleiro_interativo,
#             self.texto_status
#         ]
#         self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     def criar_formas_base(self):
#         return list(self.quadrantes.values()) + [
#             Circle(x=201, y=201, radius=90, paint=ft.Paint(color=CINZA)),
#             Circle(x=201, y=201, radius=80, paint=ft.Paint(color=PRETO)),
#             Text(x=201, y=201, text="Micro Genius", text_align=ft.TextAlign.CENTER,
#                  style=ft.TextStyle(size=25, color=BRANCO, weight=ft.FontWeight.BOLD),
#                  alignment=ft.alignment.center),
#         ]

#     # As funções agora são síncronas (sem 'async')
#     def ao_clicar(self, e: ft.TapEvent):
#         if self.tabuleiro_interativo.disabled:
#             return
            
#         cor_clicada = self.get_cor_pela_pos(e.local_x, e.local_y)
#         estado_anterior = self.jogo.estado

#         if estado_anterior == "INICIO" and cor_clicada == "centro":
#             self.jogo.iniciar_novo_jogo()
#         elif estado_anterior == "JOGANDO" and isinstance(cor_clicada, int):
#             self.piscar_cor(cor_clicada, 0.2)
#             self.jogo.registrar_jogada(cor_clicada)
#         elif estado_anterior == "FIM_DE_JOGO" and cor_clicada == "centro":
#             self.jogo.iniciar_novo_jogo()
        
#         if estado_anterior != self.jogo.estado:
#             self.atualizar_visual()
    
#     def atualizar_visual(self):
#         if self.jogo.estado == "INICIO":
#             self.texto_pontos.value = f"Recorde: {self.jogo.recorde}"
#             self.texto_status.value = "Clique em Micro Genius para iniciar"
#         elif self.jogo.estado == "JOGANDO":
#             self.texto_pontos.value = f"Pontos: {len(self.jogo.resposta_jogador)}"
#             self.texto_status.value = "Sua vez!"
#         elif self.jogo.estado == "FIM_DE_JOGO":
#             pontos_finais = len(self.jogo.sequencia) - 1
#             self.texto_pontos.value = f"Recorde: {self.jogo.recorde}"
#             self.texto_status.value = f"Fim de Jogo! Pontuação: {pontos_finais}. Clique em Micro Genius para recomeçar."
        
#         self.update()
        
#         if self.jogo.estado == "MOSTRANDO":
#             self.mostrar_sequencia()

#     def mostrar_sequencia(self):
#         self.tabuleiro_interativo.disabled = True
#         self.texto_status.value = "Observe..."
#         self.update()
#         time.sleep(1)

#         for cor_id in self.jogo.sequencia:
#             self.texto_pontos.value = f"Pontos: {len(self.jogo.sequencia)}"
#             self.piscar_cor(cor_id, 0.5)
#             time.sleep(0.2)
        
#         self.jogo.estado = "JOGANDO"
#         self.tabuleiro_interativo.disabled = False
#         self.atualizar_visual()

#     def piscar_cor(self, cor_id, duracao_s):
#         self.quadrantes[cor_id].paint.color = CORES_CLARO[cor_id]
#         self.update()
#         time.sleep(duracao_s)
#         self.quadrantes[cor_id].paint.color = CORES_ESCURO[cor_id]
#         self.update()

#     def get_cor_pela_pos(self, x, y):
#         if (x - 201)**2 + (y - 201)**2 <= 80**2: return "centro"
#         if 0 <= x <= 200 and 0 <= y <= 200: return 0
#         if 202 <= x <= 402 and 0 <= y <= 200: return 1
#         if 0 <= x <= 200 and 202 <= y <= 402: return 2
#         if 202 <= x <= 402 and 202 <= y <= 402: return 3
#         return None

# # --- FUNÇÃO PRINCIPAL QUE INICIA A APLICAÇÃO (agora síncrona) ---
# def main(page: ft.Page):
#     page.title = "Genius com Flet"
#     page.window_width = 600
#     page.window_height = 650
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.bgcolor = CINZA
    
#     app = AppGenius()
#     page.add(app)

# # --- INICIA O JOGO ---
# ft.app(target=main, view=ft.WEB_BROWSER)

import flet as ft
from flet.canvas import Canvas, Rect, Circle, Text
from random import randrange
import os
from pathlib import Path
import time

# --- CONSTANTES ---
CORES_ESCURO = ["#009600", "#960000", "#969600", "#000096"]
CORES_CLARO = ["#00FF00", "#FF0000", "#FFFF00", "#0000FF"]
PRETO, BRANCO, CINZA = "#000000", "#FFFFFF", "#EAEAEA"
BASE_DIR = Path(__file__).resolve().parent
ARQUIVO_RECORDE = BASE_DIR / "recorde.txt"

# --- CLASSE PARA A LÓGICA DO JOGO ("CÉREBRO") ---
class JogoGenius:
    # (Nenhuma mudança nesta classe, ela não se importa com som)
    def __init__(self):
        self.sequencia = []
        self.resposta_jogador = []
        self.estado = "INICIO"
        self.recorde = self.carregar_recorde()
    def carregar_recorde(self):
        if not os.path.exists(ARQUIVO_RECORDE): return 0
        with open(ARQUIVO_RECORDE, "r") as f:
            try: return int(f.read().strip())
            except: return 0
    def salvar_recorde(self):
        pontos = len(self.sequencia) - 1
        if pontos > self.recorde:
            self.recorde = pontos
            with open(ARQUIVO_RECORDE, "w") as f: f.write(str(self.recorde))
    def iniciar_novo_jogo(self):
        self.sequencia = [randrange(4)]
        self.resposta_jogador = []
        self.estado = "MOSTRANDO"
    def proximo_nivel(self):
        self.sequencia.append(randrange(4))
        self.resposta_jogador = []
        self.estado = "MOSTRANDO"
    def registrar_jogada(self, cor_id):
        if self.estado != "JOGANDO": return
        self.resposta_jogador.append(cor_id)
        if self.resposta_jogador[-1] != self.sequencia[len(self.resposta_jogador) - 1]:
            self.salvar_recorde()
            self.estado = "FIM_DE_JOGO"
            return
        if len(self.resposta_jogador) == len(self.sequencia):
            self.proximo_nivel()

# --- CLASSE PARA A APLICAÇÃO FLET ("ROSTO") ---
class AppGenius(ft.Column):
    def __init__(self):
        super().__init__()
        self.jogo = JogoGenius()
        
        # --- PASSO 1: PREPARAR OS SONS ---
        # Criamos um dicionário de controles de áudio, um para cada som.
        self.sons = {
            0: ft.Audio(src="sons/som_verde.wav"),
            1: ft.Audio(src="sons/som_vermelho.wav"),
            2: ft.Audio(src="sons/som_amarelo.wav"),
            3: ft.Audio(src="sons/som_azul.wav"),
        }

        self.texto_pontos = ft.Text(f"Recorde: {self.jogo.recorde}", size=24, weight=ft.FontWeight.BOLD)
        self.texto_status = ft.Text("Clique em Micro Genius para iniciar", size=18)
        
        self.quadrantes = {
            i: Rect(paint=ft.Paint(color=CORES_ESCURO[i]), **kwargs)
            for i, kwargs in enumerate([
                {"x": 0, "y": 0, "width": 200, "height": 200, "border_radius": ft.border_radius.only(top_left=200)},
                {"x": 202, "y": 0, "width": 200, "height": 200, "border_radius": ft.border_radius.only(top_right=200)},
                {"x": 0, "y": 202, "width": 200, "height": 200, "border_radius": ft.border_radius.only(bottom_left=200)},
                {"x": 202, "y": 202, "width": 200, "height": 200, "border_radius": ft.border_radius.only(bottom_right=200)},
            ])
        }
        
        self.canvas_jogo = Canvas(width=402, height=402, shapes=self.criar_formas_base())
        
        self.tabuleiro_interativo = ft.GestureDetector(
            content=self.canvas_jogo,
            on_tap_down=self.ao_clicar,
        )

        self.controls = [
            self.texto_pontos,
            self.tabuleiro_interativo,
            self.texto_status
        ]
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def did_mount(self):
        """Adiciona os controles de áudio à página quando o app montar."""
        # --- PASSO 2: ADICIONAR OS TOCADORES À PÁGINA ---
        # Os controles de áudio precisam estar na página para funcionar.
        for audio_control in self.sons.values():
            self.page.overlay.append(audio_control)
        self.page.update()

    def tocar_som(self, cor_id):
        """Toca o som correspondente à cor."""
        # --- PASSO 3: TOCAR O SOM ---
        self.sons[cor_id].play()

    def criar_formas_base(self):
        return list(self.quadrantes.values()) + [
            Circle(x=201, y=201, radius=90, paint=ft.Paint(color=CINZA)),
            Circle(x=201, y=201, radius=80, paint=ft.Paint(color=PRETO)),
            Text(x=201, y=201, text="Micro Genius", text_align=ft.TextAlign.CENTER,
                 style=ft.TextStyle(size=25, color=BRANCO, weight=ft.FontWeight.BOLD),
                 alignment=ft.alignment.center),
        ]

    def ao_clicar(self, e: ft.TapEvent):
        if self.tabuleiro_interativo.disabled:
            return
            
        cor_clicada = self.get_cor_pela_pos(e.local_x, e.local_y)
        estado_anterior = self.jogo.estado

        if estado_anterior == "INICIO" and cor_clicada == "centro":
            self.jogo.iniciar_novo_jogo()
        elif estado_anterior == "JOGANDO" and isinstance(cor_clicada, int):
            self.tocar_som(cor_clicada) # Toca o som do clique
            self.piscar_cor(cor_clicada, 0.2)
            self.jogo.registrar_jogada(cor_clicada)
        elif estado_anterior == "FIM_DE_JOGO" and cor_clicada == "centro":
            self.jogo.iniciar_novo_jogo()
        
        if estado_anterior != self.jogo.estado:
            self.atualizar_visual()
    
    def atualizar_visual(self):
        if self.jogo.estado == "INICIO":
            self.texto_pontos.value = f"Recorde: {self.jogo.recorde}"
            self.texto_status.value = "Clique em Micro Genius para iniciar"
        elif self.jogo.estado == "JOGANDO":
            self.texto_pontos.value = f"Pontos: {len(self.jogo.resposta_jogador)}"
            self.texto_status.value = "Sua vez!"
        elif self.jogo.estado == "FIM_DE_JOGO":
            pontos_finais = len(self.jogo.sequencia) - 1
            self.texto_pontos.value = f"Recorde: {self.jogo.recorde}"
            self.texto_status.value = f"Fim de Jogo! Pontuação: {pontos_finais}. Clique para recomeçar."
        
        self.update()
        
        if self.jogo.estado == "MOSTRANDO":
            self.mostrar_sequencia()

    def mostrar_sequencia(self):
        self.tabuleiro_interativo.disabled = True
        self.texto_status.value = "Observe..."
        self.update()
        time.sleep(1)

        for cor_id in self.jogo.sequencia:
            self.texto_pontos.value = f"Pontos: {len(self.jogo.sequencia)}"
            self.tocar_som(cor_id) # Toca o som da sequência
            self.piscar_cor(cor_id, 0.5)
            time.sleep(0.2)
        
        self.jogo.estado = "JOGANDO"
        self.tabuleiro_interativo.disabled = False
        self.atualizar_visual()

    def piscar_cor(self, cor_id, duracao_s):
        self.quadrantes[cor_id].paint.color = CORES_CLARO[cor_id]
        self.update()
        time.sleep(duracao_s)
        self.quadrantes[cor_id].paint.color = CORES_ESCURO[cor_id]
        self.update()

    def get_cor_pela_pos(self, x, y):
        if (x - 201)**2 + (y - 201)**2 <= 80**2: return "centro"
        if 0 <= x <= 200 and 0 <= y <= 200: return 0
        if 202 <= x <= 402 and 0 <= y <= 200: return 1
        if 0 <= x <= 200 and 202 <= y <= 402: return 2
        if 202 <= x <= 402 and 202 <= y <= 402: return 3
        return None

# --- FUNÇÃO PRINCIPAL ---
def main(page: ft.Page):
    page.title = "Genius com Flet"
    page.window_width = 600
    page.window_height = 650
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = CINZA
    
    # --- PASSO 4: ADICIONAR PASTA DE ASSETS ---
    # Informa ao Flet onde encontrar a pasta "sons"
    page.assets_dir = "sons"

    app = AppGenius()
    page.add(app)

# --- INICIA O JOGO ---
# Use ft.app(target=main) para rodar como app de desktop
ft.app(target=main, view=ft.WEB_BROWSER)