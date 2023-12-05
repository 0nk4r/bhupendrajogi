import fitz  # PyMuPDF for PDF processing
import pandas as pd
import re  # Regular expression library for pattern matching

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as pdf:
        text = ""
        for page in pdf:
            text += page.get_text()
        return text

def extract_ips_from_text(text):
    # Regular expression pattern for matching IP addresses
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    # Find all matches in the text
    return ip_pattern.findall(text)

def check_unlisted_ips_in_pdf(pdf_ips, listed_ips):
    # Convert both lists to sets for faster operations
    pdf_ip_set = set(pdf_ips)
    listed_ip_set = set(listed_ips)
    # Find IPs in PDF that are not in the listed IPs
    unlisted_ips = pdf_ip_set - listed_ip_set
    return unlisted_ips

# Path to your CSV and PDF files
csv_path = 'scope_final_network_vapot.csv'
pdf_path = 'PHO_Stockbroking_Network VAPT_NAPT_Report_4Dec23_v1.0.pdf'

# Read the list of IP addresses from the CSV file
ip_df = pd.read_csv(csv_path, header=None)  # Assuming no header in the CSV
listed_ip_list = ip_df[0].tolist()  # Get the first column with IPs

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Extract all IP addresses from the PDF text
pdf_ips = extract_ips_from_text(pdf_text)

# Check for any IP addresses in the PDF that are not in the CSV list
unlisted_ips_in_pdf = check_unlisted_ips_in_pdf(pdf_ips, listed_ip_list)

# Output the results
if unlisted_ips_in_pdf:
    print("Unlisted IP addresses found in PDF:")
    for ip in unlisted_ips_in_pdf:
        print(ip)
else:
    print("No unlisted IP addresses found in PDF.")
