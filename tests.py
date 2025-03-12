from tkinter import *
from tkinter import ttk
from sigtab import *
from functions_sm import FunctionsSM
from functions_am import FunctionsAM
from airtab import *

root = Tk()

class Application(SigmetTab, AirmetTab, FunctionsAM, FunctionsSM):
    def __init__(self):
        self.root = root
        self.root.iconbitmap('./images/cimaer.ico')
        self.is_ts = True
        self.has_saved = True

        self.h1var = StringVar()
        self.h2var = StringVar()
        self.air_h1var = StringVar()
        self.air_h2var = StringVar()
        self.topvar = StringVar()
        self.air_topvar = StringVar()
        self.L1var = StringVar()
        self.L2var = StringVar()
        self.air_L1var = StringVar()
        self.air_L2var = StringVar()
        self.mov_var = StringVar()
        self.air_mov_var = StringVar()
        self.sig_type = StringVar()
        self.air_type = StringVar()
        self.op_var = StringVar()
        self.air_op_var = StringVar()

        self.var_use_actual = IntVar()
        self.air_var_use_actual = IntVar()
        self.multi_var = IntVar()
        self.air_multi_var = IntVar()
        self.multi_var.set(1)
        self.air_multi_var.set(1)
        self.previsor_var = StringVar()
        self.air_previsor_var = StringVar()

        self.sig_type.set('EMBD TS')
        self.air_type.set('SFC VIS')
        self.fcst_type = StringVar()
        self.fcst_type.set('FCST')
        self.air_fcst_type = StringVar()
        self.air_fcst_type.set('FCST')
        self.mov_type = StringVar()
        self.mov_type.set('STNR')
        self.air_mov_type = StringVar()
        self.air_mov_type.set('STNR')
        self.status_type = StringVar()
        self.status_type.set('NC')
        self.air_status_type = StringVar()
        self.air_status_type.set('NC')

        self.sig_number = 0
        self.air_number = 0

        self.tela()
        self.notebook()
        self.frames()
        self.sigtab()
        self.airtab()
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
        self.frame_2 = Frame(self.airframe, bd=2, bg='#009DE0', highlightbackground='yellow', highlightthickness=3)
        self.frame_2.place(relx=0.57, rely=0.02, relwidth=0.42, relheight=0.55)

Application()
