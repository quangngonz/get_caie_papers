from utils.get_years_list import get_years_list
from utils.get_papers_list import get_papers_list
from utils.save_papers import download_pdf

subject_codes = ['9709', '9702', '9618', '9608', '9708']

for code in subject_codes:
    print(f"Getting years for subject code: {code}")
    years = get_years_list(code)
    print(f"Years for subject code {code}: {years}")
    print()

    for year in years:
        print(f"Getting papers for year: {year}")
        papers = get_papers_list(code, year)
        print(f"Papers for year {year}: {papers}")
        print()


        for paper in papers:
            paper_season = paper.split("_")[1]
            
            print("Downloading paper:", paper)
            result = download_pdf(code, year, paper_season, paper)
            print("Result:", result)
            print()

    print()
