from tkinter import *
from datetime import datetime, timedelta
import csv
import os
from tkinter import messagebox

firs_list = ['SBAZ', 'SBCW', 'SBBS', 'SBRE', 'SBAO']
envios_list = ['OPMET', 'SIMM', 'MHS']

class FunctionsAM:
    def air_clear_all(self):
        self.out_msg.delete("1.0", "end")  # Limpa o conteúdo da caixa de texto
        self.airmet_list = []  # Limpa a lista temporária de AIRMETs

        # Reinicia o número sequencial com base no arquivo CSV
        last_seq_number = self.get_last_seq_number(
            f"./AIRMET/{self.check_firs.get()}/AIRMET {self.check_firs.get()} {datetime.now().strftime('%d-%m-%Y')}.csv"
        )
        self.air_number = last_seq_number + 1  # Define o próximo número como o próximo na sequência

    def air_change_color_w(self):
        self.mov_ent.config(bg='white')
    
    def air_change_color_r(self):
        self.mov_ent.config(bg='red')

    def air_atualizar_validade(self):
        if self.var_use_actual.get() == 1:
            data_hora_utc = (datetime.now(self.utc_zone) + timedelta(minutes=2)).strftime("%H%M")
            self.valid_1.delete(0, END)
            self.valid_1.insert(0, data_hora_utc)
            self.valid_1.config(state='readonly')
        else:
            self.valid_1.config(state='normal')
            self.valid_1.delete(0, END)

    def air_limpar_coord(self, coord):
        coord.delete(1.0, END)

    def air_check_error(self):
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

    def air_copy_all_func(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.out_msg.get('1.0', END))

    def air_create_csv(self):     
        self.has_saved = True
        if not hasattr(self, "airmet_list") or not self.airmet_list:
            print("Nenhuma mensagem para salvar.")
            return

        # Define o caminho do arquivo CSV
        date_str = datetime.now(self.utc_zone).strftime("%d-%m-%Y")
        caminho_pasta = f"./AIRMET/{self.check_firs.get()}"
        os.makedirs(caminho_pasta, exist_ok=True)
        file_name = f"AIRMET {self.check_firs.get()} {date_str}.csv"
        caminho_arquivo = os.path.join(caminho_pasta, file_name)
        
        # Escreve as mensagens no arquivo CSV
        with open(caminho_arquivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for airmet in self.airmet_list:
                writer.writerow([airmet["message"].strip()])
        print(f"Arquivo CSV '{file_name}' atualizado com sucesso!")
        
        # Limpa a lista temporária após salvar
        self.airmet_list = []

    def air_ask_clr_msg(self):
        if self.has_saved == False:
            answer = messagebox.askyesno('Salvamento', 'Deseja salvar as mensagens no CSV?')
            if answer == 'yes':
                self.create_csv()
            else:
                self.clear_all()
        else:
            self.clear_all()

    def air_get_last_seq_number(self, file_name): 
        """Obtém o último número sequencial das mensagens no arquivo CSV.""" 
        if not os.path.exists(file_name): 
            return 0

        last_seq_number = 0

        with open(file_name, mode='r', encoding='utf-8') as file: 
            reader = csv.reader(file)
            for row in reader:
                if row:
                    last_message = row[0].strip()
                    if "AIRMET" in last_message: 
                        try:
                            air_number = last_message.split("AIRMET")[1].split()[0]
                            if air_number.isdigit(): 
                                last_seq_number = int(air_number)
                        except (IndexError, ValueError):
                            continue
        
        return last_seq_number

    def air_create_msg(self):
        self.has_saved = False
        if not hasattr(self, "airmet_list"):
            self.airmet_list = []

        self.fir_name = ''
        self.info = ''
        self.direction = ''

        if self.multi_var.get() == 0:
            self.ask_clr_msg()

        if len(self.airmet_list) > 0:
            self.air_number = self.airmet_list[-1]["seq_number"] + 1
        elif self.out_msg.get(END) != '':
            self.air_number += 1
        else:
            last_seq_number = self.get_last_seq_number(
                f"./AIRMET/{self.check_firs.get()}/AIRMET {self.check_firs.get()} {datetime.now().strftime('%d-%m-%Y')}.csv"
            )
            self.air_number = last_seq_number + 1

        self.fir_name = {
            "SBAZ": "AMAZONICO",
            "SBCW": "CURITIBA",
            "SBBS": "BRASILIA",
            "SBRE": "RECIFE",
            "SBAO": "ATLANTICO",
        }.get(self.check_firs.get(), '')

        if self.mov_type.get() == 'MOV':
            self.direction = f'{self.mov_ent.get()} '
        else:
            self.direction = ''

        message = f'''WBAZ23 SBGL {(datetime.now(self.utc_zone) - timedelta(minutes=5)).strftime("%d%H%M")}
{self.check_firs.get()} AIRMET {self.air_number} VALID {self.formato_personalizado}{self.valid_1.get()}/{self.valid_2.get()} {self.check_firs.get()} - {self.check_firs.get()} {self.fir_name} FIR {self.fcst_type.get()} WI {self.ent_coord_1.get('1.0', END)} {self.mov_type.get()} {self.direction}{self.status_type.get()}= \n\n'''

        self.out_msg.insert(END, message)
        self.airmet_list.append({
            "seq_number": self.air_number,
            "message": message
        })

    def air_ts_true(self):
        pass
    def air_ts_false(self):
        pass
