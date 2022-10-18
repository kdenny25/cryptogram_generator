import pandas as pd
import xlsxwriter
import tkinter as tk
import customtkinter as ctk
import os
from tkinter import filedialog
from backend.core.encrypt_phrase import encryptPhrase
from backend.core.file_management import importFile

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window

# window setup
app.geometry('600x340')
app.title('Cryptogram Generator')

# create 3x3 grid system
app.grid_rowconfigure((2,0), weight=1)
app.grid_columnconfigure((0,2), weight=1)

def load_file(file_path, textbox):
    file_path = filedialog.askopenfilename()
    textbox.insert('0.0',"File Path: " + file_path)
    return file_path

def generate_cryptograms(file_path):
    if file_path != '':
        final_df = createCryptograms(file_path, 3)
        save_path = os.path.splitext(file_path)
        save_path = save_path[0] + "test_encrypt.xlsx"
        print(save_path)
        final_df.to_excel(save_path, engine='xlsxwriter')

def createCryptograms(file_path, num_hints):
    """ returns dataframe of original file with encrypted phrases
        and hints. """
    # import file to generate cryptograms
    phrases = importFile(file_path)
    crypto_gen = encryptPhrase()
    df_copy = phrases.dataframe
    df_copy["encrypted"] = ""
    # print(crypto_gen.encryptedalpha)
    # # create columns for each number of specified hints
    # for i in range(num_hints):
    #     df_copy["hint " + str(i)] = ""


    # iterate through list of phrases and encrypt them
    for idx, i in enumerate(phrases.list):
        crypto_gen.setPhrase(i)

        # add encrypted phrase to dataframe
        df_copy.at[idx, "encrypted"] = crypto_gen.getEncryptedPhrase()

        # add hints to dataframe
        for j in range(num_hints):
            df_copy.at[idx, "hint " + str(j)] = crypto_gen.getHint(j)

    return df_copy

file_path = ''

results_text_box = ctk.CTkTextbox()
results_text_box.grid(row=0, column=0, columnspan=3, padx=20, pady=(20,0), sticky='nsew')
results_text_box.insert('0.0','Select File.')

# Button to open file dialogue and select the file to use.
button_load_file = ctk.CTkButton(master=app, text='Load File', command=lambda: load_file(file_path, results_text_box))
button_load_file.grid(row=1, column=0, padx=20, pady= (20,0), sticky='ew')

# Button to run the program and generate encrypted phrases.
button_create_cryptograms = ctk.CTkButton(master=app, text='Generate Cryptograms',
                                          command=lambda: generate_cryptograms(file_path))
button_create_cryptograms.grid(row=1, column=2, padx=20, pady=(20,0), sticky='ew')

label_error = ctk.CTkLabel(master=app, text='Error Messages Here')
label_error.grid(row=2, column=0, columnspan=3, padx=20, sticky='w')

app.mainloop()