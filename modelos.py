"""Modulo com as definiçoes de tipo de certificado"""

tipos = {
    "Ouvinte": """
      Certificamos que <strong><i>{}</i></strong>,{}
       participou do <strong>IV Encontro Capixaba
        de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08 a
        10 de outubro de 2025.""",
    "tecnico": """
      Certificamos que <strong><i>{}</i></strong>,{}
       atuou como técnico de som e transmisao do <strong>IV Encontro Capixaba
        de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
    "poster": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        foi apresentado por <strong><i>{}</i></strong>, na forma de
        <strong>Pôster</strong> no <strong>IV Encontro Capixaba
        de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade
        Federal do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08 a
        10 de outubro de 2025.""",
    "trabalho": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        foi apresentado por <strong><i>{}</i></strong> no <strong>IV Encontro Capixaba
        de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade
        Federal do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08 a
        10 de outubro de 2025.""",
    "comunicacao": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        foi apresentado por <strong><i>{}</i></strong>, na forma de
        <strong>Comunicação Oral</strong> no
        <strong>IV Encontro Capixaba
        de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
    "palestrante": """
      Certificamos que <strong><i>{}</i></strong>, participou como
      <strong>Palestrante</strong> no <strong>IV Encontro Capixaba
        de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08
        a 10 de outubro de 2025.""",
    "mesa": """
      Certificamos que <strong><i>{}</i></strong>, participou da Mesa redonda:
      <strong>"Mecânica Quântica, sua construção e seus desafios"</strong>
      no <strong>IV Encontro Capixaba
      de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade Federal
      do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08
      a 10 de outubro de 2025.""",
    "organizacao": """
      Certificamos que <strong><i>{}</i></strong>,{} participou da
      <strong>Organização</strong> do <strong>IV Encontro Capixaba
        de Física/SBF (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de 08
        a 10 de outubro de 2025.""",
    "mco_pg": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apersentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Comunicação Oral</strong> na seção de
        <strong>Pós-Graduação</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período
        de 08 de outubro de 2025 a 10 de outubro de 2025.""",
    "mco_ic": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Comunicação Oral</strong> na seção de
        <strong>Iniciação Científica</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período
        de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
    "mco_em": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Comunicação Oral</strong> na seção de
        <strong>Ensino Médio</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período de
        08 de outubro de 2025 a 10 de outubro de 2025.""",
    "mh_co": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} recebeu <strong>
        Menção Honrosa</strong> com a <strong>Comunicação Oral</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período
        de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
    "mh_po": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} recebeu <strong>
        Menção Honrosa</strong> com a <strong>Pôster</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período
        de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
    "mp_em": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Pôster</strong> na seção de <strong>
        Ensino médio</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período
        de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
    "mp_ic": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Pôster</strong na seção de <strong>
        Iniciação Científica</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período
        de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
    "mp_pg": """
      Certificamos que o trabalho de título <strong><i>{}</i></strong>,
        apresentado por <strong><i>{}</i></strong>,{} foi avaliado
        como melhor <strong>Pôster</strong na seção de <strong>
        Pós-Graduação</strong>
        apresentado no <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>, realizado na Universidade Federal
        do Espírito Santo, campus Goiabeiras, Vitória - ES, no período
        de 08 de outubro
        de 2025 a 10 de outubro de 2025.""",
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
                    left: 100pt; right: 100pt; top: 260pt; height: 632pt;
                }
                @frame footer_frame {           /* Another static Frame */
                    -pdf-frame-content: footer_content;
                    left: 50pt; width: 512pt; top: 772pt; height: 20pt;
                }
            }
            p {
               font-family: Ufes-Sans;
                font-size: 16pt;
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
          O certificado de pôster enviado anteriormente continha um erro.
          Favor desconsiderar o certificado anterior.
          Segue em anexo o(s) certificado(s) corrigido, relacionado a sua participação no
          <strong>IV Encontro Capixaba de Física/SBF
        (IV ECF/SBF)</strong>
          <br><br>
          Atenciosamente,<br>
          Comitê organizador do IV ECF/SBF 2025.
        </p>
        <img src="cid:sbf_logo" alt="Logo Sociedade Brasileira de Física"
        style="width:250px;">
      </body>
    </html>
    """,
    'emai_subject': """ERRATA: Certificado Pôster IV ECF/SBF 2025""",
}
