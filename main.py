from pypdf import PdfReader, PdfWriter

# Lista com os nomes dos arquivos PDF a serem unidos
pdfs = ["manual1.pdf", "manual2.pdf"]

# Cria o escritor de PDF
writer = PdfWriter()

# Lê cada PDF e adiciona suas páginas ao escritor
for pdf_file in pdfs:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

# Escreve o resultado em um novo arquivo
with open("manual_robo_educa_volume_1.pdf", "wb") as f_out:
    writer.write(f_out)
