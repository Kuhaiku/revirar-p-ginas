from PyPDF2 import PdfReader, PdfWriter

def inverter_pdf(input_pdf, output_pdf):
    # Ler o arquivo PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    total_paginas = len(reader.pages)
    
    # Se o número de páginas for ímpar, adicionar uma página em branco no final
    if total_paginas % 2 != 0:
        writer.add_page(reader.pages[-1])  # Adiciona a última página ao final

    # Percorre as páginas duas a duas (1 com 2, 3 com 4...)
    for i in range(0, total_paginas - 1, 2):
        writer.add_page(reader.pages[i + 1])  # Adiciona a página par
        writer.add_page(reader.pages[i])      # Adiciona a página ímpar

    # Salva o novo PDF com as páginas invertidas
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"PDF invertido salvo como: {output_pdf}")

# Exemplo de uso
input_pdf = "teste.pdf"
output_pdf = "arquivo_invertido.pdf"
inverter_pdf(input_pdf, output_pdf)
