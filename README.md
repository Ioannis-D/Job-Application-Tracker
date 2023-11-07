<p align="center">
  <img src="./Job Application Tracker logo.png" />
</p>

### ABOUT
---

Searching for a job can be challenging and it is a 'job' by itself. Sometimes, especially recently graduates, apply for a number of jobs everyday just to start their career. But also, recently unemployed or even senior professionals that search for a new opportunity tend to be lost after some days of applications without being sure where and when they have applied. 

This program helps everyone track their job applications fast and easily. The only thing the user has to do is to provide the url, the job title and the company's name for every applied position. Then, the program automatically creates or modifies a spreadsheet application.

The user doesn't have to create anything, the program does it. 

Run the program and make sure you track your process of job applications! Oh, and good luck with it!.

### HOW TO USE IT
---
It is advised to create a new directory (for example Job Applications) and save the program there. Then, from that directory you can run the Job Applications Tracker. 

First, it asks for a url* and then for the job title and the company's name. You can leave it running while you apply for different job positions. 

The program stops when an empty url, job title or company's name is given. 

Once you have done with the applications, give an empty url and the program will show you all the last instances created. If you have made a mistake, fear not. Once you have finished, you will be shown your contributions and you can modify any mistaken instance.

After you have checked that everything is as it should, all the records are passed to the spreadsheet, including the Company, the Job Title, the URL and the Day of Application.


(*apart from being able to review the job description, the url is asked for the future versions of the program with which some job applications will be automatically filled. See the [Future Lines](#future-lines) section for more details)

### DEPENDENCIES
---
The program is written completely in Python. Different libraries are used but the majority of them are already included in basic Python3. 

- [Pandas](https://pandas.pydata.org/) is used for reading and writing the spreadsheet. Also the registers are passed in a DataFrame. 

##### Pre-installed libraries used
- datetime
- pathlib
- re
- readline
- argparse 

### FUTURE LINES
---
This version (0.1) is not the final version of the program. The program is to been designed to automate even more the process. 

The next version (0.2) will automatically insert the Job Title and the Company's name if the url given will be either from Linkedin or InfoJobs (a commonly used job-searching website in Spain).

Even then, the program will not be complete. My first idea was to include a LLM (specifically, the Llama2 of Meta) to summarise the job description in one or two paragraphs. Version 1.0 will include this feature but it will be optional as Llama2 will have to run on the user's local machine. 

Version 1.1 will also make optional the use of ChatGPT (with the user's credentials) for doing the summary.
