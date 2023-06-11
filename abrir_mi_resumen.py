"""
pdfcracker 1.0 (C) 2023
"""

import itertools
import warnings
import os
from tkinter import Tk
from tkinter import filedialog
from pypdf import PdfReader, PdfWriter

warnings.filterwarnings("ignore", category=UserWarning)
"""Supresses the warning for UserWarning: pypdf only implements RC4 encryption so far"""


def intro_message():
    """
    Shows the intro message to the user
    """
    message = """
    --------------------------------------------------------------------
    Bienvenido al programa de recuperación de contraseñas de sus PDFs.
    
    Este software tiene como objetivo descifrar la contraseña de su
    extracto de tarjeta de crédito o bancario en Chile, que normalmente
    está protegido por los primeros 4 o los últimos 4 dígitos de su RUT.

    Por favor, utilice este programa de forma responsable.
    --------------------------------------------------------------------
    """
    print(message)

def select_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Show the file open dialog
    return file_path

def guess_password(pdf_file, digits):
    numbers = '0123456789'
    if os.path.exists(pdf_file):
        pdf = PdfReader(pdf_file)
    else:
        print(f"The file {pdf_file} does not exist.")
        return None

    if pdf.is_encrypted:
        for password_tuple in itertools.product(numbers, repeat=digits):
            password = ''.join(password_tuple)
            try:
                if pdf.decrypt(password):
                    return password
            except:
                continue
    return None

def change_password(pdf_file, old_password, new_password):
    pdf = PdfReader(pdf_file)
    if pdf.decrypt(old_password):
        pdf_writer = PdfWriter()
        for page in pdf.pages:
            pdf_writer.add_page(page)
        pdf_writer.encrypt(new_password)
        with open('unprotected.pdf', 'wb') as f:
            pdf_writer.write(f)

intro_message()

pdf_file = select_file()

if pdf_file is not "":
    try:
        digits = int(input("Ingrese la longitud de la \
                           contraseña (Dale enter para usar '4 números' por defecto): "))
    except ValueError:
        digits = 4

    old_password = guess_password(pdf_file, digits)

    if old_password is not None:
        print("Contraseña encontrada: ", old_password)
        change_password(pdf_file, old_password, '0000')
        print("La contraseña ha sido cambiada a '0000' y el \
              archivo ha sido grabado como 'unprotected.pdf'")
    else:
        print("Contraseña no encontrada")
