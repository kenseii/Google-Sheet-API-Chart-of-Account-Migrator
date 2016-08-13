from __future__ import print_function
import httplib2
import os
from frappeclient import FrappeClient
import csv
import sys


from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '10rLDRdF7h342s1py3eXLYzwkm-bKOhJHQcFYISdukSc'
    rangeName = 'A1:F200'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    

    if not values:
        print('No data found.')
    else:
        #print('Name, Major:')
        #client = FrappeClient("http://192.168.1.34:8000", "administrator", "chillington")
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s,%s,%s,%s,%s' % (row[0],row[1],row[2],row[3],row[4],row[5]))
            pname= row[5]
            code = row[0] + row[1] + row[2] + row[3] + row[4]
            roo = int(code[0])
            rootype="test"
            if roo==1:
                rootype="Asset"
                print (rootype)
            elif roo==2:
                rootype="Equity"
                print (rootype)
            elif roo==3 or roo==4:
                    
                rootype="Expense"
                print (rootype)
            elif roo==5:
                    
                rootype="Income"
                print (rootype)
            else:
                pass

            code=row[0]+row[1]+row[2]+row[3]+row[4]
            print (code)
            concode=code.replace('.','')
            print (concode)


            if len(concode)>=2:
                normal_acct=1
                parent = code[:-2]
                print (parent)

            else:
                print ("No parent")
                parent = "Wheelbarrow"
"""
            account = {"doctype": "Account",
                           "company": "WB",
                           "parent_account":parent,
                           "root_type":rootype,
                           "name": "-".join(row),
                           "account_name": "-".join(row),
                           "is_group": 1 if len(code) < 5 else 0,
                           "code": code}
            try:
                client.insert(account)
            except:
                pass

"""

                



if __name__ == '__main__':
    main()

