import PyPDF2
import argparse
import sys


# Get metadata from PDF file
def get_metadata(file_name):
	pdf_file = PyPDF2.PdfFileReader(open(file_name, "rb"))
	doc_info = pdf_file.getDocumentInfo()
	print(f"[*] PDF Metadata for: {file_name}")
	
	for info in doc_info:
		print(f"[+] {info.strip('/')}: {doc_info[info]}")


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", dest="file", help="Specify the PDF file you want to analyse.")

	if len(sys.argv) != 3:
		parser.print_help(sys.stderr)
		sys.exit(1)

	args = parser.parse_args()
	file_name = args.file

	try:	
		get_metadata(file_name)

	except:
		print(f"[-] File Not Found!")
		sys.exit(1)



if __name__ == "__main__":
	main()