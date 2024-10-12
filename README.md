# Resume Optimization Tool

## Overview

This project provides a Python-based tool designed to help users optimize and rewrite their resumes for specific job titles. It enhances the original resume by aligning the content with job-specific requirements and improving the overall presentation for better chances of passing through ATS (Applicant Tracking Systems).

## Features

- **Job-Specific Resume Optimization**: The tool rewrites your resume dynamically based on the job title you are targeting.
- **Markdown to PDF Conversion**: The tool takes a markdown resume and converts it into a PDF format, ready for professional use.
- **ATS Optimization**: The rewritten resume incorporates industry-specific keywords and action-oriented language to improve the chances of clearing ATS.
- **Customization**: Allows users to input a specific job title, making the resume relevant and tailored to the job they are applying for.

## Project Structure

- **`resume_optim.py`**: The main script that handles reading the markdown resume, rewriting it based on the job title, and converting it to PDF format using the `pdfkit` library.
- **`generic_resume.md`**: A sample markdown resume used as a base for rewriting.
- **`rewritten_resume.pdf`**: A sample output generated after running the script, showcasing the rewritten resume in PDF format.

## Dependencies

- Python 3.x
- OpenAI API (or a compatible local model)
- Markdown library for converting markdown to HTML
- pdfkit for converting HTML to PDF
- wkhtmltopdf (required for pdfkit to generate PDFs)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Install `wkhtmltopdf` for PDF generation:
   - On Windows, download from [here](https://wkhtmltopdf.org/downloads.html) and adjust the path to the executable in the script if necessary.

## Usage

1. Run the script and enter the job title when prompted:
   ```bash
   python resume_optim.py
   ```

2. The tool will:
   - Read the `generic_resume.md` file.
   - Rewrite the resume based on the job title provided.
   - Convert the rewritten markdown resume into a PDF file named `rewritten_resume.pdf`.

## Example

If you are targeting a Software Engineering position, the tool will modify the original markdown resume to highlight relevant skills, experiences, and achievements, enhancing the chances of success in applying for that role.

## Customization

- You can modify the prompt in the `resume_optim.py` script to suit specific needs or industries.
- You can replace `generic_resume.md` with your own resume in markdown format for personalized rewriting.
