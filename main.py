"""
Arquivo principal com as chamadas das rotinas para gerar e enviar
os certificados
"""
# Define your data
import pandas as pd
from certificado import generate_certificados
from send_email import send_email


# Main program
if __name__ == "__main__":
    DATA_FILE = 'data.csv'
    df = pd.read_csv(DATA_FILE)
    emails_unique = df["email"].unique()
    for email in emails_unique:
        data = df.loc[df["email"] == email]
        certificados_gerados = generate_certificados(data)
        recipient = data["email"]
        recieve = data["nome"][0]
        send_email(recieve, recipient, certificados_gerados)
