from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from tkinter import messagebox
import pytz
import csv
import os

sig_types_list = ['EMBD TS', 'SEV TURB', 'SEV ICE']
firs_list = ['SBAZ', 'SBCW', 'SBBS', 'SBRE', 'SBAO']
envios_list = ['OPMET', 'SIMM', 'MHS']
root = Tk()

class Application:
    def __init__(self):
        self.root = root
        self.root.iconbitmap('./images/cimaer.ico')
        self.is_ts = True
        self.has_saved = True
        self.h1var = StringVar()
        self.h2var = StringVar()
        self.topvar = StringVar()
        self.L1var = StringVar()
        self.L2var = StringVar()
        self.mov_var = StringVar()
        self.sig_type = StringVar()
        self.op_var = StringVar()
        self.var_use_actual = IntVar()
        self.multi_var = IntVar()
        self.multi_var.set(1)
        self.previsor_var = StringVar()
        self.sig_type.set('EMBD TS')
        self.fcst_type = StringVar()
        self.fcst_type.set('FCST')
        self.mov_type = StringVar()
        self.mov_type.set('STNR')
        self.status_type = StringVar()
        self.status_type.set('NC')
        self.sig_number = 0
        self.tela()
        self.notebook()
        self.frames()
        self.sigtab()
        root.mainloop()

    def tela(self):
        self.root.title('SMARTSIG')
        self.root.geometry('1380x800')
        self.root.resizable(False, False)

    def notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def frames(self):
        self.sigframe = Frame(self.notebook, bd=2, bg='lightblue', highlightbackground='yellow', highlightthickness=3)
        self.airframe = Frame(self.notebook, bd=2, bg='lightblue', highlightbackground='yellow', highlightthickness=3)

        self.notebook.add(self.sigframe, text='SIGMET')
        self.notebook.add(self.airframe, text='AIRMET')

        self.frame_1 = Frame(self.sigframe, bd=2, bg='#009DE0', highlightbackground='yellow', highlightthickness=3)
        self.frame_1.place(relx=0.57, rely=0.02, relwidth=0.42, relheight=0.55)

    def sigtab(self):
        self.utc_zone = pytz.utc
        self.data_hora_utc = datetime.now(self.utc_zone)
        self.formato_personalizado = self.data_hora_utc.strftime("%d")

        self.multi_selec = Checkbutton(self.sigframe, text='Múltiplas mensagens', background='lightblue', variable=self.multi_var)
        self.multi_selec.place(relx=0.01, y=420)

        #---------------------------------INPUT COORDENADA 1---------------------------------------
        self.lb_coord_1 = Label(self.sigframe, text='Coordenada 1', background='lightblue')
        self.lb_coord_1.place(relx=0.01, rely=0.01)
        self.ent_coord_1 = Text(self.sigframe, wrap='word')
        self.ent_coord_1.place(relx=0.01, rely=0.04, relwidth=0.5, relheight=0.07)
        self.clr_coord_1 = Button(self.sigframe, text='Limpar', command=lambda: self.limpar_coord(self.ent_coord_1))
        self.clr_coord_1.place(relx=0.52, rely=0.056)

        #---------------------------------INPUT COORDENADA 2---------------------------------------
        # self.lb_coord_2 = Label(self.sigframe, text='Coordenada 2', background='lightblue')
        # self.lb_coord_2.place(relx=0.01, rely=0.12)
        # self.ent_coord_2 = Text(self.sigframe, wrap='word')
        # self.ent_coord_2.place(relx=0.01, rely=0.15, relwidth=0.5, relheight=0.07)
        # self.clr_coord_2 = Button(self.sigframe, text='Limpar', command=lambda: self.limpar_coord(self.ent_coord_2))
        # self.clr_coord_2.place(relx=0.52, y=125)

        #---------------------------------INPUT COORDENADA 3---------------------------------------
        # self.lb_coord_3 = Label(self.sigframe, text='Coordenada 3', background='lightblue')
        # self.lb_coord_3.place(relx=0.01, y=175)
        # self.ent_coord_3 = Text(self.sigframe, wrap='word')
        # self.ent_coord_3.place(relx=0.01, y=195, relwidth=0.5, relheight=0.07)
        # self.clr_coord_3 = Button(self.sigframe, text='Limpar', command=lambda: self.limpar_coord(self.ent_coord_3))
        # self.clr_coord_3.place(relx=0.52, y=208)

        #---------------------------------INPUT COORDENADA 4---------------------------------------
        # self.lb_coord_4 = Label(self.sigframe, text='Coordenada 4', background='lightblue')
        # self.lb_coord_4.place(relx=0.01, y=257)
        # self.ent_coord_4 = Text(self.sigframe, wrap='word')
        # self.ent_coord_4.place(relx=0.01, y=277, relwidth=0.5, relheight=0.07)
        # self.clr_coord_4 = Button(self.sigframe, text='Limpar', command=lambda: self.limpar_coord(self.ent_coord_4))
        # self.clr_coord_4.place(relx=0.52, y=290)

        #---------------------------------INPUT COORDENADA 5---------------------------------------
        # self.lb_coord_5 = Label(self.sigframe, text='Coordenada 5', background='lightblue')
        # self.lb_coord_5.place(relx=0.01, y=339)
        # self.ent_coord_5 = Text(self.sigframe, wrap='word')
        # self.ent_coord_5.place(relx=0.01, y=359, relwidth=0.5, relheight=0.07)
        # self.clr_coord_5 = Button(self.sigframe, text='Limpar', command=lambda: self.limpar_coord(self.ent_coord_5))
        # self.clr_coord_5.place(relx=0.52, y=372)

        #---------------------------------OUTPUT MENSAGENS-----------------------------------------
        self.lb_msg = Label(self.sigframe, text='Mensagens:', background='lightblue', font='Arial')
        self.lb_msg.place(relx=0.01, y=448)
        self.out_msg = Text(self.sigframe, wrap='word')
        self.out_msg.place(relx=0.01, y= 470, relwidth=0.98, relheight=0.35)
        self.copy_all = Button(self.sigframe, text='Copiar Tudo', command=lambda: self.copy_all_func())
        self.copy_all.place(x=1049, y=442)
        self.create_msg = Button(self.sigframe, text='Criar SIGMETs', command=lambda: self.check_error())
        self.create_msg.place(x=960, y=442)
        self.del_msg = Button(self.sigframe, text='Limpar Mensagens', command=lambda: self.ask_clr_msg())
        self.del_msg.place(x=1200, y=442)
        self.gen_csv_bt = Button(self.sigframe, text='Salvar CSV', command=lambda: self.create_csv())#, command=lambda: self.clr_msg())
        self.gen_csv_bt.place(x=1130, y=442)

        #---------------------------------INPUT VALIDADE------------------------------------------
        self.lb_valid = Label(self.frame_1, text='Validade:', background='#009DE0')
        self.lb_valid.place(relx=0.01, y=5)
        self.actual_day = Label(self.frame_1, text=self.formato_personalizado, background='#009DE0')
        self.actual_day.place(relx=0.01, y=25)
        self.lb_bar = Label(self.frame_1, text='/', background='#009DE0')
        self.lb_bar.place(x=50, y=25)
        self.use_actual = Checkbutton(self.frame_1, text="Usar horário atual + 2'", background='#009DE0', variable=self.var_use_actual, command=self.atualizar_validade)
        self.use_actual.place(x=110, y=24)
        self.valid_1 = Entry(self.frame_1, textvariable=self.h1var)
        self.valid_1.place(x=20, y=26, width=28)
        self.valid_2 = Entry(self.frame_1, textvariable=self.h2var)
        self.valid_2.place(x=60, y=26, width=40)

        #---------------------------------INPUT FIR-----------------------------------------------
        self.lb_fir = Label(self.frame_1, text='FIR:', background='#009DE0')
        self.lb_fir.place(x=300, y=5)
        self.check_firs = ttk.Combobox(self.frame_1, values=firs_list)
        self.check_firs.place(x=300, y=25, width=60)

        #---------------------------------INPUT TS------------------------------------------------
        self.lb_type = Label(self.frame_1,text='Fenômenos:', background='#009DE0')
        self.lb_type.place(relx=0.01, y=80)
        self.lb_TS = Label(self.frame_1, text='TS', background='#009DE0')
        self.lb_TS.place(relx=0.01, y=100)
        self.has_gr = Checkbutton(self.frame_1, text='GR', background='#009DE0')
        self.has_gr.place(x=30, y=98)
        self.embd_ts = Radiobutton(self.frame_1, text='EMBD TS', background='#009DE0', variable=self.sig_type, value='EMBD TS', command=self.ts_true)
        self.embd_ts.place(relx=0.01, y=120)
        self.obsc_ts = Radiobutton(self.frame_1, text='OBSC TS', background='#009DE0', variable=self.sig_type, value='OBSC TS', command=self.ts_true)
        self.obsc_ts.place(relx=0.01, y=150)
        self.frq_ts = Radiobutton(self.frame_1, text='FRQ TS', background='#009DE0', variable=self.sig_type, value='FRQ TS', command=self.ts_true)
        self.frq_ts.place(relx=0.01, y=180)
        self.sql_ts = Radiobutton(self.frame_1, text='SQL TS', background='#009DE0', variable=self.sig_type, value='SQL TS', command=self.ts_true)
        self.sql_ts.place(relx=0.01, y=210)
        self.lb_top = Label(self.frame_1, text='TOP FL', background='#009DE0')
        self.lb_top.place(relx=0.01, y=240)
        self.top = Entry(self.frame_1, textvariable=self.topvar)
        self.top.place(x=50, y=240, width=22)

        #---------------------------------INPUT TURB-----------------------------------------------
        self.lb_turb = Label(self.frame_1, text='TURB', background='#009DE0')
        self.lb_turb.place(x=120, y=100)
        self.sev_turb = Radiobutton(self.frame_1, text='SEV TURB', background='#009DE0', variable=self.sig_type, value='SEV TURB', command=self.ts_false)
        self.sev_turb.place(x=120, y=120)

        #---------------------------------INPUT ICE------------------------------------------------
        self.lb_ice = Label(self.frame_1, text='ICE', background='#009DE0')
        self.lb_ice.place(x=120, y=150)
        self.sev_ice = Radiobutton(self.frame_1, text='SEV ICE', background='#009DE0', variable=self.sig_type, value='SEV ICE', command=self.ts_false)
        self.sev_ice.place(x=120, y=180)
        self.sev_GRice = Radiobutton(self.frame_1, text='SEV ICE (FZRA)', background='#009DE0', variable=self.sig_type, value='SEV ICE (FZRA)', command=self.ts_false)
        self.sev_GRice.place(x=120, y=210)
        self.lb_limits1 = Label(self.frame_1, text='FL', background='#009DE0')
        self.lb_limits1.place(x=120, y=240)
        self.limits1 = Entry(self.frame_1, textvariable=self.L1var)
        self.limits1.place(x=135, y=240, width=22)
        self.lb_limits_bar = Label(self.frame_1, text='/', background='#009DE0')
        self.lb_limits_bar.place(x=155, y=240)
        self.limits2 = Entry(self.frame_1, textvariable=self.L2var)
        self.limits2.place(x=165, y=240, width=22)

        #---------------------------------INPUT CNL-----------------------------------------------
        self.cnl = Radiobutton(self.frame_1, text='CANCELAMENTO', background='#009DE0', variable=self.sig_type, value='CNL')
        self.cnl.place(x=240, y=120)

        #---------------------------------INPUT FCST/OBS------------------------------------------
        self.lb_forc = Label(self.frame_1, text='FCST/OBS', background='#009DE0')
        self.lb_forc.place(relx=0.01, y=290)
        self.fcst = Radiobutton(self.frame_1, text='FCST', background='#009DE0', variable=self.fcst_type, value='FCST')
        self.fcst.place(relx=0.01, y=310)
        self.obs = Radiobutton(self.frame_1, text='OBS', background='#009DE0', variable=self.fcst_type, value='OBS')
        self.obs.place(relx=0.01, y=340)

        #---------------------------------INPUT STNR/MOV------------------------------------------        
        self.lb_stnr = Label(self.frame_1, text='STNR/MOV', background='#009DE0')
        self.lb_stnr.place(x=120, y=290)
        self.stnr = Radiobutton(self.frame_1, text='STNR', background='#009DE0', variable=self.mov_type, value='STNR', command=self.change_color_w)
        self.stnr.place(x=120, y=310)
        self.mov = Radiobutton(self.frame_1, text='MOV', background='#009DE0', variable=self.mov_type, value='MOV', command=self.change_color_r)
        self.mov.place(x=120, y=340)
        self.mov_ent = Entry(self.frame_1, textvariable=self.mov_var)
        self.mov_ent.place(x=125, y=360, width=50)
        #self.change_color(self.mov_ent, self.mov_type.get(), 'MOV')

        #---------------------------------INPUT STATUS------------------------------------------
        self.lb_status = Label(self.frame_1, text='STATUS', background='#009DE0')
        self.lb_status.place(x=240, y=290)
        self.nc = Radiobutton(self.frame_1, text='NC', background='#009DE0', variable=self.status_type, value='NC')
        self.nc.place(x=240, y=310)
        self.wkn = Radiobutton(self.frame_1, text='WKN', background='#009DE0', variable=self.status_type, value='WKN')
        self.wkn.place(x=240, y=340)
        self.intsf = Radiobutton(self.frame_1, text='INTSF', background='#009DE0', variable=self.status_type, value='INTSF')
        self.intsf.place(x=240, y=370)

        #---------------------------------INPUT ENVIO------------------------------------------
        self.lb_op = Label(self.frame_1, text='OPERADOR:', background='#009DE0')
        self.lb_op.place(x=340, y=290)
        self.op_ent = Entry(self.frame_1, textvariable=self.op_var)
        self.op_ent.place(x=340, y=310, width=38)
        self.lb_env = Label(self.frame_1, text='ENVIO:', background='#009DE0')
        self.lb_env.place(x=340, y=340)
        self.env_box = ttk.Combobox(self.frame_1, values=envios_list)
        self.env_box.set('OPMET')
        self.env_box.place(x=340, y=360, width=70)

        #---------------------------------INPUT PREVISOR----------------------------------------
        self.lb_previsor = Label(self.frame_1, text='PREVISOR:', background='#009DE0')
        self.lb_previsor.place(x=460, y=290)
        self.ent_previsor = Entry(self.frame_1, textvariable=self.previsor_var)
        self.ent_previsor.place(x=440, y=310, width=110)

        #---------------------------------INPUT TC------------------------------------------------
        #self.lb_tc = Label(self.frame_1, text='TC', background='#009DE0')
        #self.lb_tc.place(x=240, y=100)
        #self.tc_type = Radiobutton(self.frame_1, text='TC', background='#009DE0', variable=type_option, value='TC')
        #self.tc_type.place(x=240, y=120)

    #----------------------------------------------------------------------FUNÇÕES------------------------------------------------------------------------
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
            self.create_sigs()

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

    def create_sigs(self):
        print(int(datetime.now(self.utc_zone) - timedelta(minutes=5)).strftime("%d%H%M"))
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

Application()
