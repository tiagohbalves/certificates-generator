"""Gera os certificaso e salva em um pdf conforme nome"""
import os
from xhtml2pdf import pisa             # import python module
import pandas as pd
from modelos import tipos, SOURCE_HTML

def check_and_create_cert_dir():
    """
        Function to check if directory exist and create.
        returns the path to the certificate directory.
    """
    project_path = os.path.dirname(os.path.realpath(__file__))
    certificate_path = os.path.join(project_path, 'certificates')
    if not os.path.exists(certificate_path):
        os.mkdir(certificate_path)
    return certificate_path


def get_text_certificado(data):
    """ Funçao para gerar o texto do certificado """
    tipo_unico = [
        "Ouvinte",
        "organizacao",
        "tecnico",
        "palestrante",
        "mesa"
        ]
    matricula_texto = ''
    if not pd.isna(data.matricula):
        matricula_texto = f' matricula <strong><i>{data.matricula}</i></strong>, '

    if data["tipo"] in tipo_unico:
        texto = tipos[data["tipo"]].format(data["nome"], matricula_texto)
    else:
        texto = tipos[data["tipo"]].format(data["title"], data["nome"],
                                           matricula_texto
                                           )

    return texto


# Utility function
def save_certificado_pdf(source_html, output_filename):
    """
    Function to convert HTML to PDF and save it to a file
    given output filename.
    Arguments:
        source_html : HTML to be converted to PDF
        output_filename : Path to save the PDF file
    Returns:
        True on error and False on success
    """
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err


def generate_certificados(datas):
    """
    Routine to generate certificates in PDF format
    for each entry in the datas DataFrame
    Arguments:
        datas : DataFrame with the data to generate certificates
    Returns:
        List of generated certificate file paths
    """
    certificates = []
    certificate_path = check_and_create_cert_dir()
    for _, data in datas.iterrows():
        texto = get_text_certificado(data)
        output_name = data["nome"]+'_'+data["tipo"]+".pdf"
        output_file = os.path.join(certificate_path, output_name)
        status = save_certificado_pdf(SOURCE_HTML % texto, output_file)
        if not status:
            certificates.append(output_file)
    return certificates
