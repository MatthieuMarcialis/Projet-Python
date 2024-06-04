from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter.filedialog import askopenfilename
from trajectory.pose_subscriber import Subscriber, Odometry
import rospy
from std_msgs.msg import String
# from geometry_msgs.msg import Twist
import matplotlib.animation as animation  


"""Initialisation de la fenêtre principale"""
root = Tk()
root.geometry('1920x1080')
root.title('Turtle Bot Pilot Program')
root.resizable(height = True, width = True)

"""Connexion au Turtle Bot"""
def connexion():
    URI = URI.get()
    Hostname = Hostname.get()


URI = StringVar()
Hostname = StringVar()

frm_link = Label(root, height = 8, width = 40, relief = SUNKEN)
frm_link_title = Label(frm_link, text = "Connexion au Turtle Bot | Attente de connexion")
frm_link_status = Label(frm_link, text = "Test")
frm_URI = Label(frm_link, text = "URI:")
frm_Hostname = Label(frm_link, text = "Hostname:")
entry_URI = Entry(frm_link, textvariable = URI)
entry_Hostname = Entry(frm_link, textvariable = Hostname)
button_link = Button(frm_link, text = "Connexion", command = connexion, relief = GROOVE)

frm_link.place(x = "5", y = "5")
frm_link_title.place(x = "0", y = "0")
frm_URI.place(x = "0", y = "25")
frm_Hostname.place(x = "0", y = "50")
entry_URI.place(x = "25", y = "25")
entry_Hostname.place(x = "62", y = "50")
button_link.place(x = "5", y = "75")
frm_link_status.place(x = "0", y = "100")

"""Marche/Arrêt Turtle Bot"""

def start():
    if indicator_light['fill'] == "red":
        indicator_space.itemconfig(indicator_light, fill = "green")
        connexion()

def stop():
    indicator_space.itemconfig(indicator_light, fill = "red")
    



frm_OnOff = Label(root, height = 4, width = 17, relief = SUNKEN)
frm_acq_title = Label(frm_OnOff, text = "Etat du Turtle Bot")
button_start = Button(frm_OnOff, text="Start", command=start)
button_stop = Button(frm_OnOff, text="Stop", command=stop)
indicator_space = Canvas(frm_OnOff, height = 15, width = 15)
indicator_light = indicator_space.create_oval(2,2,15,15, fill = "red")

frm_OnOff.place(x = "300", y = "5")
frm_acq_title.place(x = "0", y = "0")
button_start.place(x = "5", y = "30")
button_stop.place(x = "75", y = "30")
indicator_space.place(x = "100", y = "2")

def set_lin(event):
    global lin_mot
    if isinstance(event, str):
        lin_mot = int(val_lin.get())
    else:
        lin_mot = lin_speed.get()

def set_ang(event):
    global ang_mot
    if isinstance(event, str):
        ang_mot = int(val_rot.get())
    else:
        ang_mot = rot_speed.get()

lin_speed = IntVar()
rot_speed = IntVar()
val_lin = StringVar()
val_rot = StringVar()

frm_speed = Label(root, height = 25, width = 40, relief = GROOVE)
frm_speed_title = Label(frm_speed, text = "Vitesses du Turtle Bot")
frm_lin_speed = Label(frm_speed, height = 10, width = 15, relief = SUNKEN)
frm_rot_speed = Label(frm_speed, height = 10, width = 15, relief = SUNKEN)
frm_lin_speed_title = Label(frm_lin_speed, text = "Vitesse linéaire")
frm_rot_speed_title = Label(frm_rot_speed, text = "Vitesse de rotation")
slider_lin_speed = Scale(frm_lin_speed, from_=100, to=0, variable = val_lin, command = set_lin)
slider_rot_speed = Scale(frm_rot_speed, from_=100, to=0, variable = val_rot, command = set_ang)
entry_lin_speed = Entry(frm_lin_speed, textvariable = lin_speed, width = 7)
entry_rot_speed = Entry(frm_rot_speed, textvariable = rot_speed, width = 7)

fwd_sqr = Button(frm_speed, height = 2, width = 5, relief = RAISED)
bck_sqr = Button(frm_speed, height = 2, width = 5, relief = RAISED)
lft_sqr = Button(frm_speed, height = 2, width = 5, relief = RAISED)
rgt_sqr = Button(frm_speed, height = 2, width = 5, relief = RAISED)

slider_lin_speed.bind("<Return>", lambda event: entry_lin_speed.configure(textvariable=str(val_lin)))
entry_lin_speed.bind("<Return>", lambda event: slider_lin_speed.configure(variable=int(lin_speed)))
slider_rot_speed.bind("<Return>", lambda event: entry_rot_speed.configure(textvariable=str(val_rot)))
entry_rot_speed.bind("<Return>", lambda event: slider_rot_speed.configure(variable=int(rot_speed)))
fwd_sqr.bind('<Up>')
bck_sqr.bind('<Down>')
lft_sqr.bind('<Left>')
rgt_sqr.bind('<Right>')

frm_speed.place(x = "5", y = "175")
frm_speed_title.place(x = "75", y = "0")
frm_lin_speed.place(x = "5", y = "25")
frm_rot_speed.place(x = "165", y = "25")
frm_lin_speed_title.place(x = "0", y = "0")
frm_rot_speed_title.place(x = "0", y = "0")
slider_lin_speed.place(x = "50", y = "25")
slider_rot_speed.place(x = "50", y = "25")
entry_lin_speed.place(x = "5", y = "25")
entry_rot_speed.place(x = "5", y = "25")
fwd_sqr.place(x = "120", y = "190")
bck_sqr.place(x = "120", y = "240")
lft_sqr.place(x = "70", y = "240")
rgt_sqr.place(x = "170", y = "240")

"""Type de Pilotage"""
def switch_pilot():
    if button_pilot_status['text'] == "Automatique":
        button_pilot_status['text'] = "Manuel"
        button_trajectory['state'] = "normal"
    else:
        button_pilot_status['text'] = "Automatique"
        button_trajectory['state'] = "disabled"

def find_trajectory():
    global filesearch
    filesearch = askopenfilename(initialdir = "/", title = "Choisissez une trajectoire", filetypes = [("Json","*.json")])
    button_trajectory.config(text = "Trajectoire:"+filesearch)
    root.update()
    execute_trajectory()
    button_trajectory['state'] = "disabled"
    button_pilot_status['state'] = "disabled"
    

def execute_trajectory():
    subcriber = Subscriber("/odom", Odometry, callback=trajectory)

frm_pilot = Label(root, height = 20, width = 30, relief = SUNKEN)
frm_pilot_title = Label(frm_pilot, text = "Type de Pilotage")
button_pilot_status = Button(frm_pilot, text = "Automatique", command = switch_pilot)
button_trajectory = Button(frm_pilot, text = "Donner une trajectoire", command = find_trajectory)

frm_pilot.place(x = "300", y = "80")
frm_pilot_title.pack(side = TOP)
button_pilot_status.pack(expand = YES)
button_trajectory.pack(side = BOTTOM)


"""Visualisation de la carte"""
frm_plt = Label(root, relief = SUNKEN)
frm_plt_title = Label(frm_plt, text = "Position du Turtle Bot")
plt_pos = Figure(figsize = (10, 10), dpi = 100) 

frm_plt.place(x = "1000", y = "5")
frm_plt_title.pack(side = TOP)

plot1 = plt_pos.add_subplot(111)  
canvas = FigureCanvasTkAgg(plt_pos, master = frm_plt)   

def update_map():
    plot1.scatter(x_list[-1],y_list[-1])
    canvas.draw()

x_list = [0.0]
y_list = [0.0]

def trajectory(message: Odometry):
    x_list.append(message.pose.position.x)
    y_list.append(message.pose.position.y)
    print(message.pose)
    update_map()



canvas.draw() 
canvas.get_tk_widget().pack()





"""Afficache de l'interface"""
root.mainloop()

