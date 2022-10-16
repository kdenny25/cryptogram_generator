import pandas as pd
import xlsxwriter
import tkinter as tk
import os
from tkinter import filedialog
from crypto_gen import encryptPhrase
from file_management import importFile



root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

def createCryptograms(file_path, num_hints):
    # import file to generate cryptograms
    phrases = importFile(file_path)
    crypto_gen = encryptPhrase()
    df_copy = phrases.dataframe
    df_copy["encrypted"] = ""
    print(crypto_gen.encryptedalpha)
    # create columns for each number of specified hints
    for i in range(num_hints):
        df_copy["hint " + str(i)] = ""


    # iterate through list of phrases and encrypt them
    for idx, i in enumerate(phrases.list):
        crypto_gen.setPhrase(i)

        # add encrypted phrase to dataframe
        df_copy.at[idx, "encrypted"] = crypto_gen.getEncryptedPhrase()

        # add hints to dataframe
        for j in range(num_hints):
            df_copy.at[idx, "hint " + str(j)] = crypto_gen.getHint(j)

    return df_copy

final_df = createCryptograms(file_path, 3)

save_path = os.path.splitext(file_path)
save_path = save_path[0] + "test_encrypt.xlsx"
print(save_path)
final_df.to_excel(save_path, engine='xlsxwriter')