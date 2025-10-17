## 🇬🇧 `README.en.md`

<div align='center'>
  <a href='README.md'>🇧🇷 Português (BR)</a> • 
  <a href='README.en.md'>🇬🇧 English</a>
</div>

# 🪶 Certificate Generator and Sender

This repository contains a set of **Python** scripts that automate the generation and sending of certificates to event participants.  
The system reads participant data from a **CSV** file, creates personalized **PDF** certificates from **HTML** templates, and sends them by email — grouping multiple certificates for the same recipient in one message.

---

## 🧭 Table of Contents
- [⚙️ Features](#️-features)
- [📁 Project Structure](#-project-structure)
- [🧩 Requirements](#-requirements)
- [🚀 How to Use](#-how-to-use)
- [🎨 Customization](#-customization)
- [📜 License](#-license)

---

## ⚙️ Features

✅ **CSV Reading:** Loads participant data (name, email, participation type, etc.) from a `data.csv` file.  
✅ **PDF Generation:** Creates PDF certificates based on HTML templates and a background image.  
✅ **Certificate Templates:** Supports multiple types of certificates (attendee, speaker, poster, organization, etc.) defined in a dedicated module.  
✅ **Email Sending:** Uses Gmail’s SMTP server to send certificates as attachments.  
✅ **Email Grouping:** Detects multiple certificates for the same email and sends them in a single message.  
✅ **Personalized Email:** Allows customization of the subject and body, supporting embedded images.

---

## 📁 Project Structure

````

.
├── certificates/         # Automatically created directory for generated PDFs
├── main.py               # Main script orchestrating the entire process
├── certificado.py        # Module responsible for generating PDF files
├── send_email.py         # Module responsible for sending emails
├── modelos.py            # Contains all HTML templates for certificates and emails
├── data.csv              # (REQUIRED) Participant data file
├── certificado.png       # (REQUIRED) Certificate background image
├── log-sbf.png           # (REQUIRED) Logo embedded in the email body
└── .env                  # (REQUIRED) File storing email credentials

````

---

## 🧩 Requirements

🟢 **Python 3.8+**

📦 Required libraries:
- `pandas`
- `xhtml2pdf`
- `python-dotenv`

Install them with:

```bash
pip install pandas xhtml2pdf python-dotenv
````

---

## 🚀 How to Use

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Create the `data.csv` File

Example structure:

| Column      | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| `nome`      | Participant’s full name                                                   |
| `email`     | Recipient email address                                                   |
| `tipo`      | Certificate type (must match a key in `tipos` dictionary in `modelos.py`) |
| `title`     | Work title (optional)                                                     |
| `matricula` | Registration or ID number (optional)                                      |

---

### 4️⃣ Configure the `.env` File

```env
EMAIL='your_email@gmail.com'
PASS='your_google_app_password'
```

⚠️ **Important:**
To use Gmail’s SMTP, generate a **16-digit App Password** in your Google Account (your regular password won’t work).

---

### 5️⃣ Add the Required Images

🖼️ `certificado.png` — certificate background image (A4 landscape)
📧 `log-sbf.png` — logo embedded in the email body

---

### 6️⃣ Run the Script

```bash
python main.py
```

The program will:

1. Read `data.csv`
2. Generate PDFs in `certificates/`
3. Send the certificates by email

---

## 🎨 Customization

### ✨ Certificate Types

Edit the `tipos` dictionary in `modelos.py` to change certificate texts.

Supported types:

* `ouvinte` — Attendee
* `tecnico` — Technician
* `poster` — Poster Presentation
* `trabalho` — Paper Presentation
* `comunicacao` — Oral Communication
* `palestrante` — Speaker
* `mesa` — Round Table
* `organizacao` — Organization
* `mco_pg` — Best Oral Presentation (Graduate)
* `mco_ic` — Best Oral Presentation (Undergraduate)
* `mco_em` — Best Oral Presentation (High School)
* `mh_co` — Honorable Mention - Oral Communication
* `mh_po` — Honorable Mention - Poster
* `mp_em` — Best Poster - High School
* `mp_ic` — Best Poster - Undergraduate
* `mp_pg` — Best Poster - Graduate

---

### 🧾 PDF and Email Layout

* 🪄 **PDF Layout:** Edit the `SOURCE_HTML` variable in `modelos.py`
* 💌 **Email Content:** Edit the `EMAIL_DEF` dictionary in `modelos.py`

---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.
