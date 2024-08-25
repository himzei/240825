import requests
from bs4 import BeautifulSoup


jobs = []


def job_berlin(term):
    response = requests.get(
        f"https://berlinstartupjobs.com/skill-areas/{term}",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    
    soup = BeautifulSoup(response.text, "html.parser")

    lis = soup.find_all("li", class_="bjs-jlid")
    for item in lis: 
        title = item.find("h4", class_="bjs-jlid__h").text
        company = item.find("a", class_="bjs-jlid__b").text
        description = item.find("div", class_="bjs-jlid__description").text.strip()
        link = item.find("h4").find("a").get("href")

        job_data = {
            "title": title, 
            "company": company, 
            "description": description, 
            "link": link
        }
        jobs.append(job_data)  

    return jobs
    


def job_web3(term):
    response = requests.get(
        f"https://web3.career/{term}-jobs",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    
    soup = BeautifulSoup(response.text, "html.parser")
    lis = soup.find_all("tr", class_="table_row")
    for item in lis: 
        try: 
            title = item.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text
            company = item.find("td", class_="job-location-mobile").text
            link = item.find("div", class_="mb-auto align-middle job-title-mobile").find("a").get("href")
        except: 
            pass
        
        job_data = {
            "title": title.strip(), 
            "company": company.strip(), 
            "link": f"https://web3.career{link.strip()}"
        }

        jobs.append(job_data)

    return jobs


    
        
