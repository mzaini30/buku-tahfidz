const { PDFDocument, rgb } = require("pdf-lib");
const fs = require("fs").promises;

async function mergePDFs() {
  let list_file = [];

  for (let n = 0; n < 3; n++) {
    list_file.push("./list-hapalan-yang-tidak-lancar.pdf");
  }
  for (let n = 0; n < 6; n++) {
    list_file.push("./ziyadah-kiri.pdf");
    list_file.push("./ziyadah-kanan.pdf");
  }
  list_file.push("./aturan-pengisian.pdf");

  // Daftar file PDF yang akan digabungkan
  const pdfFiles = list_file; // Gantilah dengan nama file Anda

  // Buat dokumen PDF kosong
  const mergedPdf = await PDFDocument.create();

  // Iterasi melalui setiap file PDF dan tambahkan ke dokumen yang digabungkan
  for (const pdfFile of pdfFiles) {
    const pdfBytes = await fs.readFile(pdfFile);
    const pdf = await PDFDocument.load(pdfBytes);
    const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
    copiedPages.forEach((page) => mergedPdf.addPage(page));
  }

  // Simpan dokumen yang digabungkan ke file baru
  const mergedPdfBytes = await mergedPdf.save();
  await fs.writeFile("isi-bergabung.pdf", mergedPdfBytes);
}

mergePDFs()
  .then(() => console.log("File PDF telah digabungkan."))
  .catch((error) => console.error("Terjadi kesalahan:", error));
