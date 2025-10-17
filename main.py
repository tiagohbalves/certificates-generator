"""
Main file to generate and send certificates via email.
The data.csv file is read to get the participants data,
certificates are generated in PDF format and sent via email
using Gmail SMTP server. The formats and email content are 
are defined in modelos.py file.
The data.csv file should contain the following columns:
- nome : Name of the participant
- email : Email address of the participant
- tipo : Type of participation (e.g., poster, palestrante, ouvinte, etc.)
    consistent with the keys in modelos.py 'tipos' dictionary
- title : Title of the work (if applicable)
- matricula : Registration number (if applicable)

"""
# Define your data
import pandas as pd
from certificado import generate_certificados
from send_email import send_email


def main_routine():
    """ 
    Main routine to generate and send certificates,
    the certificates are generated based on data from data.csv
    and sent to the respective emails. Multiple certificates
    are sent in a single email if the same email address is found
    for different participants. 
    """
    data_file = 'data.csv' # Path to your data file
    df = pd.read_csv(data_file)
    emails_unique = df["email"].unique()
    for email in emails_unique:
        data = df.loc[df["email"] == email]
        certificados_gerados = generate_certificados(data)
        if isinstance(data["nome"], pd.Series):
            recieve = data["nome"].iloc[0]
        else:
            recieve = data["nome"]
        if isinstance(data["email"],  pd.Series):
            recipient = data["email"].iloc[0]
        else:
            recipient = data["email"]
        send_email(recieve, recipient, certificados_gerados)

# Main program
if __name__ == "__main__":
    main_routine()
