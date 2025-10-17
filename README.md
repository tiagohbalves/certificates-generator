## 🇧🇷 `README.md`

<div align='center'>
  <a href='README.md'>🇧🇷 Português (BR)</a> • 
  <a href='README.en.md'>🇬🇧 English</a>
</div>

# 🪶 Gerador e Enviador de Certificados

Este repositório contém um conjunto de scripts em **Python** que automatizam a geração e o envio de certificados para participantes de eventos.  
O sistema lê dados de um arquivo **CSV**, cria certificados personalizados em **PDF** a partir de modelos **HTML**, e os envia por e-mail — agrupando múltiplos certificados do mesmo destinatário em uma única mensagem.

---

## 🧭 Sumário
- [⚙️ Funcionalidades](#️-funcionalidades)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🧩 Requisitos](#-requisitos)
- [🚀 Como Usar](#-como-usar)
- [🎨 Personalização](#-personalização)
- [📜 Licença](#-licença)

---

## ⚙️ Funcionalidades

✅ **Leitura de CSV:** Carrega informações de participantes (nome, e-mail, tipo de participação etc.) a partir do arquivo `data.csv`.  
✅ **Geração de PDFs:** Cria certificados em PDF baseados em modelos HTML e uma imagem de fundo.  
✅ **Modelos de Certificado:** Suporte a múltiplos tipos de certificado (ouvinte, palestrante, pôster, organização etc.), definidos em módulo próprio.  
✅ **Envio de E-mails:** Utiliza o servidor SMTP do Gmail para envio dos certificados.  
✅ **Agrupamento de E-mails:** Detecta múltiplos certificados do mesmo e-mail e envia tudo em uma única mensagem.  
✅ **E-mail Personalizado:** Permite personalizar assunto e corpo do e-mail, com suporte a imagens embutidas.

---

## 📁 Estrutura do Projeto

```

.
├── certificates/         # Diretório criado automaticamente para PDFs gerados
├── main.py               # Script principal que orquestra todo o processo
├── certificado.py        # Módulo responsável por gerar os arquivos PDF
├── send_email.py         # Módulo responsável por enviar os e-mails
├── modelos.py            # Contém os modelos HTML dos certificados e e-mails
├── data.csv              # (OBRIGATÓRIO) Arquivo com dados dos participantes
├── certificado.png       # (OBRIGATÓRIO) Imagem de fundo do certificado
├── log-sbf.png           # (OBRIGATÓRIO) Logo usado no corpo do e-mail
└── .env                  # (OBRIGATÓRIO) Arquivo com as credenciais de e-mail

````

---

## 🧩 Requisitos

🟢 **Python 3.8+**

📦 Bibliotecas necessárias:
- `pandas`
- `xhtml2pdf`
- `python-dotenv`

Instale tudo com:

```bash
pip install pandas xhtml2pdf python-dotenv
````

---

## 🚀 Como Usar

### 1️⃣ Clone o Repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```

### 2️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Crie o Arquivo `data.csv`

Crie o arquivo `data.csv` na raiz do projeto com os dados dos participantes:

| Coluna      | Descrição                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------- |
| `nome`      | Nome completo do participante                                                             |
| `email`     | E-mail do destinatário                                                                    |
| `tipo`      | Tipo de certificado (deve corresponder a uma chave no dicionário `tipos` do `modelos.py`) |
| `title`     | Título do trabalho apresentado (opcional)                                                 |
| `matricula` | Número de matrícula ou ID (opcional)                                                      |

---

### 4️⃣ Configure o `.env`

Crie um arquivo `.env` na raiz do projeto com suas credenciais de e-mail:

```env
EMAIL='seu_email@gmail.com'
PASS='sua_senha_de_aplicativo'
```

⚠️ **Atenção:**
Para usar o SMTP do Gmail, é necessário gerar uma **senha de app** de 16 dígitos nas configurações da sua conta Google.

---

### 5️⃣ Adicione as Imagens

🖼️ `certificado.png` — imagem de fundo (A4 horizontal)
📧 `log-sbf.png` — logo usada no corpo do e-mail

---

### 6️⃣ Execute o Script

```bash
python main.py
```

O sistema irá:

1. Ler o `data.csv`
2. Gerar os PDFs em `certificates/`
3. Enviar os certificados por e-mail

---

## 🎨 Personalização

### ✨ Tipos de Certificados

Para adicionar, remover ou modificar textos dos certificados, edite o dicionário `tipos` no arquivo `modelos.py`.

Tipos atualmente suportados:

* `ouvinte`
* `tecnico`
* `poster`
* `trabalho`
* `comunicacao`
* `palestrante`
* `mesa`
* `organizacao`
* `mco_pg`
* `mco_ic`
* `mco_em`
* `mh_co`
* `mh_po`
* `mp_em`
* `mp_ic`
* `mp_pg`

---

### 🧾 Layout de PDF e E-mail

* 🪄 **Layout do PDF:** altere o conteúdo da variável `SOURCE_HTML` em `modelos.py`.
* 💌 **Conteúdo do E-mail:** modifique o dicionário `EMAIL_DEF` em `modelos.py`.

---

## 📜 Licença

Este projeto é licenciado sob a **MIT License**.
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
