#!/usr/bin/env python3

########################################################################
#                       Job Aplication Tracker                         #
#             Easily track the job applications you have done.         #
#                         Written in Pyton.                            #
#                                                                      #
#                           Version 0.1                                #
#----------------------------------------------------------------------#
#                   Licence: Apache License 2.0                        #
#                                                                      #
#   Creator: Ioannis Doganos, github: https://github.com/Ioannis-D     #
########################################################################

# ------------ LIBRARIES USED ------------
from datetime import date # For the current day
from pathlib import Path # To check if the spreadsheet exists
import pandas as pd # To manipulate the data and the spreadsheet
import time # For the sleep operation
import readline # To pre-print the Job and Company already given if the user wants to modify them
import argparse # For the help message

# ------------ HELP MESSAGE ------------
help_message = """
This is a program written in Python for letting you store your job applications nicely and tidy into a spreadsheet (.xlsx). 

It is easy and fast to use:
    Firstly, the program will ask you to insert the url of the job position you have applied.
    Secondly, it will ask you for the Job Title and the Company's name.
Please note that empty cells are not allowed which means you will have to provide all three components else the tracking is stopped. 

You can leave the program open until you are done with all your applications for the day.
At the end, your new registrations will be shown to you in order to make possible changes in case of an error. 
The program automatically records the date and inserts it in the spreadsheet.

You do not have to create any spreadsheet yourself. Once run, the program creates everything for you! 

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

# Register the date in the form dd/mm/yy
today = date.today().strftime("%d/%m/%y")

# Create an empty df to store the new data. Later on, it is added to the existing data in excel
df_temp = pd.DataFrame(columns=['Company', 'Job Title', 'url', 'Date of Aplication'])

# Keep the program alive until the user does not give a url or until empty job title or company name is given twice.
while True:

    # Ask for the url, the job title and the company's name
    url = input("URL: (press ENTER to finish) ")
    if(url == ""): # If url is given empty it means the user wants to exit.
        print("Exiting.\nGood luck with the applications\n")
        break

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
        else: 
            print(f"\nYou must give a number between 0 and {len(df_temp)-1}\n")
            time.sleep(1) # Make sure the user sees the message

# If spreadsheet exists, read it and add the new data.
spreadsheet = Path("./Job_Aplications.xlsx") # The excel file's path
if spreadsheet.exists():
    df_original = pd.read_excel(spreadsheet)

    # Join the two dataframes
    df_original = pd.concat([df_temp, df_original], ignore_index=True)

    df_original[['Company', 'Job Title']].dropna() # Remove if Company or Job Title is not provided

    # Write the new df into the spreadsheet
    write_spreadsheet(spreadsheet, df_original)

# If it does not exist, create it
else:
    write_spreadsheet(spreadsheet, df_temp)
