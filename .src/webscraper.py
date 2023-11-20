# The Infojobs package used for the scraping of jobs applied through InfoJobs
# Creator: Ioannis Doganos | github:https://github.com/Ioannis-D


#import re
from bs4 import BeautifulSoup
import chardet


class Infojobs():
    def __init__(self, file, directory):
        self.file = directory + file

    def check_html(self):
        if re.search(r"\.html$", self.file):
            with open(self.file, "rb") as f:
                result = chardet.detect(f.read())
            page = open(self.file, "r", encoding=result["encoding"])
            soup = BeautifulSoup(page, features="lxml")
            page.close()
            return soup
        else:
            return 

    def url(self):
        soup = Infojobs.check_html(self)
        if soup:
            url_regex = '\A(https://www.infojobs.net\S*)\\?application?'
            base = soup.find("base")
            if base is not None:
                url = base["href"]
                url = re.findall(url_regex, url)

                if url:
                    return url[0]
            else:
                print(f"\n\nCould not find a url for the {self.file}.\n\
Please make sure you have downloaded the webpage as suggested or insert the information manually.\n\
If you want to re-download the page, leave blank the URL, Job Title and Company Name and delete this file.\n")
                return
        else:
            print(f"\n\n    ####   Attention needed   ####\n\
The script found a file in InfoJobs directory that might not be a webpage.\n\
    The file is: {self.file}\n\n\
If you think that the file is a webpage, please add the '.html' extension at the end of the name or the script will not read it.\n\
Elsewhere, consider deleting or moving it to another location\n\
    ##############################\n")
            return False

    def job_title(self):
        soup = Infojobs.check_html(self)
        if soup:
            job_title = soup.find(id="prefijoPuesto", class_="text-hyphen")
            if job_title is not None:
                job_title = job_title.text.strip()
                if job_title is not None:
                    return job_title
                else:
                    return 
            else:
                return
        else:
            return 

    def company_name(self):
        soup = Infojobs.check_html(self)
        if soup:
            company_name = soup.find("a", class_="link")
            if company_name is not None:
                company_name = company_name.text
                if company_name is not None:
                    return company_name
                else:
                    return
            else:
                return
        else:
            return


