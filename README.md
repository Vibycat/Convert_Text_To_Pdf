
# Convert Text to PDF

## Overview
The **Convert_Text_To_Pdf** project provides a simple and efficient Python-based utility to convert text files (`.txt`) into PDF documents. The script processes all `.txt` files in a specified input directory and outputs the converted `.pdf` files to a designated output directory. 

This project is ideal for anyone who needs to quickly transform text files into professional-looking PDFs.

## Features
- **Batch Conversion**: Converts all `.txt` files in a directory to `.pdf` format.
- **Customizable Paths**: Prompt-based input for flexible file path selection.
- **Error Handling**: Ensures graceful handling of missing or invalid paths.
- **Preserves Input Files**: The original text files are not modified.
- **Automated Directory Management**: Automatically creates the output directory if it doesn't exist.

## Directory Structure
```
Convert_Text_To_Pdf/
├── src/                      # Source code and helper scripts
├── tests/                    # Test scripts and files (if applicable)
├── logs/                     # Logs for debugging (optional)
├── assets/                   # Example input text files and generated PDF files
│   ├── Text/                 # Input text files
│   └── Pdf/                  # Output PDF files
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies for the project
```

## Requirements
- **Python**: Version 3.7 or later
- **fpdf Library**: Install using `pip install fpdf`

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Vibycat/Convert_Text_To_Pdf.git
    cd Convert_Text_To_Pdf
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script**:
    ```bash
    python src/Convert_Text_To_Pdf.py
    ```

4. **Follow the Prompts**:
    - Enter the path to the folder containing `.txt` files.
    - Enter the path to the folder where `.pdf` files should be saved.

## Example Workflow
### Input:
A folder containing the following `.txt` files:
```
example1.txt
example2.txt
```

### Output:
A folder containing the corresponding `.pdf` files:
```
example1.pdf
example2.pdf
```

## Error Handling
- If the input directory doesn't exist, the script notifies the user and exits.
- If a `.txt` file is empty, it is skipped, and a message is displayed.

## Contributions
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

---

Happy Converting! 🚀
