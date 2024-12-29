from concurrent.futures import ThreadPoolExecutor, as_completed

from utils.get_years_list import get_years_list
from utils.get_papers_list import get_papers_list
from utils.save_papers import download_pdf

subject_codes = ['9709', '9702', '9618', '9608', '9708']

def download_paper(code, year, paper):
    paper_season = paper.split("_")[1]
    print("Downloading paper:", paper)
    result = download_pdf(code, year, paper_season, paper)
    print("Result:", result)
    print()

def process_subject_code(code, start_year=2016, end_year=2024):
    print(f"Getting years for subject code: {code}")
    years = get_years_list(code)
    print(f"Years for subject code {code}: {years}")
    print()
    
    for year in years:
        if int(year) < start_year or int(year) > end_year:
            continue

        print(f"Getting papers for year: {year}")
        papers = get_papers_list(code, year)
        print(f"Papers for year {year}: {papers}")
        print()
        
        # Use ThreadPoolExecutor to download papers concurrently
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(download_paper, code, year, paper): paper for paper in papers}
            
            for future in as_completed(futures):
                paper = futures[future]
                try:
                    future.result()  # Get the result of the future
                except Exception as e:
                    print(f"Error downloading paper {paper}: {e}")
        print()

def main():
    for code in subject_codes:
        process_subject_code(code)
        print()

if __name__ == "__main__":
    main()

# TODO: Migrate to PapaCambridge API for more up-to-date papers
