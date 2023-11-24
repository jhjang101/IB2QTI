<<<<<<< HEAD
# QTI Converter for IB Questionbank DOCX Files

## Introduction

This Python script automates the process of converting DOCX files specifically generated from the [International Baccalaureate (IB) Questionbank](http://ibquestionbank.ibo.org/) to QTI format, facilitating the creation of interactive question sets for IB exams and practice.

## Features
- Converts IB Questionbank DOCX files to GitHub-flavored Markdown (GFM) format using Pandoc.
- Processes GFM files to remove unnecessary lines, fix LaTeX equation tags, convert HTML images to Markdown images, format answers, and add answers if necessary.
- Handles image and equation incorporation in questions and answers.
- Utilizes text2qti to convert the formatted GFM file to a QTI zip file, ready for import into QTI-compatible platforms.

## Prerequisites
1. Downlolad and install Python 3.9+ from here: https://www.python.org/
2. Download and install the latest version of Pandoc from here: https://pandoc.org/
3. Install text2qti using pip:

        $ pip install text2qti

## Usage
1. Save the script `qti.py` and `txt.py` in the same directory as the DOCX file you want to convert.
2. Open a terminal window and navigate to the directory containing the qti.py script.
3. Execute the script using the following command:

        $ python qti.py

4. Follow the on-screen prompts to provide the DOCX filename.
5. The script will convert the IB Questionbank DOCX file and create the corresponding QTI zip file in the same directory.

## Notes

- This script is specifically designed for single answer multiple-choice questions, which is the predominant question type in the IB Questionbank.
- If answer choices in the DOCX file are images or tables, the script will extract the image or table data and include it in the corresponding question.

## Contribution
Contributions to improve the script's functionality or documentation are welcome. Please submit pull requests through GitHub.

## Links
- Pandoc documentation: https://pandoc.org/
- text2qti documentation: https://github.com/gpoore/text2qti
=======
# IB2QTI
 Convert IB questionbank to QTI for canvas
>>>>>>> e4c1dae9954858944c5babc62b25eb0d0e191f27
