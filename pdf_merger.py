import os
from pypdf import PdfWriter

folder = r"C:\Users\teboh\OneDrive\Documents"

merger = PdfWriter()

file_names = input("Enter the PDF names separated by commas: ").split(",")

for file in file_names:
    file = file.strip()
    found = False

    for filename in os.listdir(folder):
        name, extension = os.path.splitext(filename)

        if name == file and extension.lower() == ".pdf":
            path = os.path.join(folder, filename)
            merger.append(path)
            found = True
            break

    if not found:
        print(f"{file} was not found as a PDF.")

merger.write(os.path.join(folder, "combined files.pdf"))
merger.close()

print("Merging PDFs complete.")

