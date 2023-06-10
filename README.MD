# RUTCracker

- Instructions in [English](#rutcracker)
- Instrucciones en [Español Chilensis](#rutcracker-1)

***RUTCracker is a Python script intended to recover lost or forgotten passwords of PDF files that are often set as the first four, five or last four digits of a RUT number in Chile, sometimes including the verification digit, and sometimes not.***

## Description & Motivation

In the digital age, managing multiple passwords can be challenging. More so when institutions such as banks use different methods to set these passwords. Some banks in Chile use the first four or five digits of your RUT as a password, sometimes including the verification digit and sometimes not, causing even more confusion and making it harder to remember.

Forgetting the password to a critical document can cause stress and delays, especially when it comes to handling important personal or financial data. As a Chilean citizen who has encountered this issue more than once, I was motivated to develop RUTCracker. 

The goal of this project is to alleviate the difficulties associated with these various password conventions and make the process of password recovery more accessible and user-friendly. It can be particularly helpful in scenarios where the lost password is protecting vital financial documents, such as credit card or bank statements.

**Please note that this script should only be used for ethical purposes, such as recovering the password of a file that you own or have permission to access. Unauthorized use of this software to access or decrypt files that do not belong to you is strictly prohibited and unethical.**

## Installation

1. Clone this repository.
2. Install the necessary dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script with Python 3:

   ```
   python3 abrir_mi_resumen.py
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

If after installing the requirements, the program won't run with an error --> modulenotfounderror: no module named 'tkinter'

The error “No matching distribution found for tkinter” usually occurs when you are trying to install tkinter using pip on a system where tkinter is not installed or is not supported.

To resolve this issue, you can try installing tkinter using your system’s package manager. For example, on Ubuntu, you can run the following command:

```
sudo apt-get install python3-tk
```
If you are using a different operating system, you can try searching for instructions on how to install tkinter on your system.

I hope this helps!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



# RUTCracker

***RUTCracker es un script de Python que se las ingenia para desencriptar esas contraseñas perdidas u olvidadas de archivos PDF, las típicas que son los primeros cuatro, cinco o los últimos cuatro dígitos de tu RUT, a veces con el dígito verificador, a veces sin él.***

## Descripción y Motivación

En esta era digital, tener que recordar mil contraseñas es una lata tremenda. Y más todavía cuando los bancos se les ocurren las ideas más raras para estas contraseñas. Algunos bancos o tarjetas de crédito en Chile ocupan los primeros cuatro o cinco dígitos de tu RUT como contraseña, a veces con el dígito verificador, a veces sin él. Un verdadero cacho que te complica la vida y hace más difícil acordarse.

Y cuando se te olvida la contraseña de una wea importante, la angustia es tremenda, especialmente cuando se trata de tus documentos personales o financieros, como los estados de cuenta de tarjetas de crédito o bancos.

Como chileno que ha tenido que lidiar con este rollo más de una vez, me motivé a desarrollar RUTCracker, para alivianar estos problemas y hacer el proceso de recuperación de contraseña más amigable para el usuario. Esta wea te puede servir caleta cuando se te olvida la contraseña que está protegiendo documentos importantes como tus estados de cuenta.

**Ojo, que este script debe usarse solo para fines pulentos, como recuperar la contraseña de un archivo que te pertenece o al que tienes permiso para acceder. Si ocupas esta wea para acceder a archivos ajenos, estás en problemas, ya que está estrictamente prohibido y es super flaite.**

## Instalación

1. Hazle un clone a este repositorio.
2. Instala las dependencias necesarias usando pip, como un mago:

   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el script con Python 3, como todo un pro:

   ```
   python3 abrir_mi_resumen.py
   ```

2. Cuando se te solicite, selecciona la wea para la cual necesitas adivinar la contraseña.
3. Luego, ingresa la cantidad de caracteres de la contraseña. Por defecto, son 4.
4. La wea de script intentará adivinar la contraseña. Si tiene éxito, te mostrará la contraseña y guardará una copia del PDF con la contraseña cambiada a '0000', la bautizamos como 'unprotected.pdf'.

## Dependencias

Esta wea usa las siguientes bibliotecas de Python:

- tkinter (biblioteca estándar)
- itertools (biblioteca estándar)
- PyPDF2

Instala las bibliotecas necesarias con pip, así no más:

```
pip install -r requirements.txt
```

## Licencia

Esta wea está bajo la Licencia MIT - échale un vistazo al archivo [LICENSE](LICENSE) para más detalles.

(C) Goro2030 - 10/Jun/2023