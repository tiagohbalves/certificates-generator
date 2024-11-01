"""Modulo com as definiçoes de tipo de certificado"""

tipos = {
    "participante": """
      Certificamos que <strong><i>{}</i></strong>,{}
       participou do <strong>III Encontro Capixaba
        de Física/SBF (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "poster": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        foi apresentado por <strong><i>{}</i></strong>,{} na forma de
        <strong>Pôster</strong> no <strong>III Encontro Capixaba
        de Física/SBF (III ECF/SBF)</strong>, realizado na Universidade
        Federal do Espírito Santo, campus de São Mateus, no período de 30 de
        outubro de 2024 a 01 de novembro de 2024.""",
    "comunicaco": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        foi apresentado por <strong><i>{}</i></strong>,{} na forma de
        <strong>Comunicação Oral</strong> no
        <strong>III Encontro Capixaba
        de Física/SBF (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "palestrante": """
      Certificamos que <strong><i>{}</i></strong>, participou como
      <strong>Palestrante</strong> no <strong>III Encontro Capixaba
        de Física/SBF (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "organizador": """
      Certificamos que <strong><i>{}</i></strong>,{} participou da
      <strong>Organização</strong> do <strong>III Encontro Capixaba
        de Física/SBF (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mco_pg": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apersentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Comunicação Oral</strong> na seção de
        <strong>Pós-Graduação</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mco_ic": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Comunicação Oral</strong> na seção de
        <strong>Iniciação Científica</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mco_em": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Comunicação Oral</strong> na seção de
        <strong>Ensino Médio</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mh_co": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} recebeu <strong>
        Menção Honrosa</strong> com a <strong>Comunicação Oral</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mh_po": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} recebeu <strong>
        Menção Honrosa</strong> com a <strong>Pôster</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mp_em": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Pôster</strong> na seção de <strong>
        Ensino médio</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mp_ic": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Pôster</strong na seção de <strong>
        Iniciação Científica</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
    "mp_pg": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Pôster</strong na seção de <strong>
        Pós-Graduação</strong>
        apresentado no <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus de São Mateus, no período de 30 de outubro
        de 2024 a 01 de novembro de 2024.""",
}

SOURCE_HTML = """
<html lang="en">
    <head>
        <style>
            @page {
                background-image: url('certificado.png');
                size: a4 landscape;
                @frame header_frame {           /* Static Frame */
                    -pdf-frame-content: header_content;
                    left: 50pt; width: 512pt; top: 50pt; height: 40pt;
                    font-size: 10pt;
                }
                @frame content_frame {          /* Content Frame */
                    left: 100pt; right: 100pt; top: 150pt; height: 632pt;
                }
                @frame footer_frame {           /* Another static Frame */
                    -pdf-frame-content: footer_content;
                    left: 50pt; width: 512pt; top: 772pt; height: 20pt;
                }
            }
            p {
               font-family: Ufes-Sans;
                font-size: 14pt;
                font-weight: 400;
                text-align: justify;
                text-justify: inter-word;
            }
        </style>
        </head>

<body>
    <!-- Content for Static Frame 'header_frame' -->
     <!-- <div id="header_content">Certificados</div> -->

    <!-- Content for Static Frame 'footer_frame' -->
   <!--  <div id="footer_content">(c) - page <pdf:pagenumber>
        of <pdf:pagecount>
    </div>  -->

    <!-- HTML Content -->
    <p >
        %s
    </p>
</body>
</html>
"""

EMAIL_DEF = {
    'email_body': """
    <html>
      <body>
        <p>
          Prezado(a) %s, <br><br>
          Segue em anexo o(s) certificado(s) relacionado a sua participação no
          <strong>III Encontro Capixaba de Física/SBF
        (III ECF/SBF)</strong>
          <br><br>
          Atenciosamente,<br>
          Comitê organizador do III ECF 2024.
        </p>
        <img src="cid:sbf_logo" alt="Logo Sociedade Brasileira de Física"
        style="width:250px;">
      </body>
    </html>
    """,
    'emai_subject': """Certificado III ECF 2024"""
}
