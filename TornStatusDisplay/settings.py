import customtkinter
import math
import json


# Making GUI
version = "v0.0.0"
app = customtkinter.CTk()
app.resizable(False, False)
s_width = app.winfo_screenwidth()
s_height = app.winfo_screenheight()
a = int(math.floor(s_width/2))
b = int(math.floor(s_height/2))
app.geometry(str(a)+"x"+str(b))
app.title("Torn Status Display ("+version+")")
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")
f_w, f_h = int(math.floor(a*0.40)), int(math.floor(b*0.9))

with open("resources/settings.tss", "r") as f:
    settings_data = json.load(f)
fly_delay_var = customtkinter.StringVar(value=settings_data["fly_delay"])
ground_delay_var = customtkinter.StringVar(value=settings_data["ground_delay"])
# EVENTS

time_left_checkbox_val = customtkinter.StringVar(value="on")
def time_left_checkbox_def():
    settings_data["show_time_left"] = time_left_checkbox_val.get()
    print("Show time_left toggled to " + settings_data["show_time_left"])

def apply():
    settings_data["fly_delay"] = int(fly_delay_var.get())
    settings_data["ground_delay"] = int(ground_delay_var.get())
    with open("resources/settings.tss", "w") as f:
        json.dump(settings_data, f, indent=4)
    print("Set fly_delay to "+fly_delay_var.get())
    print("Set ground_delay to "+ground_delay_var.get())
    print("Applied! Saved settings file to `settings.tss`")


def GUISettingsPanel():
    f = customtkinter.CTkFrame(master=app, width=f_w, height=f_h, corner_radius=60)
    l = customtkinter.CTkLabel(f, fg_color="#2e2e2e", text="Settings", width=f_w, text_color="white", height=int(math.floor(f_h*0.1)), font=("Segoe UI", int(math.floor(f_h*0.085))), corner_radius=60)
    c = customtkinter.CTkCheckBox(f, text="Show time_left on your RCP.", command=time_left_checkbox_def, variable=time_left_checkbox_val, onvalue="on", offvalue="off")
    ap = customtkinter.CTkButton(f, text="Apply", command=apply)
    d = customtkinter.CTkFrame(master=f, width=f_w, height=f_h/10, fg_color="transparent")
    dl = customtkinter.CTkLabel(d, fg_color="transparent", text="API request delay (Flying)", width=f_w/2, text_color="white", height=int(math.floor(f_h*0.05)), font=("Segoe UI", int(math.floor(f_h*0.025))))
    e = customtkinter.CTkEntry(d, placeholder_text="Fly delay", textvariable=fly_delay_var)
    d2 = customtkinter.CTkFrame(master=f, width=f_w, height=f_h/10, fg_color="transparent")
    dl2 = customtkinter.CTkLabel(d2, fg_color="transparent", text="API request delay (Grounded)", width=f_w/2, text_color="white", height=int(math.floor(f_h*0.05)), font=("Segoe UI", int(math.floor(f_h*0.025))))
    e2 = customtkinter.CTkEntry(d2, placeholder_text="Ground delay", textvariable=ground_delay_var)

    return f, l, c, ap, d, dl, e, d2, dl2, e2



def GUIPreviewPanel():
    f = customtkinter.CTkFrame(master=app, width=f_w, height=f_h, corner_radius=60)
    l = customtkinter.CTkLabel(f, fg_color="#2e2e2e", text="Preview", width=f_w, text_color="white", height=int(math.floor(f_h*0.1)), font=("Segoe UI", int(math.floor(f_h*0.085))), corner_radius=60)
    l2 = customtkinter.CTkLabel(f, fg_color="transparent", text="COMING SOON", width=f_w, text_color="red", height=int(math.floor(f_h*0.1)), font=("Segoe UI", int(math.floor(f_h*0.085)))) 
    return f, l, l2



def LoadGUI():
    settingsframe.pack(side="left", fill="both", expand=True, padx=int(math.floor(a*0.05)), pady=int(math.floor(b*0.025)))
    previewframe.pack(side="left", fill="both", expand=True, padx=int(math.floor(a*0.05)), pady=int(math.floor(b*0.025)))
    label.pack(pady=(10, 0), padx=25)
    label2.pack(pady=(10, 0), padx=25)
    time_left_checkbox.pack()
    label3.pack()
    dummyframe.pack()
    dummylabel.pack(side="left", fill="x", expand=True)
    fly_d_b.pack(side="left", fill="x", expand=True)
    dummyframe2.pack()
    dummylabel2.pack(side="left", fill="x", expand=True)
    ground_d_b.pack(side="left", fill="x", expand=True)
    
    apply_button.pack()


settingsframe, label, time_left_checkbox, apply_button, dummyframe, dummylabel, fly_d_b, dummyframe2, dummylabel2, ground_d_b  = GUISettingsPanel()
previewframe, label2, label3 = GUIPreviewPanel()
LoadGUI()
app.mainloop()
