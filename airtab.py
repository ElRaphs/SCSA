from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
import pytz
from functions_am import *

firs_list = ['SBAZ', 'SBCW', 'SBBS', 'SBRE', 'SBAO']
envios_list = ['OPMET', 'SIMM', 'MHS']

class AirmetTab(FunctionsAM):
    def airtab(self):
        self.air_utc_zone = pytz.utc
        self.air_data_hora_utc = datetime.now(self.air_utc_zone)
        self.air_formato_personalizado = self.air_data_hora_utc.strftime("%d")

        self.air_multi_selec = Checkbutton(self.airframe, text='Múltiplas mensagens', background='lightblue', variable=self.air_multi_var)
        self.air_multi_selec.place(relx=0.01, y=420)

        #---------------------------------INPUT COORDENADA 1---------------------------------------
        self.air_lb_coord_1 = Label(self.airframe, text='Coordenada 1', background='lightblue')
        self.air_lb_coord_1.place(relx=0.01, rely=0.01)
        self.air_ent_coord_1 = Text(self.airframe, wrap='word')
        self.air_ent_coord_1.place(relx=0.01, rely=0.04, relwidth=0.5, relheight=0.07)
        self.air_clr_coord_1 = Button(self.airframe, text='Limpar', command=lambda: self.air_limpar_coord(self.air_ent_coord_1))
        self.air_clr_coord_1.place(relx=0.52, rely=0.056)

        #---------------------------------INPUT COORDENADA 2---------------------------------------
        # self.air_lb_coord_2 = Label(self.airframe, text='Coordenada 2', background='lightblue')
        # self.air_lb_coord_2.place(relx=0.01, rely=0.12)
        # self.air_ent_coord_2 = Text(self.airframe, wrap='word')
        # self.air_ent_coord_2.place(relx=0.01, rely=0.15, relwidth=0.5, relheight=0.07)
        # self.air_clr_coord_2 = Button(self.airframe, text='Limpar', command=lambda: self.air_limpar_coord(self.air_ent_coord_2))
        # self.air_clr_coord_2.place(relx=0.52, y=125)

        #---------------------------------INPUT COORDENADA 3---------------------------------------
        # self.air_lb_coord_3 = Label(self.airframe, text='Coordenada 3', background='lightblue')
        # self.air_lb_coord_3.place(relx=0.01, y=175)
        # self.air_ent_coord_3 = Text(self.airframe, wrap='word')
        # self.air_ent_coord_3.place(relx=0.01, y=195, relwidth=0.5, relheight=0.07)
        # self.air_clr_coord_3 = Button(self.airframe, text='Limpar', command=lambda: self.air_limpar_coord(self.air_ent_coord_3))
        # self.air_clr_coord_3.place(relx=0.52, y=208)

        #---------------------------------INPUT COORDENADA 4---------------------------------------
        # self.air_lb_coord_4 = Label(self.airframe, text='Coordenada 4', background='lightblue')
        # self.air_lb_coord_4.place(relx=0.01, y=257)
        # self.air_ent_coord_4 = Text(self.airframe, wrap='word')
        # self.air_ent_coord_4.place(relx=0.01, y=277, relwidth=0.5, relheight=0.07)
        # self.air_clr_coord_4 = Button(self.airframe, text='Limpar', command=lambda: self.air_limpar_coord(self.air_ent_coord_4))
        # self.air_clr_coord_4.place(relx=0.52, y=290)

        #---------------------------------INPUT COORDENADA 5---------------------------------------
        # self.air_lb_coord_5 = Label(self.airframe, text='Coordenada 5', background='lightblue')
        # self.air_lb_coord_5.place(relx=0.01, y=339)
        # self.air_ent_coord_5 = Text(self.airframe, wrap='word')
        # self.air_ent_coord_5.place(relx=0.01, y=359, relwidth=0.5, relheight=0.07)
        # self.air_clr_coord_5 = Button(self.airframe, text='Limpar', command=lambda: self.air_limpar_coord(self.air_ent_coord_5))
        # self.air_clr_coord_5.place(relx=0.52, y=372)

        #---------------------------------OUTPUT MENSAGENS-----------------------------------------
        self.air_lb_msg = Label(self.airframe, text='Mensagens:', background='lightblue', font='Arial')
        self.air_lb_msg.place(relx=0.01, y=448)
        self.air_out_msg = Text(self.airframe, wrap='word')
        self.air_out_msg.place(relx=0.01, y= 470, relwidth=0.98, relheight=0.35)
        self.air_copy_all = Button(self.airframe, text='Copiar Tudo', command=lambda: self.air_copy_all_func())
        self.air_copy_all.place(x=1049, y=442)
        self.air_create_msg_button = Button(self.airframe, text='Criar SIGMETs', command=lambda: self.air_check_error())
        self.air_create_msg_button.place(x=960, y=442)
        self.air_del_msg = Button(self.airframe, text='Limpar Mensagens', command=lambda: self.air_ask_clr_msg())
        self.air_del_msg.place(x=1200, y=442)
        self.air_gen_csv_bt = Button(self.airframe, text='Salvar CSV', command=lambda: self.air_create_csv())#, command=lambda: self.air_clr_msg())
        self.air_gen_csv_bt.place(x=1130, y=442)

        #---------------------------------INPUT VALIDADE------------------------------------------
        self.air_lb_valid = Label(self.frame_2, text='Validade:', background='#009DE0')
        self.air_lb_valid.place(relx=0.01, y=5)
        self.air_actual_day = Label(self.frame_2, text=self.air_formato_personalizado, background='#009DE0')
        self.air_actual_day.place(relx=0.01, y=25)
        self.air_lb_bar = Label(self.frame_2, text='/', background='#009DE0')
        self.air_lb_bar.place(x=50, y=25)
        self.air_use_actual = Checkbutton(self.frame_2, text="Usar horário atual + 2'", background='#009DE0', variable=self.air_var_use_actual, command=self.air_atualizar_validade)
        self.air_use_actual.place(x=110, y=24)
        self.air_valid_1 = Entry(self.frame_2, textvariable=self.air_h1var)
        self.air_valid_1.place(x=20, y=26, width=28)
        self.air_valid_2 = Entry(self.frame_2, textvariable=self.air_h2var)
        self.air_valid_2.place(x=60, y=26, width=40)

        #---------------------------------INPUT FIR-----------------------------------------------
        self.air_lb_fir = Label(self.frame_2, text='FIR:', background='#009DE0')
        self.air_lb_fir.place(x=300, y=5)
        self.air_check_firs = ttk.Combobox(self.frame_2, values=firs_list)
        self.air_check_firs.place(x=300, y=25, width=60)

        #---------------------------------INPUT TS------------------------------------------------
        self.air_lb_type = Label(self.frame_2,text='Fenômenos:', background='#009DE0')
        self.air_lb_type.place(relx=0.01, y=80)
        self.air_lb_TS = Label(self.frame_2, text='TS', background='#009DE0')
        self.air_lb_TS.place(relx=0.01, y=100)
        self.air_has_gr = Checkbutton(self.frame_2, text='GR', background='#009DE0')
        self.air_has_gr.place(x=30, y=98)
        self.air_embd_ts = Radiobutton(self.frame_2, text='EMBD TS', background='#009DE0', variable=self.air_type, value='EMBD TS', command=self.air_ts_true)
        self.air_embd_ts.place(relx=0.01, y=120)
        self.air_obsc_ts = Radiobutton(self.frame_2, text='OBSC TS', background='#009DE0', variable=self.air_type, value='OBSC TS', command=self.air_ts_true)
        self.air_obsc_ts.place(relx=0.01, y=150)
        self.air_frq_ts = Radiobutton(self.frame_2, text='FRQ TS', background='#009DE0', variable=self.air_type, value='FRQ TS', command=self.air_ts_true)
        self.air_frq_ts.place(relx=0.01, y=180)
        self.air_sql_ts = Radiobutton(self.frame_2, text='SQL TS', background='#009DE0', variable=self.air_type, value='SQL TS', command=self.air_ts_true)
        self.air_sql_ts.place(relx=0.01, y=210)
        self.air_lb_top = Label(self.frame_2, text='TOP FL', background='#009DE0')
        self.air_lb_top.place(relx=0.01, y=240)
        self.air_top = Entry(self.frame_2, textvariable=self.air_topvar)
        self.air_top.place(x=50, y=240, width=22)

        #---------------------------------INPUT TURB-----------------------------------------------
        self.air_lb_turb = Label(self.frame_2, text='TURB', background='#009DE0')
        self.air_lb_turb.place(x=120, y=100)
        self.air_sev_turb = Radiobutton(self.frame_2, text='SEV TURB', background='#009DE0', variable=self.air_type, value='SEV TURB', command=self.air_ts_false)
        self.air_sev_turb.place(x=120, y=120)

        #---------------------------------INPUT ICE------------------------------------------------
        self.air_lb_ice = Label(self.frame_2, text='ICE', background='#009DE0')
        self.air_lb_ice.place(x=120, y=150)
        self.air_sev_ice = Radiobutton(self.frame_2, text='SEV ICE', background='#009DE0', variable=self.air_type, value='SEV ICE', command=self.air_ts_false)
        self.air_sev_ice.place(x=120, y=180)
        self.air_sev_GRice = Radiobutton(self.frame_2, text='SEV ICE (FZRA)', background='#009DE0', variable=self.air_type, value='SEV ICE (FZRA)', command=self.air_ts_false)
        self.air_sev_GRice.place(x=120, y=210)
        self.air_lb_limits1 = Label(self.frame_2, text='FL', background='#009DE0')
        self.air_lb_limits1.place(x=120, y=240)
        self.air_limits1 = Entry(self.frame_2, textvariable=self.air_L1var)
        self.air_limits1.place(x=135, y=240, width=22)
        self.air_lb_limits_bar = Label(self.frame_2, text='/', background='#009DE0')
        self.air_lb_limits_bar.place(x=155, y=240)
        self.air_limits2 = Entry(self.frame_2, textvariable=self.air_L2var)
        self.air_limits2.place(x=165, y=240, width=22)

        #---------------------------------INPUT CNL-----------------------------------------------
        self.air_cnl = Radiobutton(self.frame_2, text='CANCELAMENTO', background='#009DE0', variable=self.air_type, value='CNL')
        self.air_cnl.place(x=240, y=120)

        #---------------------------------INPUT FCST/OBS------------------------------------------
        self.air_lb_forc = Label(self.frame_2, text='FCST/OBS', background='#009DE0')
        self.air_lb_forc.place(relx=0.01, y=290)
        self.air_fcst = Radiobutton(self.frame_2, text='FCST', background='#009DE0', variable=self.air_fcst_type, value='FCST')
        self.air_fcst.place(relx=0.01, y=310)
        self.air_obs = Radiobutton(self.frame_2, text='OBS', background='#009DE0', variable=self.air_fcst_type, value='OBS')
        self.air_obs.place(relx=0.01, y=340)

        #---------------------------------INPUT STNR/MOV------------------------------------------        
        self.air_lb_stnr = Label(self.frame_2, text='STNR/MOV', background='#009DE0')
        self.air_lb_stnr.place(x=120, y=290)
        self.air_stnr = Radiobutton(self.frame_2, text='STNR', background='#009DE0', variable=self.air_mov_type, value='STNR', command=self.air_change_color_w)
        self.air_stnr.place(x=120, y=310)
        self.air_mov = Radiobutton(self.frame_2, text='MOV', background='#009DE0', variable=self.air_mov_type, value='MOV', command=self.air_change_color_r)
        self.air_mov.place(x=120, y=340)
        self.air_mov_ent = Entry(self.frame_2, textvariable=self.air_mov_var)
        self.air_mov_ent.place(x=125, y=360, width=50)
        #self.air_change_color(self.air_mov_ent, self.air_mov_type.get(), 'MOV')

        #---------------------------------INPUT STATUS------------------------------------------
        self.air_lb_status = Label(self.frame_2, text='STATUS', background='#009DE0')
        self.air_lb_status.place(x=240, y=290)
        self.air_nc = Radiobutton(self.frame_2, text='NC', background='#009DE0', variable=self.air_status_type, value='NC')
        self.air_nc.place(x=240, y=310)
        self.air_wkn = Radiobutton(self.frame_2, text='WKN', background='#009DE0', variable=self.air_status_type, value='WKN')
        self.air_wkn.place(x=240, y=340)
        self.air_intsf = Radiobutton(self.frame_2, text='INTSF', background='#009DE0', variable=self.air_status_type, value='INTSF')
        self.air_intsf.place(x=240, y=370)

        #---------------------------------INPUT ENVIO------------------------------------------
        self.air_lb_op = Label(self.frame_2, text='OPERADOR:', background='#009DE0')
        self.air_lb_op.place(x=340, y=290)
        self.air_op_ent = Entry(self.frame_2, textvariable=self.air_op_var)
        self.air_op_ent.place(x=340, y=310, width=38)
        self.air_lb_env = Label(self.frame_2, text='ENVIO:', background='#009DE0')
        self.air_lb_env.place(x=340, y=340)
        self.air_env_box = ttk.Combobox(self.frame_2, values=envios_list)
        self.air_env_box.set('OPMET')
        self.air_env_box.place(x=340, y=360, width=70)

        #---------------------------------INPUT PREVISOR----------------------------------------
        self.air_lb_previsor = Label(self.frame_2, text='PREVISOR:', background='#009DE0')
        self.air_lb_previsor.place(x=460, y=290)
        self.air_ent_previsor = Entry(self.frame_2, textvariable=self.air_previsor_var)
        self.air_ent_previsor.place(x=440, y=310, width=110)

#---------------------------------INPUT TC------------------------------------------------
#self.air_lb_tc = Label(self.frame_2, text='TC', background='#009DE0')
#self.air_lb_tc.place(x=240, y=100)
#self.air_tc_type = Radiobutton(self.frame_2, text='TC', background='#009DE0', variable=type_option, value='TC')
#self.air_tc_type.place(x=240, y=120)