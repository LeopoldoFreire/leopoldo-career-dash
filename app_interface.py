import customtkinter as ctk
import motor_busca
import csv
import os

# Configurações de Design
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CareerDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Leopoldo's Career Dash")
        self.geometry("900x600")
        
        # Grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Painel Lateral
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.logo = ctk.CTkLabel(self.sidebar, text="🚀 Carreira Dash", font=("Arial", 20, "bold"))
        self.logo.pack(pady=20)
        
        self.btn_search = ctk.CTkButton(self.sidebar, text="Coletar Vagas", command=self.fetch_jobs)
        self.btn_search.pack(pady=10)
        
        # Lista de Vagas
        self.vaga_list = ctk.CTkScrollableFrame(self.sidebar, label_text="Minhas Vagas")
        self.vaga_list.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Painel Central
        self.main_panel = ctk.CTkFrame(self, corner_radius=10)
        self.main_panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        self.btn_gen = ctk.CTkButton(self.main_panel, text="Gerar Carta de Apresentação", command=self.generate_cover_letter, height=50)
        self.btn_gen.pack(pady=50)

    def fetch_jobs(self):
        motor_busca.coletar_vagas()
        self.refresh_list()

    def refresh_list(self):
        for widget in self.vaga_list.winfo_children():
            widget.destroy()
        
        if os.path.exists('/home/tellinus/Scripts/Automacao_Carreira/vagas_diarias.csv'):
            with open('/home/tellinus/Scripts/Automacao_Carreira/vagas_diarias.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.add_job_item(row['cargo'], "Pendente")

    def add_job_item(self, title, status):
        frame = ctk.CTkFrame(self.vaga_list)
        frame.pack(fill="x", pady=5)
        ctk.CTkLabel(frame, text=title[:25] + "...", font=("Arial", 11)).pack(side="left", padx=5)
        ctk.CTkLabel(frame, text=status, text_color="orange", font=("Arial", 10)).pack(side="right", padx=5)

    def generate_cover_letter(self):
        # Placeholder para integração futura com LLM e contexto do Codex
        print("Gerando carta de apresentação personalizada...")
        # Lógica: ler perfil do Codex e adaptar aos dados da vaga.
