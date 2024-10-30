"""Gera os certificaso e salva em um pdf conforme nome"""
import os
from xhtml2pdf import pisa             # import python module
from modelos import tipos, SOURCE_HTML


def check_and_create_cert_dir():
    """
        Function to check if directory exist and create
    """
    project_path = os.path.dirname(os.path.realpath(__file__))
    certificate_path = os.path.join(project_path, 'certificates')
    if not os.path.exists(certificate_path):
        os.mkdir(certificate_path)
    return certificate_path


def get_text_certificado(data):
    """ Funçao para gerar o texto do certificado """
    tipo_unico = [
        "participante",
        "palestrante",
        "organizador"
        ]
    if data["tipo"] in tipo_unico:
        texto = tipos[data["tipo"]].format(data["nome"])
    else:
        texto = tipos[data["tipo"]].format(data["title"], data["nome"])

    return texto


# Utility function
def save_certificado_pdf(source_html, output_filename):
    """gera o certificado e salva em pdf"""
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
    """ Metodo principal """
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
