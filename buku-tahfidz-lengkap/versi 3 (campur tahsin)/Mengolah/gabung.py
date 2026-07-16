import pypdf

def merge_pdfs():
    writer = pypdf.PdfWriter()
    
    # 6. Tahsin x 11
    print("Adding 6. Tahsin.pdf (11 times)")
    for _ in range(11):
        writer.append("6. Tahsin.pdf")
        
    # loop (8 kali) { 5. Ujian Kiri.pdf, 4. Ujian Kanan.pdf }
    print("Adding 5. Ujian Kiri.pdf & 4. Ujian Kanan.pdf loop (8 times)")
    for i in range(8):
        writer.append("5. Ujian Kiri.pdf")
        writer.append("4. Ujian Kanan.pdf")
        
    # loop (12 kali) { 3. Ziyadah Kiri.pdf, 2. Ziyadah Kanan.pdf }
    print("Adding 3. Ziyadah Kiri.pdf & 2. Ziyadah Kanan.pdf loop (12 times)")
    for i in range(12):
        writer.append("3. Ziyadah Kiri.pdf")
        writer.append("2. Ziyadah Kanan.pdf")
        
    # 1. Aturan Pengisian.pdf
    print("Adding 1. Aturan Pengisian.pdf")
    writer.append("1. Aturan Pengisian.pdf")
    
    output_filename = "isi-bergabung.pdf"
    with open(output_filename, "wb") as f:
        writer.write(f)
    writer.close()
    
    # Verify the page count of the generated file
    reader = pypdf.PdfReader(output_filename)
    num_pages = len(reader.pages)
    print(f"Successfully merged into {output_filename} with {num_pages} pages.")

if __name__ == "__main__":
    merge_pdfs()
