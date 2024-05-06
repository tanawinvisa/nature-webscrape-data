import requests
from bs4 import BeautifulSoup

search_input = input("Enter your search query: ")
search_input = search_input.replace(" ", "+")
print("Modified search query:", search_input)
needyear = input("Needyear: ")
if needyear :
    startyear = input("start year search query: ")
    endyear = input("end year search query: ")





def getScholarData():
    try:
        # Base URL
        base_url = "https://www.google.com/scholar?q="

        # Concatenating the base URL, modified search query, and hl parameter
        if needyear:
            url = base_url + search_input + "&hl=en" + "&as_ylo=2012&as_yhi=2015"
        else:
            url = base_url + search_input + "&hl=en"

        print("Modified URL:", url)

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)

        scholar_results = []

        for el in soup.select(".gs_ri"):
            result = {}
            result["Title"] = el.select(".gs_rt")[0].text.strip()
            result["Title Link"] = el.select(".gs_rt a")[0]["href"]
            result["ID"] = el.select(".gs_rt a")[0]["id"]
            result["Displayed Link"] = el.select(".gs_a")[0].text.strip()
            result["Snippet"] = el.select(".gs_rs")[0].text.replace("\n", "").strip()
            result["Cited By Count"] = el.select(".gs_nph+ a")[0].text.strip()
            result["Cited Link"] = "https://scholar.google.com" + el.select(".gs_nph+ a")[0]["href"]
            versions_count = el.select("a~ a+ .gs_nph")[0].text.strip()
            result["Versions Count"] = versions_count if versions_count else "N/A"
            result["Versions Link"] = "https://scholar.google.com" + el.select("a~ a+ .gs_nph")[0]["href"] if versions_count else "N/A"
            scholar_results.append(result)

        print("Scholar Results:")
        for result in scholar_results:
            print("-" * 50)
            for key, value in result.items():
                print(f"{key}: {value}")
        
    except Exception as e:
        print("An error occurred:", e)


def getData():
    try:
        id_value = input("Enter the ID value: ")

        # Base URL
        base_url = "https://scholar.google.com/scholar?q=info:"

        # Constructing the complete URL by concatenating the base URL, ID value, and output parameter
        url = base_url + id_value + ":scholar.google.com&output=cite"

        print("Modified URL:", url)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        cite_results = []
        for el in soup.select("#gs_citt tr"):
            cite_results.append({
                "title": el.select_one(".gs_cith").text.strip(),
                "snippet": el.select_one(".gs_citr").text.strip()
            })
        links = []
        for el in soup.select("#gs_citi .gs_citi"):
            links.append({
                "name": el.text.strip(),
                "link": el.get("href")
            })
        print(cite_results)
        print(links)
    except Exception as e:
        print(e)

getScholarData()
print("-" * 50)
print("Cite Result")
getData()
