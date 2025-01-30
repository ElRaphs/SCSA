from tkinter import *
from datetime import datetime, timedelta
import csv
import os
from tkinter import messagebox

firs_list = ['SBAZ', 'SBCW', 'SBBS', 'SBRE', 'SBAO']
envios_list = ['OPMET', 'SIMM', 'MHS']

class FunctionsSM:
    def clear_all(self):
        self.out_msg.delete("1.0", "end")  # Limpa o conteúdo da caixa de texto
        self.sigmet_list = []  # Limpa a lista temporária de SIGMETs

        # Reinicia o número sequencial com base no arquivo CSV
        last_seq_number = self.get_last_seq_number(
            f"./SIGMET/{self.check_firs.get()}/SIGMET {self.check_firs.get()} {datetime.now().strftime('%d-%m-%Y')}.csv"
        )
        self.sig_number = last_seq_number + 1  # Define o próximo número como o próximo na sequência

    def change_color_w(self):
        self.mov_ent.config(bg='white')
    def change_color_r(self):
        self.mov_ent.config(bg='red')

    def atualizar_validade(self):
        if self.var_use_actual.get() == 1:
            data_hora_utc = (datetime.now(self.utc_zone) + timedelta(minutes=2)).strftime("%H%M")
            self.valid_1.delete(0, END)
            self.valid_1.insert(0, data_hora_utc)
            self.valid_1.config(state='readonly')
        else:
            self.valid_1.config(state='normal')
            self.valid_1.delete(0, END)

    def limpar_coord(self, coord):
        coord.delete(1.0, END)

    def check_error(self):
        all_fine = True

        if len(self.valid_1.get()) != 4:
            self.valid_1.configure(bg='red')
            all_fine = False
        else:
            self.valid_1.configure(bg='white')

        if len(self.valid_2.get()) != 6:
            self.valid_2.configure(bg='red')
            all_fine = False
        else:
            self.valid_2.configure(bg='white')

        if self.check_firs.get() == '':
            all_fine = False

        if self.is_ts == True and len(self.top.get()) != 3:
            self.top.configure(bg='red')
            self.limits1.configure(bg='white')
            self.limits2.configure(bg='white')
            all_fine = False
        elif self.is_ts == False:
            if len(self.limits1.get()) != 3 or len(self.limits2.get()) != 3 or (int(self.limits2.get()) - int(self.limits1.get())) < 0:
                self.limits1.configure(bg='red')
                self.limits2.configure(bg='red')
                self.top.configure(bg='white')
                all_fine = False
        else:
            self.limits1.configure(bg='white')
            self.limits2.configure(bg='white')
            self.top.configure(bg='white')

        if len(self.op_ent.get()) != 4:
            self.op_ent.configure(bg='red')
            all_fine = False
        else:
            self.op_ent.configure(bg='white')

        if self.ent_previsor.get() == '':
            self.ent_previsor.configure(bg='red')
            all_fine = False
        else:
            self.ent_previsor.configure(bg='white')

        if all_fine:
            self.create_msg()

    def copy_all_func(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.out_msg.get('1.0', END))

    def create_csv(self):     
        self.has_saved = True
        if not hasattr(self, "sigmet_list") or not self.sigmet_list:
            print("Nenhuma mensagem para salvar.")
            return

        # Define o caminho do arquivo CSV
        date_str = datetime.now(self.utc_zone).strftime("%d-%m-%Y")
        caminho_pasta = f"./SIGMET/{self.check_firs.get()}"
        os.makedirs(caminho_pasta, exist_ok=True)
        file_name = f"SIGMET {self.check_firs.get()} {date_str}.csv"
        caminho_arquivo = os.path.join(caminho_pasta, file_name)
        
        # Escreve as mensagens no arquivo CSV
        with open(caminho_arquivo, mode='a', newline='', encoding='utf-8') as file:  # Modo 'a' para adicionar em vez de sobrescrever
            writer = csv.writer(file)
            for sigmet in self.sigmet_list:
                writer.writerow([sigmet["message"].strip()])  # Remove espaços em branco desnecessários
        print(f"Arquivo CSV '{file_name}' atualizado com sucesso!")
        
        # Limpa a lista temporária após salvar
        self.sigmet_list = []

    def ts_true(self):
        self.is_ts = True
    def ts_false(self):
        self.is_ts = False

    def ask_clr_msg(self):
        if self.has_saved == False:
            answer = messagebox.askyesno('Salvamento', 'Deseja salvar as mensagens no CSV?')
            if answer == 'yes':
                self.create_csv()
            else:
                self.clear_all()
        else:
            self.clear_all()

    def get_last_seq_number(self, file_name): 
        """Obtém o último número sequencial das mensagens no arquivo CSV.""" 
        if not os.path.exists(file_name): 
            return 0  # Arquivo não existe, retorna 0

        last_seq_number = 0  # Número padrão caso não encontre SIGMET

        with open(file_name, mode='r', encoding='utf-8') as file: 
            reader = csv.reader(file)
            for row in reader:
                if row:  # Verifica se a linha não está vazia
                    last_message = row[0].strip()
                    if "SIGMET" in last_message: 
                        try:
                            # Extrai o número logo após "SIGMET"
                            sigmet_number = last_message.split("SIGMET")[1].split()[0]
                            if sigmet_number.isdigit(): 
                                last_seq_number = int(sigmet_number)
                        except (IndexError, ValueError):
                            continue  # Ignora mensagens que não seguem o formato esperado
                        
        return last_seq_number

    def create_msg(self):
        self.has_saved = False
        if not hasattr(self, "sigmet_list"):
            self.sigmet_list = []

        self.fir_name = ''
        self.top_str = ''
        self.limit_str = ''
        self.info = ''
        self.direction = ''

        # Se multi_var estiver desativado, limpa a mensagem de saída
        if self.multi_var.get() == 0:
            self.ask_clr_msg()

        # Determina o número sequencial da SIGMET
        if len(self.sigmet_list) > 0:  # Se já há mensagens criadas nesta sessão
            self.sig_number = self.sigmet_list[-1]["seq_number"] + 1
        elif self.out_msg.get(END) != '':
            self.sig_number += 1
        else:
            last_seq_number = self.get_last_seq_number(
                f"./SIGMET/{self.check_firs.get()}/SIGMET {self.check_firs.get()} {datetime.now().strftime('%d-%m-%Y')}.csv"
            )
            self.sig_number = last_seq_number + 1

        # Define o nome da FIR com base no valor selecionado
        self.fir_name = {
            "SBAZ": "AMAZONICO",
            "SBCW": "CURITIBA",
            "SBBS": "BRASILIA",
            "SBRE": "RECIFE",
            "SBAO": "ATLANTICO",
        }.get(self.check_firs.get(), '')

        # Configurações de `top_str` e `info`
        if self.is_ts:
            self.top_str = 'TOP '
            self.info = self.top.get()
        else:
            self.top_str = ''
            self.info = f'{self.limits1.get()}/{self.limits2.get()}'

        # Configuração do movimento
        if self.mov_type.get() == 'MOV':
            self.direction = f'{self.mov_ent.get()} '
        else:
            self.direction = ''

        # Cria a mensagem SIGMET
        if self.sig_type.get() != 'CNL':
            message = f'''WSBZ23 SBGL {(datetime.now(self.utc_zone) - timedelta(minutes=5)).strftime("%d%H%M")}
{self.check_firs.get()} SIGMET {self.sig_number} VALID {self.formato_personalizado}{self.valid_1.get()}/{self.valid_2.get()} {self.check_firs.get()} - {self.check_firs.get()} {self.fir_name} FIR {self.sig_type.get()} {self.fcst_type.get()} WI {self.ent_coord_1.get('1.0', END)}{self.top_str}FL{self.info} {self.mov_type.get()} {self.direction}{self.status_type.get()}= \n\n'''
        else:
            message = f'''WSBZ23 SBGL {(datetime.now(self.utc_zone) - timedelta(minutes=5)).strftime("%d%H%M")}
{self.check_firs.get()} SIGMET {self.sig_number} VALID {self.formato_personalizado}{self.valid_1.get()}/{self.valid_2.get()} {self.check_firs.get()} - {self.check_firs.get()} {self.fir_name} FIR {self.ent_coord_1.get('1.0', END)}= '''

        # Adiciona a mensagem ao final do widget de saída
        self.out_msg.insert(END, message)

        # Armazena a mensagem na lista temporária
        self.sigmet_list.append({
            "seq_number": self.sig_number,
            "message": message
        })