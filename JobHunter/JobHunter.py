# This script pulls from a job website and stores positions into a database. If there is a new posting it notifies the user.
# CNA 330
# Zachary Rubin, zrubin@rtc.edu
# T.J. Dewey, tjdewey@student.rtc.edu
# Help on add new job function from Mohhammad Pakizehjam
# Help on entire document from Justin Ellis
import mysql.connector
import sys
import json
import urllib.request
import os
import time

# Connect to database
# You may need to edit the connect function based on your local settings.
def connect_to_sql():
    conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='cna330')
    return conn

# Create the table structure
def create_tables(cursor):
    ## Add your code here. Starter code below
    cursor.execute('''CREATE TABLE IF NOT EXISTS Jobs_found (id INT PRIMARY KEY auto_increment,
                        Type varchar(10), Title varchar(100), Description TEXT, Job_id varchar(33),
                        Created_at DATE, Company varchar(100), location varchar(50),
                        How_to_apply varchar(1000));''')
    return

# Query the database.
# You should not need to edit anything in this function
def query_sql(cursor, query):
    cursor.execute(query)
    return cursor

# Add a new job
def add_new_job(cursor, jobdetails):
    ## Add your code here
    query = "INSERT INTO"
    return query_sql(cursor, query)

# Check if new job
def check_if_job_exists(cursor, jobdetails):
    ## Add your code here
    type = jobdetails['type']
    title = jobdetails['title']
    description = jobdetails['description']
    job_id = jobdetails['id']
    created_at = time.strptime(jobdetails['created_at'], "%a %b %c %H:%M:%S %Z %Y")
    company = jobdetails['company']
    location = jobdetails['location']
    how_to_apply = jobdetails['how_to_apply']
    query = (INSERT INTO jobs (catagories) VALUES(%s, %s, %s, %s, %s, %s, %s, %s,)
                           (type, title, description, job_id, created_at, company,
                            location, how_to_apply))
    return query_sql(cursor, query)

# Check if new job
def check_if_job_exists(cursor, jobdetails, table="Jobs_found"):
    ## Add your code here
    job_id = jobdetails['id']
    query = "SELECT * FROM jobs WHERE Job_id = \'%s\'" % job_id
    return query_sql(cursor, query)

def delete_job(cursor, jobdetails):
    ## Add your code here
    job_id = Jobdetails['id']
    query = "DELETE FROM jobs WHERE job_id = \'%s\'" % job_id
    return query_sql(cursor, query)

# Grab new jobs from a website
def fetch_new_jobs(arg_dict):
    # Code from https://github.com/RTCedu/CNA336/blob/master/Spring2018/Sql.py
    query = "https://jobs.github.com/positions.json?" + "location=seattle" ## Add arguments here
    jsonpage = 0
    try:
        contents = urllib.request.urlopen(query)
        response = contents.read()
        jsonpage = json.loads(response)
    except:
        pass
    return jsonpage

# Load a text-based configuration file
def load_config_file(filename):
    argument_dictionary = 0
    # Code from https://github.com/RTCedu/CNA336/blob/master/Spring2018/FileIO.py
    rel_path = os.path.abspath(os.path.dirname(__file__))
    file = 0
    file_contents = 0
    try:
        file = open(filename, "r")
        file_contents = file.read()
    except FileNotFoundError:
        print("File not found, it will be created.")
        file = open(filename, "w")
        file.write("")
        file.close()

    ## Add in information for argument dictionary
    return argument_dictionary

# Main area of the code.
def jobhunt(arg_dict, cursor):
    # Fetch jobs from website
    jobpage = fetch_new_jobs(arg_dict)
    #! print (jobpage) #?suggested or required?
    ## Add your code here to parse the job page
        #? parse arg_dict into 'job details" var here?
    add_or_delete_job(jobpage, cursor)
def add_or_delete_job(jobpage, cursor):
    ## Add in your code here to check if the job already exists in the DB
    for detail in jobpage:
        check_if_job_exists(cursor, details)
        is_job_found = len(cursor.fetchall()) > 0
        ## Add in your code here to notify the user of a new posting
        if is_job_found:
            print("Last job found: " + jobdetails['title'] + " from " + jobdetails["company"])
        else:
            print("New job found:" + jobdetails['title'] + " from " + jobdetails["company"])
            add_new_job(cursor, jobdetails)
    ## EXTRA CREDIT: Add your code to delete old entries

# Setup portion of the program. Take arguments and set up the script
# You should not need to edit anything here.
def main():
    # Connect to SQL and get cursor
    conn = connect_to_sql()
    cursor = conn.cursor()
    create_tables(cursor)
    # Load text file and store arguments into dictionary
    arg_dict = load_config_file(sys.argv[1])
    while(1):
        jobhunt(cursor, arg_dict)
        conn.commit()
        time.sleep(3600) # Sleep for 1h

if __name__ == '__main__':
    main()
