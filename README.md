# Blackboard-to-GCal
This is a simple program that imports user's events from their college Blackboard Portal to Google Calendar App.\
\
This reads the user's credentials from a text file, and logs in automatically from Blackboard, and uses the export ical function to download an iCal(.ics) file. \
This file is then parsed and the useful data is converted to a CSV(.csv) file which is then added to your Google Calendar using the API. 

# Steps to use
1. Clone this repository  
`git clone https://github.com/c0mr4d3/Blackboard-to-GCal`

2. Navigate to the project directory
`cd Blackboard-to-GCal`

3. Install the requirements
`pip install -r requirements.txt`

4. Create a text file, named `secret.txt` with your blackboard username and password in the format
`username:password`

5. Activate Google calendar API from the link below \
https://developers.google.com/calendar/quickstart/python
![Activate Google API](https://github.com/c0mr4d3/Blackboard-to-GCal/blob/master/google_auth.png)

6. Download the `credentials.json` from above link and place it in the working directory i.e. `Blackboard-to-Gcal`
![Download credentials.json](https://github.com/c0mr4d3/Blackboard-to-GCal/blob/master/google_credentials.png)

7. Run the file `python ical.py`

8. A browser popup will appear asking permissions for Google API to access your email, select **the same email** which you used for enabling Google API, and grant persmissions.

# To-do
1. Add the blackboard links to Google Calendar Event description
2. Improve the wait times using Selenium functions instead of `time.wait`

Any pull requests are welcome. 
