# PDF Password Cracker

This is a simple Python script intended to guess the password of a PDF file.

## Description

This script is intended for educational purposes or password recovery for personal use. The software is designed to guess the password of a PDF document, which is often the first four or last four digits of your RUT number in Chile.

**Please use this script responsibly and ethically.**

## Installation

1. Clone this repository.
2. Install the necessary dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script with Python 3:

   ```
   python3 pdf_password_cracker.py
   ```

2. When prompted, select the file for which you would like to guess the password.
3. Next, enter the number of characters in the password. By default, this is 4.
4. The script will attempt to guess the password. If successful, it will display the password and save a copy of the PDF with the password changed to '0000', named 'unprotected.pdf'.

## Dependencies

This script uses the following Python libraries:

- tkinter (standard library)
- itertools (standard library)
- PyPDF2

You can install the necessary libraries with pip:

```
pip install -r requirements.txt
```


# Desencriptador de Contraseñas de PDF

Este es un simple script en Python diseñado para adivinar la contraseña de un archivo PDF.

## Descripción

Este script se ha creado para fines educativos o para la recuperación de contraseñas de uso personal. El software está diseñado para adivinar la contraseña de un documento PDF, que a menudo son los primeros cuatro o últimos cuatro dígitos de tu número de RUT en Chile.

**Por favor, usa este script de manera responsable y ética.**

## Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias usando pip:

   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el script con Python 3:

   ```
   python3 desencriptador_contraseñas_pdf.py
   ```

2. Cuando se te solicite, selecciona el archivo para el cual te gustaría adivinar la contraseña.
3. A continuación, introduce el número de caracteres de la contraseña. Por defecto, son 4.
4. El script intentará adivinar la contraseña. Si tiene éxito, mostrará la contraseña y guardará una copia del PDF con la contraseña cambiada a '0000', con el nombre 'unprotected.pdf'.

## Dependencias

Este script usa las siguientes bibliotecas de Python:

- tkinter (biblioteca estándar)
- itertools (biblioteca estándar)
- PyPDF2

Puedes instalar las bibliotecas necesarias con pip:

```
pip install -r requirements.txt
```