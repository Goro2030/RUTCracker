"""
pdfcracker 1.0 (C) 2023
"""

import itertools
import warnings
import os
from tkinter import Tk
from tkinter import filedialog
from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError

warnings.filterwarnings("ignore", category=UserWarning)
"""Suppresses the warning for UserWarning: pypdf only implements RC4 encryption so far"""


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
    """Open a file dialog and return the chosen path."""
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Show the file open dialog
    root.destroy()  # Close the Tkinter root window
    return file_path

def guess_password(pdf_file, digits):
    """Brute-force numeric passwords for *pdf_file* of given length."""
    numbers = '0123456789'
    total_combinations = len(numbers) ** digits
    progress = 0

    if os.path.exists(pdf_file):
        pdf = PdfReader(pdf_file)
    else:
        print(f"The file {pdf_file} does not exist.")
        return None

    if not pdf.is_encrypted:
        print("El archivo PDF no está protegido con contraseña.")
        return ""

    for password_tuple in itertools.product(numbers, repeat=digits):
        # Print progress bar
        progress += 1
        bar = '#' * int(progress * 50 / total_combinations)
        percent = progress * 100 / total_combinations
        print(f"\rProgress: [{bar:50s}] {percent:.1f}%", end="", flush=True)

        password = ''.join(password_tuple)
        try:
            if pdf.decrypt(password):
                print()  # Ensure we start on a new line for the next print
                return password
        except PdfReadError:
            continue
    print()  # Ensure we start on a new line for the next print
    return None

def change_password(pdf_file, old_password, new_password):
    """Write *pdf_file* encrypted with *new_password* when *old_password* works."""
    pdf = PdfReader(pdf_file)
    if pdf.decrypt(old_password):
        pdf_writer = PdfWriter()
        for page in pdf.pages:
            pdf_writer.add_page(page)
        pdf_writer.encrypt(new_password)
        with open('unprotected.pdf', 'wb') as output_file:
            pdf_writer.write(output_file)

intro_message()

selected_file = select_file()

if selected_file != "":
    try:
        password_length = int(
            input(
                "Ingrese la longitud de la "
                "contraseña (Dale enter para usar '4 números' por defecto): "
            )
        )
    except ValueError:
        password_length = 4

    found_password = guess_password(selected_file, password_length)

    if found_password == "":
        print("El archivo no estaba protegido. No se modificó el PDF.")
    elif found_password is not None:
        print("Contraseña encontrada: ", found_password)
        change_password(selected_file, found_password, "0000")
        print(
            "La contraseña ha sido cambiada a '0000' y el "
            "archivo ha sido grabado como 'unprotected.pdf'"
        )
    else:
        print("Contraseña no encontrada")
