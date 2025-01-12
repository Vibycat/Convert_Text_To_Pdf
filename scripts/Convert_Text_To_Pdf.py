"""
**********************************************
*            Script Information             *
**********************************************
Script Name: Convert_Text_To_Pdf
Author: [Kyle May]
Date: [01-12-2025]
Version: 1.0.0
Description:
    Converts text files from the input directory to PDF using fpdf and outputs the files to the output directory.
**********************************************
"""

# **********************************************
# *                   Imports                  *
# **********************************************
from fpdf import FPDF
import os

# **********************************************
# *           Helper Functions                 *
# **********************************************
def text_to_pdf(input_path, output_path):
    """
    Converts a single text file to a PDF.
    Args:
        input_path (str): Path to the input text file.
        output_path (str): Path to save the output PDF file.
    """
    # Check if the input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return

    # Read the text file
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add lines to the PDF
    for line in lines:
        pdf.cell(0, 10, txt=line.strip(), ln=True)

    # Save the PDF
    try:
        pdf.output(output_path)
        print(f"PDF successfully created at '{output_path}'")
    except Exception as e:
        print(f"Error saving the PDF: {e}")


def convert_directory(input_dir, output_dir):
    """
    Converts all text files in the input directory to PDF files in the output directory.
    The input text files are not modified in any way.
    Args:
        input_dir (str): Path to the directory containing text files.
        output_dir (str): Path to the directory to save the PDF files.
    """
    # Check if the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    # Create the output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Process each text file in the directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".txt"):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name.replace(".txt", ".pdf"))
            
            print(f"Converting '{file_name}' to PDF and saving in '{output_dir}'...")
            text_to_pdf(input_path, output_path)


# **********************************************
# *                Main Logic                  *
# **********************************************
if __name__ == "__main__":
    """
    Main execution block for the script.
    """
    # Prompt user for input and output directories
    input_dir = input("Enter the full path to the input directory containing text files: ").strip()
    output_dir = input("Enter the full path to the output directory for the PDF files: ").strip()

    # Validate user input
    if not input_dir or not output_dir:
        print("Error: Both input and output directory paths are required.")
        exit(1)

    print("Converting all text files in the directory to PDF...")
    convert_directory(input_dir, output_dir)
    print("Conversion complete!")
