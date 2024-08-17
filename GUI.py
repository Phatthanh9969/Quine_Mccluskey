import customtkinter  # Import the customtkinter module for the GUI
import main           # Import the main module which contains the logic for the Quine-McCluskey algorithm
import os             # Import os module to interact with the operating system
os.system("cls")      # Clear the terminal/command prompt

# Create the main window
window = customtkinter.CTk()
WIDTH = 750
HEIGHT = 450
window.geometry(f"{WIDTH}x{HEIGHT}")  # Set the size of the window
window.title("QUINE MCCLUSKEY")  # Set the title of the window

def list_to_string(lst, separator=',  '):
    return separator.join(map(str, lst))

# Function to handle the combobox selection and change appearance mode
def combobox_callback(choice):
    selected_value = menumode.get()  # Get the selected value from the combobox
    customtkinter.set_appearance_mode(selected_value)  # Set the appearance mode (light/dark/system)
    
    # Set color theme based on appearance mode
    if selected_value == "light":
        color = "green"
    else:
        color = "blue"
    customtkinter.set_default_color_theme(color)  # Set the default color theme
    
    # Create and place the submit button
    button = customtkinter.CTkButton(frame_input, text="Submit", command=submit)
    button.place(relx=375/WIDTH, rely=350/HEIGHT, anchor="center")

    window.mainloop()  # Start the main event loop

# Function to handle the submit button click
def submit():

    for widget in frame_output.winfo_children():
       widget.destroy()

    for widget in frame_extend.winfo_children():
       widget.destroy()

    Label = customtkinter.CTkLabel(frame_output, text="__PROGRESS__")
    Label.place(relx=10/WIDTH, rely=5/HEIGHT)

    Label = customtkinter.CTkLabel(frame_extend, text="__RESULT__")
    Label.place(relx=10/WIDTH, rely=5/HEIGHT)

    testNum = True
    testVar = True

    # Validate the number of minterms and variables
    if testNum and testVar:
        num = num_entry.get()  # Get minterms from the entry widget
        vars = var_entry.get()  # Get variables from the entry widget

        temp = num.replace(" ", "")  # Remove spaces from minterms input

        testNum = temp.isdigit()  # Check if the minterms input is numeric
        testVar = vars.isalpha()   # Check if the variables input contains only alphabetic characters

        if testNum:
            num = sorted(main.input_minterms(num))  # Process and sort the minterms input
            testNum = False
        else:
            # Show an error message and reset the minterms input if validation fails
            caption = customtkinter.CTkLabel(frame_input, text="Try Again")
            caption.place(relx=360/WIDTH, rely=150/HEIGHT)

            num_entry.delete(0, len(num_entry.get()))
            num = (0, 10000)

            testNum = True

        if testVar:
            vars = sorted(main.input_letter(vars))  # Process and sort the variables input
            testVar = False
        else:
            # Show an error message and reset the variables input if validation fails
            caption = customtkinter.CTkLabel(frame_input, text="Try Again")
            caption.place(relx=360/WIDTH, rely=150/HEIGHT)

            var_entry.delete(0, len(var_entry.get()))

            testVar = True

    # Check if the number of variables matches the number of bits needed for minterms
    lenght_max_num = len(bin(max(num))) - 2  # Calculate the length of the binary representation of the max minterm
    lenght_max_var = len(vars)  # Get the number of variables

    if lenght_max_var < lenght_max_num or lenght_max_var > lenght_max_num:
        running = False
        # Show an error message if the number of variables doesn't match the number of minterms
        caption = customtkinter.CTkLabel(frame_input, text="Try Again")
        caption.place(relx=360/WIDTH, rely=150/HEIGHT)
    else:
        running = True

    if running:

        num_entry.delete(0, len(num_entry.get()))
        var_entry.delete(0, len(var_entry.get()))
        
        # Clear previous error message
        caption = customtkinter.CTkLabel(frame_input, text="                 ")
        caption.place(relx=360/WIDTH, rely=150/HEIGHT)

        # Step 1: Display the minterms
        caption = customtkinter.CTkLabel(frame_output, text="Step 1: Minterm", fg_color=("white", "grey75"), 
                                         text_color="black", height=25, width=250, anchor="w")
        caption.place(relx=20/WIDTH, rely=50/HEIGHT)

        # num= main.list_to_string(num)
        temp = list_to_string(num)
        temp = "∑m (" + temp + ")"
        
        caption = customtkinter.CTkLabel(frame_output, text=temp, anchor="center")
        caption.place(relx=50/WIDTH, rely=80/HEIGHT)

        # Step 2: Group the minterms
        caption = customtkinter.CTkLabel(frame_output, text="Step 2: Group", fg_color=("white", "grey75"), 
                                         text_color="black", height=25, width=250, anchor="w")
        caption.place(relx=20/WIDTH, rely=110/HEIGHT)
        
        temp = main.group_minterms(num)  # Group minterms using the function from the main module
        temp = [lst for lst in temp if lst]  # Filter out empty lists

        for i in range(len(temp)):
            caption = customtkinter.CTkLabel(frame_output, text=temp[i])
            caption.place(relx=50/WIDTH, rely=(140+i*25)/HEIGHT)

        # Step 3: Find and display the prime implicants
        caption = customtkinter.CTkLabel(frame_output, text="Step 3: Prime Implicants", fg_color=("white", "grey75"), 
                                         text_color="black", height=25, width=250, anchor="w")
        caption.place(relx=20/WIDTH, rely=310/HEIGHT)
        
        minterms = main.quine_mccluskey(num)  # Find prime implicants using the function from the main module
        temp = list_to_string(minterms)
        temp = "F: " + temp
        caption = customtkinter.CTkLabel(frame_output, text=temp)
        caption.place(relx=50/WIDTH, rely=340/HEIGHT)

        # Step 4: Convert implicants to variables
        caption = customtkinter.CTkLabel(frame_output, text="Step 4: Convert Implicants", fg_color=("white", "grey75"), 
                                         text_color="black", height=25, width=250, anchor="w")
        caption.place(relx=20/WIDTH, rely=370/HEIGHT)

        result = main.finding_unique_minterms(minterms, vars)  # Convert prime implicants to variables
        result = result.replace("+", "  ")

        caption = customtkinter.CTkLabel(frame_output, text=result)
        caption.place(relx=50/WIDTH, rely=400/HEIGHT)

        # Step 5: Display the minimized function
        result = main.finding_unique_minterms(minterms, vars)
        result = "F = " + result  # Find the minimized function
        
        caption = customtkinter.CTkLabel(frame_extend, text=result, font=("roboto", 17))
        caption.place(relx=150/WIDTH, rely=180/HEIGHT)
        

        # window.mainloop()  # Start the main event loop

# Create and place the output frame
frame_output = customtkinter.CTkFrame(window)
frame_output.place(relx=10/WIDTH, rely=10/HEIGHT, relwidth=250/WIDTH, relheight=431/HEIGHT)

# Create and place the input frame
frame_input = customtkinter.CTkFrame(window)
frame_input.place(relx=270/WIDTH, rely=10/HEIGHT, relwidth=450/WIDTH, relheight=280/HEIGHT)

# Create and place the extend frame
frame_extend = customtkinter.CTkFrame(window)
frame_extend.place(relx=270/WIDTH, rely=0.667, relwidth=450/WIDTH, relheight=140/HEIGHT)

# Create and place the labels
Label = customtkinter.CTkLabel(frame_input, text="__INPUT__")
Label.place(relx=10/WIDTH, rely=5/HEIGHT)

Label = customtkinter.CTkLabel(frame_output, text="__PROGRESS__")
Label.place(relx=10/WIDTH, rely=5/HEIGHT)

Label = customtkinter.CTkLabel(frame_extend, text="__RESULT__")
Label.place(relx=10/WIDTH, rely=5/HEIGHT)

# Create and place the minterms label and entry
frame_num = customtkinter.CTkLabel(frame_input, text="MINTERMS")
frame_num.place(relx=150/WIDTH, rely=100/HEIGHT)

num_entry = customtkinter.CTkEntry(frame_input, placeholder_text="e.g., 0 1 2 3 ...", width=180, height=32)
num_entry.place(relx=300/WIDTH, rely=100/HEIGHT)

# Create and place the variables label and entry
frame_var = customtkinter.CTkLabel(frame_input, text="VARIABLE")
frame_var.place(relx=150/WIDTH, rely=200/HEIGHT)

var_entry = customtkinter.CTkEntry(frame_input, placeholder_text="e.g., ABCD", width=180, height=32)
var_entry.place(relx=300/WIDTH, rely=200/HEIGHT)

# Create and place the appearance mode combobox
menumode = customtkinter.CTkComboBox(frame_extend, values=["dark", "light", "system"], command=combobox_callback)
menumode.place(relx=630/WIDTH, rely=400/HEIGHT, anchor="center")
menumode.set("system")  # Set the default value to system mode

# Create and place the submit button
button = customtkinter.CTkButton(frame_input, text="Submit", command=submit)
button.place(relx=375/WIDTH, rely=350/HEIGHT, anchor="center")

window.mainloop()  # Start the main event loop


# pyinstaller .\Quine_Mccluskey.py