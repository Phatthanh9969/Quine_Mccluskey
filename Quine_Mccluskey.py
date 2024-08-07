import customtkinter
import main
import os
import tkinter as tk
from tkinter import ttk
os.system("cls")

window = customtkinter.CTk()
WIDTH=750
HEIGHT=450
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("QUINE MCCLUSKEY")

def combobox_callback(choice):
    selected_value = menumode.get()
    customtkinter.set_appearance_mode(selected_value)
    if selected_value == "light":
        color="green"
    else:
        color="blue"
    customtkinter.set_default_color_theme(color)
    
    button = customtkinter.CTkButton(frame_input, text="Submit", command=submit)
    button.place(relx=360/WIDTH, rely=350/HEIGHT, anchor="center")

    window.mainloop()


def submit():
    #Results

    num = num_entry.get()
    num = sorted(main.input_minterms(num))
    vars = var_entry.get()
    vars = sorted(main.input_letter(vars))
    
    
    # print(minterms)
    
    num_entry.delete(0, len(num_entry.get()))
    var_entry.delete(0, len(var_entry.get()))

    # print(result)

    #STEP 1: =============================================
    caption= customtkinter.CTkLabel(frame_output, text="Step 1: Minterm", fg_color=("white", "grey75"), 
                                    text_color = "black", height=25, width=250, anchor="w")
    
    caption.place(relx=20/WIDTH, rely=50/HEIGHT)

    caption= customtkinter.CTkLabel(frame_output, text=num, anchor="center")
    caption.place(relx=50/WIDTH, rely=80/HEIGHT)
    
    #STEP 2: ================================================
    caption= customtkinter.CTkLabel(frame_output, text="Step 2: Group", fg_color=("white", "grey75"), 
                                    text_color = "black", height=25, width=250, anchor="w")
    
    caption.place(relx=20/WIDTH, rely=110/HEIGHT)
    
    temp = main.group_minterms(num)

    temp=[lst for lst in temp if lst]

    for i in range(len(temp)):
        caption= customtkinter.CTkLabel(frame_output, text=temp[i])
        caption.place(relx=50/WIDTH, rely=(140+i*25)/HEIGHT)
    
    #STEP 3: =================================================
    caption= customtkinter.CTkLabel(frame_output, text="Step 3: Prime Implicants", fg_color=("white", "grey75"), 
                                    text_color = "black", height=25, width=250, anchor="w")
    
    caption.place(relx=20/WIDTH, rely=260/HEIGHT)
    
    minterms = main.quine_mccluskey(num)

    caption= customtkinter.CTkLabel(frame_output, text=minterms)
    caption.place(relx=50/WIDTH, rely=290/HEIGHT)

    #STEP 4: =================================================
    caption= customtkinter.CTkLabel(frame_output, text="Step 4: Convert Implicants", fg_color=("white", "grey75"), 
                                    text_color = "black", height=25, width=250, anchor="w")
    
    caption.place(relx=20/WIDTH, rely=320/HEIGHT)

    result = main.finding_unique_minterms(minterms, vars)
    result = result.replace("+","  ")

    caption= customtkinter.CTkLabel(frame_output, text = result)
    caption.place(relx=50/WIDTH, rely=350/HEIGHT)

    #STEP 5: =================================================
    caption= customtkinter.CTkLabel(frame_output, text="Step 5: Function Minimizations", fg_color=("white", "grey75"), 
                                    text_color = "black", height=25, width=250, anchor="w")
    
    caption.place(relx=20/WIDTH, rely=380/HEIGHT)
    
    result = main.finding_unique_minterms(minterms, vars)
    
    caption= customtkinter.CTkLabel(frame_output, text = result)
    caption.place(relx=50/WIDTH, rely=410/HEIGHT)

    
    


    window.mainloop()

frame_output = customtkinter.CTkFrame(window)
frame_output.place(relx=10/WIDTH, rely=10/HEIGHT, relwidth=250/WIDTH, relheight=431/HEIGHT) 	

frame_input = customtkinter.CTkFrame(window)
frame_input.place(relx=270/WIDTH, rely=10/HEIGHT, relwidth=450/WIDTH, relheight=280/HEIGHT ) 	

frame_extend = customtkinter.CTkFrame(window)
frame_extend.place(relx=270/WIDTH, rely=0.667, relwidth=450/WIDTH, relheight=140/HEIGHT) 	

Label= customtkinter.CTkLabel(frame_input, text="__INPUT__")
Label.place(relx=10/WIDTH, rely=5/HEIGHT)

Label= customtkinter.CTkLabel(frame_output, text="__RESULT__")
Label.place(relx=10/WIDTH, rely=5/HEIGHT)

Label= customtkinter.CTkLabel(frame_extend, text="__EXTEND__")
Label.place(relx=10/WIDTH, rely=5/HEIGHT)

frame_num = customtkinter.CTkLabel(frame_input, text="MINTERMS")
frame_num.place(relx=200/WIDTH, rely=100/HEIGHT)

num_entry = customtkinter.CTkEntry(frame_input, placeholder_text="e.g., 0 1 2 3 ...")
num_entry.place(relx=350/WIDTH, rely=100/HEIGHT)

frame_var = customtkinter.CTkLabel(frame_input, text="VARIABLE" )
frame_var.place(relx=200/WIDTH, rely=180/HEIGHT)

var_entry = customtkinter.CTkEntry(frame_input, placeholder_text="e.g., ABCD")
var_entry.place(relx=350/WIDTH, rely=180/HEIGHT)

#combobox
menumode = customtkinter.CTkComboBox(frame_extend, values=["dark", "light", "system"], command=combobox_callback)
menumode.place(relx=630/WIDTH, rely=400/HEIGHT, anchor="center")
menumode.set("system")

#button
button = customtkinter.CTkButton(frame_input, text="Submit", command=submit)
button.place(relx=360/WIDTH, rely=350/HEIGHT, anchor="center")



window.mainloop()

