#!/usr/bin/env python3

########################################################################
#                       Job Aplication Tracker                         #
#             Easily track the job applications you have done.         #
#                         Written in Python.                           #
#                                                                      #
#                           Version 0.2                                #
#----------------------------------------------------------------------#
#                   Licence: Apache License 2.0                        #
#                                                                      #
#   Creator: Ioannis Doganos, github: https://github.com/Ioannis-D     #
########################################################################

# ------------ LIBRARIES USED ------------
from datetime import date # For the current day
from pathlib import Path # To check if the spreadsheet exists
import pandas as pd # To manipulate the data and the spreadsheet
import re # For the use of regex
import readline # To pre-print the Job and Company already given if the user wants to modify them
import argparse # For the help message
import os # For parsing the directory files
from os.path import isfile, join # For checking if the object is a file 
import numpy as np # Convert empty string to NaN

from webscraper import Infojobs # Library made to scrap the webpages

# ------------ HELP MESSAGE ------------
help_message = """
This is a program written in Python for letting you store your job applications nicely and tidy into a spreadsheet (.xlsx). 
If you have applied via InfoJobs (https://www.infojobs.net), check the README to see how to automatically register these jobs.

It is easy and fast to use:
    Firstly, the program will scan posible job applications through InfoJobs (https://www.infojobs.net). If something goes wrong, it will indicate to insert the job manually.
    After that, the program will ask you to insert the url of a job position you have applied (and not included in the InfoJobs folder).
    Then, it will ask you for the Job Title and the Company's name.
Please note that empty cells are only allowed for jobs applied through InfoJobs which means you will have to provide all three components else the tracking is stopped. 

You can leave the program open until you are done with all your applications for the day.
At the end, your new registrations will be shown to you in order to make possible changes in case of an error. 
The program automatically records the date and inserts it in the spreadsheet.

You do not have to create any spreadsheet yourself nor the InfoJobs directory. Once run, the program creates everything for you! 

So, good luck with your job hunting and be sure to track it!
"""

parser = argparse.ArgumentParser(prog="Job Application Tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter, 
        description=help_message
        )
args = parser.parse_args()

# ------------ FUNCTIONS  ------------

# Make sure no job title or company is added empty. In this case, ask the user if he wants to exit the program.
def titles(_input):
    title = input(_input)
    if title != "":
        return title
    else:
        print(f"You didn't provide a {_input}.")
        print("Press Enter if you wanna exit the program")
        title = input(_input)
        if title != "":
            return title
        else:
            return

# Stop the process of job applications recording if the user wants it.
def empty_titles(title):
    if title != None: return False
    else: return True

# Write the dataframe to Excel
def write_spreadsheet(path, df):
    df.to_excel(
            "./Job_Aplications.xlsx",
            sheet_name="Job Applications",
            index=False
            )

# Check the input when the user gives a number to modify the data given
def check_input(position_number,df_temp):
    try:
        df_temp.iloc[int(position_number)]
    except:
        return False
    else:
        return True
# Change the input
def change_input(position_number, title, df_temp):
    given_title = df_temp[title].iloc[int(position_number)]
    new_title = input_with_prefill(f"{title}: ", given_title)
    return new_title

# Return the given job or company name if to be modified
def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


# ------------ MAIN PROGRAM ------------

# Make the InfoJobs directorie if not exist. 
if not Path('./InfoJobs/').is_dir(): os.mkdir('./InfoJobs')

# Register the date in the form dd/mm/yy
today = date.today().strftime("%d/%m/%y")

# Create an empty df to store the new data. Later on, it is added to the existing data in excel
df_temp = pd.DataFrame(columns=['Company', 'Job Title', 'url', 'Date of Aplication'])

# Parse through the InfoJobs directory. 
directory = './InfoJobs/'
files = [f for f in os.listdir(directory) if isfile(join(directory, f))]
if files:
    if directory == './InfoJobs/':
        print(f"Processing files from {directory}")
        for file in files:
            url = Infojobs(file, directory).url()
            if not url: continue # Checks if the file is .html or has the correct syntax. See the 'url' function of the webscraper.py
            job_title = Infojobs(file, directory).job_title()
            company_name = Infojobs(file, directory).company_name()

            # Check if None and ask for the user to manually introduce it.
            if url is None: url = input(f"Please manually insert the URL for the {file}:\nURL: ")
            if job_title is None: job_title = input("Please manually insert the Job Title for the {file}:\nJob Title: ")
            if company_name is None: company_name = input("Please manually insert the Company Name for the {file}:\nCompany Name: ")

            # Insert it to the df_temp
            if url or job_title or company_name:
                df_temp.loc[len(df_temp)] = [company_name, job_title, url, today]
                print(f"\n{job_title} in {company_name} has been recorded\n")
                # Remove the .html file
                os.remove(directory + file)
            else:
                print(f"No data given. The {file} is not registered nor removed.")
        print("---------------------------------------------")
        print("Inserting data from InfoJobs has finished")
        print("---------------------------------------------\n")

# Keep the program alive until the user does not give a url or until empty job title or company name is given twice.
while True:

    # Ask for the url
    url = input("URL: (press ENTER to finish) ")
    if(url == ""):

        print("Exiting.\nGood luck with the applications\n")
        break
    # Ask for the job title and the company's name
    else:
        job_title = titles("Job Title: ")
        if empty_titles(job_title): break

        company_name = titles("Company Name: ")
        if empty_titles(company_name): break
    
    # Insert the data into the dataframe
    df_temp.loc[len(df_temp)] = [company_name, job_title, url, today]
    print(f"\n{job_title} in {company_name} has been recorded\n")
    print("----------------------------------\n")

# Check if the user has given some data, else exit
if df_temp.empty:
    exit()


while True:
    # Show the data to confirm or to modidy them
    print("These are the data: \n")
    print(df_temp[['Company', 'Job Title']])

    # Ask the user if he wants to change something
    position_number = input("Give number of a job to change, else save with Enter: ")
    if position_number == "": break
    else:
        if check_input(position_number, df_temp):
            for title in ['Job Title', 'Company']:
                df_temp[title].iloc[int(position_number)] = change_input(position_number, title, df_temp)
        else: print(f"\nYou must give a number between 0 and {len(df_temp)-1}\n")

# If spreadsheet exists, read it and add the new data.
spreadsheet = Path("./Job_Aplications.xlsx") # The excel file's path
if spreadsheet.exists():
    df_original = pd.read_excel(spreadsheet)

    # Join the two dataframes
    df_original = pd.concat([df_temp, df_original], ignore_index=True)

    # Remove if Company or Job Title is not provided
    df_original.replace('', np.nan, inplace=True) # Replace empty strings with NaN
    print(df_original)
    df_original.dropna(inplace=True) 
    print(df_original)

    # Write the new df into the spreadsheet
    if not df_original.empty: write_spreadsheet(spreadsheet, df_original)

# If it does not exist, create it
else:
    write_spreadsheet(spreadsheet, df_temp)
