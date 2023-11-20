<p align="center">
  <img src="./Images/Job Application Tracker logo.png" />
</p>

### ABOUT
---

Searching for a job can be challenging and it is a 'job' by itself. Sometimes, especially recent graduates, apply for a number of jobs everyday just to start their career. But also, recently professionals who seek for new opportunities tend to be lost after some days of applications without being sure where and when they have applied. 

This program helps everyone track their job applications fast and easily. The only thing the user has to do is to provide the url, the job title and the company's name for every applied position. Then, the program automatically creates or modifies a spreadsheet with all the applications.

The user doesn't have to create anything, the program does it. 

Run the program and make sure you track your process of job applications! Oh, and good luck with it!

### HOW TO USE IT
---
It is advised to create a new directory (for example Job Applications) and save the program there. Then, from that directory you can run the Job Applications Tracker. Download the programs included in the .src directory. To run the program go to the directory where downloaded and run `python3 Job_Application_Tracker.py`.

If you have applied through [InfoJobs](https://www.infojobs.net/), you can download the webpage to the directory `./InfoJobs` using the [Single HTML Downloader](https://www.tnksoft.com/soft/internet/singlehtml/) extension. You just need the text so there is no need to download any images or other decorating elements. Once the job has been registered, the downloaded `.html` file will automatically be deleted. Unfortunately, InfoJobs uses advanced anti-bot techniques that I have not been able to overpass neither with Selenium or other packages. But the process of downloading the website as a `.html` archive is fast and still works fine.

The first thing the program does is to search in the `./InfoJobs` folder for downloaded files and register the data. 

If you apply to different websites you have to import the data manually. 


First, it asks for a url and then for the job title and the company's name. You can leave it running while you apply for different job positions. 

The program stops when an empty url, job title or company's name is given. 

Once you have done with the applications, give an empty url and the program will show you all the last instances created. If you have made a mistake, fear not. Once you have finished, you will be shown your contributions and you can modify any mistaken instance.

After you have checked that everything is as it should, all the records are passed to the spreadsheet, including the Company, the Job Title, the URL and the Day of Application.

### DEPENDENCIES
---
The program is written completely in Python. Different libraries are used but the majority of them are already included in basic Python3. 

- [Pandas](https://pandas.pydata.org/) is used for reading and writing the spreadsheet. Also the registers are passed in a DataFrame. 
- [Numpy](https://numpy.org/) to convert empty string to NaN 
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) for webparsing the InfoJobs website.

##### Pre-installed libraries used
- datetime
- pathlib
- re
- readline
- argparse 
- os
- chardet

### FUTURE LINES
---
My first idea was to include a LLM (specifically, the Llama2 of Meta) to summarise the job description in one or two paragraphs. Version 1.0 will include this feature but it will be optional as Llama2 will have to run on the user's local machine. 

Version 1.1 will also make optional the use of ChatGPT (with the user's credentials) for doing the summary.

Also, other sites (like Linkedin) might be included in automatic insert.
