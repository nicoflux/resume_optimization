from openai import OpenAI
import markdown
import pdfkit

def get_job_title():
    job_title = input("Please enter the job title you're targeting: ")
    return job_title

def read_markdown_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def rewrite_resume(job_title, markdown_resume):
    # Define the prompt
    prompt = f"""
    I have a CV written in markdown format for a telecommunications engineering role. 
    I want you to rewrite and enhance my resume, making it more dynamic and adapted to the specific job title of **{job_title}**. 
    Please focus on:

    1. **Highlighting relevant skills**: Tailor the skills to the requirements of the job, making sure to emphasize key areas like [insert key skills from job description]. 
    Make sure to include action-oriented verbs and measurable achievements.

    2. **Experience and projects**: Adjust the language in the work experience and project descriptions to align with industry standards for **{job_title}**. 
    Ensure the descriptions are concise, dynamic, and emphasize problem-solving, innovation, and leadership, particularly in areas like AI, cybersecurity, project management.

    3. **Achievements**: Incorporate any notable accomplishments or quantifiable outcomes (e.g., improving efficiency by X%, reducing costs by X, or leading a project with X number of team members) where applicable. 
    If possible, link my contributions to specific business outcomes or successes that the employer would value.

    4. **Keywords**: Integrate relevant **keywords and jargon** from the **{job_title}** industry to make my resume stand out for ATS (Applicant Tracking System) scanning.

    5. **Soft skills and leadership**: Showcase any leadership, teamwork, and communication skills that match the requirements of the **{job_title}**, particularly in domains like mentoring, managing projects, and collaborating with cross-functional teams.

    Make sure the tone is professional yet dynamic, with a focus on action, results, and growth.

    **Output only the rewritten resume in markdown format** without any other text.

    ---

    {markdown_resume}

    ---
    """

    client = OpenAI(
        base_url = 'http://localhost:11434/v1',
        api_key='ollama', # required, but unused
    )

    response = client.chat.completions.create(
        model="llama3.2:latest",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ], 
        temperature = 0.25 # +++ -> more creative / --- -> more exact(less random)
    )

    return response.choices[0].message.content

# Function to convert markdown to HTML with UTF-8 encoding in the header
def markdown_to_html(markdown_content):
    
    html_body = markdown.markdown(markdown_content)
    
    # Wrap the HTML content in a proper structure with UTF-8 encoding
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CV Nicolas Bloch</title>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    return html_content

def html_to_pdf(html_content, output_pdf_path):
    pdfkit.from_string(html_content, output_pdf_path)

def main():
    job_title = get_job_title()
    markdown_resume = read_markdown_resume('generic_resume.md')
    rewritten_resume = rewrite_resume(job_title, markdown_resume)
    #print("Here is your rewritten resume:\n")
    #print(rewritten_resume)

    html_resume = markdown_to_html(rewritten_resume)
    output_pdf_path = 'rewritten_resume.pdf'
    html_to_pdf(html_resume, output_pdf_path)

    print(f"Your rewritten resume has been saved as a PDF: {output_pdf_path}")

if __name__ == "__main__":
    # Path to the wkhtmltopdf executable
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Adjust this path based on your installation
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    main()

# Convert resume to markdown, better with ChatGPT : resume.md
"""import pdfplumber
from markdownify import markdownify as md

def pdf_to_markdown(pdf_path, md_output_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"
    markdown_text = md(all_text)

    with open(md_output_path, "w") as md_file:
        md_file.write(markdown_text)
    
    print(f"Markdown file created at: {md_output_path}")

pdf_to_markdown("resume.pdf", "resume.md") """