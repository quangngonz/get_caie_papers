import os
import requests
from urllib.parse import urlparse

GCEGUIDE_URL_PAPER = "https://papers.gceguide.cc/a-levels/{}/{}/{}"

code_to_url = {
    "9709": "mathematics-(9709)",
    "9702": "physics-(9702)",
    "9618": "computer-science-(9618)",
    "9608": "computer-science-(9608)",
    "9708": "economics-(9708)"
}

def download_pdf(subject_code, year, season, paper):
    """
    Downloads a PDF file from a given URL and saves it to /download/{subject_code}/{year}.

    Args:
        subject_code (str): The subject code.
        year (int): The year of the paper.
        season (str): The season of the paper (e.g., "summer" or "winter").
        paper (str): The name of the paper.

    Returns:
        str: The file path where the PDF is saved, or an error message if download fails.
    """
    # Parse the URL to extract the file name
    file_name = paper
    pdf_url = GCEGUIDE_URL_PAPER.format(code_to_url[subject_code], year, paper)
    print("Target URL: ", pdf_url)

    # Ensure the file has a .pdf extension
    if not file_name.endswith(".pdf"):
        return "Error: The URL does not point to a .pdf file."

    # Create the directory structure /download/{subject_code}/{year}
    save_dir = os.path.join("papers", subject_code, str(year), season)
    os.makedirs(save_dir, exist_ok=True)

    # Define the full file path
    file_path = os.path.join(save_dir, file_name)

    try:
        # Download the PDF file
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Save the file
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return f"File saved to {file_path}"
    except requests.exceptions.RequestException as e:
        return f"Error downloading file: {e}"
