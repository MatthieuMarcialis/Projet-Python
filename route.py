from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from trajectory.pose_subscriber import Subscriber, Odometry
import sys

"""Programme servant d'exemple et de répertoire de fonctions utiles pour Tkinter


root = Tk()
root.geometry('800x400')
root.title('Programme initial')
root['bg'] = 'red'
root.resizable(height = True, width = True)

label1 = Label(root, text = "Label1", font=("Verdana",20,"italic"), width = 20, height = 20, fg = "blue", bg = "green")
label1.place(x = '50', y = '50')
label2 = Label(root, text = "Label2", font=("Verdana",20,"italic"), width = 20, height = 20, fg = "blue", bg = "green")
label2['text'] = "ceci est un test"
label2.place(x = "500", y= "50")


def say_hello():
    label1['text'] = "bouton appuyé"
button1 = Button(root, text = "Click here", bg = 'blue', fg = 'green', command = say_hello)
button1.place(x = "150", y = "200")

def function():
    variable = my_variable.get()
    if variable == "Test":
        label4['text'] = "test done"
    else:
        label4['text'] = "test failed succesfully" 
my_variable = StringVar()
label4 = Label(root, text = "modifiable text", height = 10, width = 50)
label4.place(x = "500", y = "500")
entry = Entry(root, textvariable = my_variable, width = 50)
entry.place(x = "510", y = "500")
button2 = Button(root, text = "Verify", command = function)
button2.place(x = "520", y = "500")

def sike():
    print("SIKE!")

my_menu = Menu(root)
files = Menu(my_menu)
options = Menu(my_menu, tearoff = 0)
options.add_command(label = "Other", command = sike)
files.add_command(label = "Save file as...")
my_menu.add_cascade(label = "Options", menu = options)
my_menu.add_cascade(label = "Files", menu = files)
root.config(menu = my_menu)


label_middle = Label(root)
label_middle.pack(expand = YES)
label5 = Label(label_middle, text = "First text")
label5.pack(side = RIGHT)
label6 = Label(label_middle, text = "Second text")
label6.pack(side = LEFT)

picture = PhotoImage(file = 'divine_coconut.png')
label7 = Label(root, image = picture)
label7.place(x = "900", y = "200")
root.mainloop()

"""

"""Initialisation de la fenêtre principale"""
root = Tk()
root.geometry('1920x1080')
root.title('Turtle Bot Pilot Program')
root.resizable(height=True, width=True)

"""Création du menu supérieur"""
my_menu = Menu(root)

files = Menu(my_menu, tearoff=0)
files.add_command(label="Save file as...")
options = Menu(my_menu, tearoff=0)
options.add_command(label="Other >")

my_menu.add_cascade(label="Options", menu=options)
my_menu.add_cascade(label="Files", menu=files)

root.config(menu=my_menu)

"""Connexion au Turtle Bot"""


def check_connexion():
    Hostname = Hostname.get()
    URI = URI.get()


URI = StringVar()
Hostname = StringVar()

frm_link = Label(root, height=8, width=40, relief=SUNKEN)
frm_link_title = Label(frm_link, text="Connexion au Turtle Bot | Attente de connexion")
frm_link_status = Label(frm_link, text="Test")
frm_URI = Label(frm_link, text="URI:")
frm_Hostname = Label(frm_link, text="Hostname:")
entry_URI = Entry(frm_link, textvariable=URI)
entry_Hostname = Entry(frm_link, textvariable=Hostname)
button_link = Button(frm_link, text="Connexion", command=check_connexion, relief=GROOVE)

frm_link.place(x="5", y="5")
frm_link_title.place(x="0", y="0")
frm_URI.place(x="0", y="25")
frm_Hostname.place(x="0", y="50")
entry_URI.place(x="25", y="25")
entry_Hostname.place(x="62", y="50")
button_link.place(x="5", y="75")
frm_link_status.place(x="0", y="100")

"""Marche/Arrêt Turtle Bot"""


def ma_fonction(message: Odometry):
    print(message.pose)


def start_action():
    """Action to perform when the Start button is clicked."""
    icon_label.config(bg="green")  # Change the icon color to green
    # init_plot()
    subcriber = Subscriber("/odom", Odometry, callback=ma_fonction)


def stop_action():
    """Action to perform when the Stop button is clicked."""
    icon_label.config(bg="red")  # Change the icon color to red
    sys.exit()

def OnOff():
    if button_acq_status['text'] == 'Off':
        button_acq_status['text'] = 'On'
    else:
        button_acq_status['text'] = 'Off'


frm_OnOff = Label(root, height=20, width=10, relief=SUNKEN)
frm_acq_title = Label(frm_OnOff, text="Etat du Turtle Bot")
button_acq_status = Button(frm_OnOff, text="Off", command=OnOff)

frm_OnOff.place(x="300", y="5")
frm_acq_title.pack(side=TOP)
button_acq_status.pack(expand=YES)


# Création d'un bouton Start
#start= Label(root, height=150, width=50)
start_button = Button(root, text="Start", command=start_action)
#start_button.place(x="20",y="50")
start_button.grid(row=3, column=0, columnspan=2)
start_button.pack()

# Création d'un bouton Stop
stop_button = Button(root, text="Stop", command=stop_action)
stop_button.pack()

# Création d'un label pour l'icône (initialisé avec la couleur rouge)
icon_label = Label(root, text="Icône", bg="red", font=("Arial", 12))
icon_label.pack()


"""Contrôle des vitesses du Turtle Bot"""


def actualise1():
    l_speed = lin_speed.get()
    r_speed = rot_speed.get()
    slider_lin_speed(l_speed)


lin_speed = StringVar()
rot_speed = StringVar()

frm_speed = Label(root, height=13, width=40, relief=GROOVE)
frm_speed_title = Label(frm_speed, text="Vitesses du Turtle Bot")
frm_lin_speed = Label(frm_speed, height=10, width=15, relief=SUNKEN)
frm_rot_speed = Label(frm_speed, height=10, width=15, relief=SUNKEN)
frm_lin_speed_title = Label(frm_lin_speed, text="Vitesse linéaire")
frm_rot_speed_title = Label(frm_rot_speed, text="Vitesse de rotation")
slider_lin_speed = Scale(frm_lin_speed, from_=100, to=0)
slider_rot_speed = Scale(frm_rot_speed, from_=100, to=0)
entry_lin_speed = Entry(frm_lin_speed, textvariable=lin_speed, width=7)
entry_rot_speed = Entry(frm_rot_speed, textvariable=rot_speed, width=7)

frm_speed.place(x="5", y="175")
frm_speed_title.place(x="75", y="0")
frm_lin_speed.place(x="5", y="25")
frm_rot_speed.place(x="165", y="25")
frm_lin_speed_title.place(x="0", y="0")
frm_rot_speed_title.place(x="0", y="0")
slider_lin_speed.place(x="50", y="25")
slider_rot_speed.place(x="50", y="25")
entry_lin_speed.place(x="5", y="25")
entry_rot_speed.place(x="5", y="25")

"""Type de Pilotage"""


def switch_pilot():
    if button_pilot_status['text'] == 'Automatique':
        button_pilot_status['text'] = 'Manuel'
    else:
        button_pilot_status['text'] = 'Automatique'


frm_pilot = Label(root, height=20, width=30, relief=SUNKEN)
frm_pilot_title = Label(frm_pilot, text="Type de Pilotage")
button_pilot_status = Button(frm_pilot, text="Automatique", command=switch_pilot)

frm_pilot.place(x="300", y="80")
frm_pilot_title.pack(side=TOP)
button_pilot_status.pack(expand=YES)

"""Visualisation de la carte"""
frm_plt = Label(root, relief=SUNKEN)
frm_plt_title = Label(frm_plt, text="Position du Turtle Bot")
plt_pos = Figure(figsize=(5, 5), dpi=100)

frm_plt.place(x="1000", y="5")
frm_plt_title.pack(side=TOP)
y = [i ** 2 for i in range(101)]

plot1 = plt_pos.add_subplot(111)
plot1.plot(y)
canvas = FigureCanvasTkAgg(plt_pos, master=frm_plt)

canvas.draw()
canvas.get_tk_widget().pack()

# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack()


"""Afficache de l'interface"""
root.mainloop()
