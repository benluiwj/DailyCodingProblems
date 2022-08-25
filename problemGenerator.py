from __future__ import print_function
import base64

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_latest_problem():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        dcp_label = None

        if not labels:
            print('No labels found.')
            return
    
        for label in labels:
            if label['name'] == 'Daily Coding Problems':
                    dcp_label = label
                    break
        
        questions = dict()
        dcp = service.users().messages().list(userId='me', labelIds=dcp_label['id']).execute().get('messages', [])
        for i in range(len(dcp)):
                latest_problem_id = dcp[i]['id']
                latest_problem = service.users().messages().get(userId='me', id=latest_problem_id).execute()
                data = latest_problem['payload']['parts'][0]['body']['data']
                problem_number = None
                for header in latest_problem['payload']['headers']:
                        if 'name' in header and header['name'] == 'Subject':
                                problem_number = (header['value'])
                data = data.replace("-","+").replace("_","/")
                decoded_data = base64.b64decode(data)
                complete_question = decoded_data.decode('utf-8')
                question_end = complete_question.find('--------------------------------------------------------------------------------')
                complete_question = complete_question[:question_end]
                questions[complete_question[:-5]] = problem_number
        return questions
        

        

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
        
        if not os.path.exists('settings.txt'):
                print("Creating settings file...")
                file_type = input('Please input in your langauge file extension (.py for python, .java for java, etc): \n')
                comment_token = input('Please input in your language comment style (# for python, // for java, etc): \n')
                settings = str(file_type) + " " + str(comment_token)
                
                with open('Settings.txt', 'w') as f:
                        f.write(settings)
        
        else:
                print("Reading from settings file")
                f = open('Settings.txt', "r")
                file_type, comment_token = f.readline().split()
        
        questions = get_latest_problem()
        for question, question_num in questions.items():
                question_num += file_type
                commented_out_question = ""
                question = question.split('\n')
                for line in question:
                        if line == '\r' or line == '':
                                commented_out_question +=  line
                        else:
                                commented_out_question += comment_token + ' ' + line
                with open(question_num, 'w') as f:
                        f.write(commented_out_question)
                        if file_type == ".py":
                                f.write("from typing import * \n")
                
                print(f"{question_num} successfully generated!")