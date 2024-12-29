from bs4 import BeautifulSoup
import requests

GCEGUIDE_URL_SUBJECT = "https://papers.gceguide.cc/a-levels/{}"

code_to_url = {
    "9709": "mathematics-(9709)",
    "9702": "physics-(9702)",
    "9618": "computer-science-(9618)",
    "9608": "computer-science-(9608)",
    "9708": "economics-(9708)"
}

skip_contents = ['Other Resources', 'Specimen Papers']

def get_years_list(subject_code):
    url = GCEGUIDE_URL_SUBJECT.format(code_to_url[subject_code])
    print("Target URL: ", url)

    print("Sending request...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        print("Response received.")

        print("Parsing HTML...")
        soup = BeautifulSoup(page.content, 'html.parser')
        years = soup.find_all('ul', class_='paperslist')

        result = []
        if years:
            print("Years found:")
            for year in years:
                list_items = year.find_all('li')
                for item in list_items:
                    anchor = item.find('a')
                    if anchor.text.strip() not in skip_contents:
                        result.append(anchor.text.strip())

            # print("Extracted results:", result)
            return result
        else:
            print("No years found with the specified class.")
            raise Exception("No years found.")
    else:
        print(f"Failed to fetch the page. Status code: {page.status_code}")
        raise Exception("Failed to fetch the page.")