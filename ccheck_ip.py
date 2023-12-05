import fitz  # PyMuPDF for PDF processing
import pandas as pd

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        text = ""
        # Iterate over each page in the PDF
        for page in pdf:
            # Extract text from the page
            text += page.get_text()
        return text

def check_ips_in_pdf(pdf_text, ip_list):
    # Check each IP in the list
    ips_found = {ip: ip in pdf_text for ip in ip_list}
    return ips_found

# Path to your CSV and PDF files
csv_path = 'scope_final_network_vapot.csv'
pdf_path = 'PHO_Stockbroking_Network VAPT_NAPT_Report_4Dec23_v1.0.pdf'

# Read the list of IP addresses from the CSV file
ip_df = pd.read_csv(csv_path, header=None)  # Assuming no header in the CSV
ip_list = ip_df[0].tolist()  # Get the first column with IPs

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Check if the IPs are in the PDF
ips_in_pdf = check_ips_in_pdf(pdf_text, ip_list)

# Output the results
for ip, found in ips_in_pdf.items():
    print(f"IP {ip} found in PDF: {found}")
