from datetime import datetime, date
import Email_Scripts
import pandas as pd
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
# downgrade the urllib3 == 1.26.15, to be able to use requests, since v2 doesn't support the latest SSL

# create a json file, format project key taken on google cloud API
cridentials_Dict = {
  "type": "service_account",
  "project_id": "finance-tracker-386612",
  "private_key_id": "ba87e64fa3994c81e4d8af2caac65a2ac2472cbd",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxVpMVsJ9R5fIh\nU0EelViWyqahuYhJJ9GQ7j9BL7sOftHgpzohtLnkitRiwylnf/z1bWJtShyAYOBR\n1K1hcP4ifcFEaPhDwpc4limL7mX0StSyGIcbWEn84KyrVFBOc1F9MzV3kc7wJb3n\n/A82JrxCllwTOpB3wUDE8ix2OkDHy5QtV+VMdNiLeCmVGnmXnb5a2Zt5RdtLtWCg\npdX+oyubIRufG1xSdvu2u0xjVEbNZoK44jPLVUtr5M5NrDv5bE0WFvwGleeAF7lD\nQ/ix9khiq4/xUmKGcELezwkIeV8yGhIA1wp31PZ55HUGgqoRqWSnM/x3yM9luvwK\nMiQwde2FAgMBAAECggEAIH+HENB/Qdjr2GOTaXFg/LFCfByt9woPA4pFmUKP+wYO\nnCbJJmgiMNmoNjkhm0//IVLcWL7eHkCimxxocZTtXZDCHDFIXdKJN9t83aHgmTYl\naEXKbJ5vYKIjwnn/BYFoi5MY10KnM6cW+C5e80OB+InpcbSnyOpnXjArKbdfK726\n365pAuenwk+e0M8oz2IqY0UJO6qwdAt/YiHVt617CtnUdiMz+ZRhxGutzukiQ9lE\nK2oRhi7RMvhptKr38gWCoVSiTNSPx5eKpo7ogcC1NVXhCSO+9TaVQCnwNucej4Nd\nYQs/Tt0Lp10CdXIvGtjX6x+RJW3+//ojqvvzfdgWuQKBgQDWMSpxw0eoLEXoFfn3\nW9aVAxxNhMrtbtg0JRqJ4H5mhfvsztce6uu55ieaMCnGSTP/NxiZKyMH6SbOyIkH\nnqkEF6khzpsY+HJckm2DiYvoK9G8uURhNXHDWAmr5L/xvHLvHd22tyJcSVPD4M7V\nZblhkcrKuFsNPZWBU+xqU5EoEwKBgQDT8+E2ShxgzTKoe/kKV9nhpjFryCU87Yil\n/T6mVewZBCjSOCpyFHLCEyLNz/F6p60pwQEh45bCLB+8psJVX2Dr06+ODFmFKIzi\n+gt31F0Y2UuDsK8mFixGK/D3qNU8CV8SFMvf9tToyvYHrcRx9WRg9UcrPyCWP1A+\n9jopsE93BwKBgQCEtgXUYuhdHMFboXI1fyOfREQfC64oGsu+01Z0IzJuF4oWGbpU\nH75aem4DLOBVSTn8YYjOLloQJrey27F7lSSnsnlKxxZ2DEnfbaKJI4oaGjxjsG7b\nxB9up3eml58OCnM0EM80zJdvksdh0EKXGeYYvBpoLH3N4GBntzX+UzTXHQKBgAMs\nMmHSqCwWxjxZZrft6rgC+dhoLY6E67e4W7i3rooNUuMarh/5CGK5UJsOEspIOkJW\nvkKYmogbivoS8PPAMr408/rHWouwuLMpFQTdK+uUTRoSifyi9lSyka/TWiXE6iRm\nJUsb8cHuT9J7mmYuSytcYI1YK4+0MOpQWzyGhBn/AoGAIMvw4y67CLgPK6IX6FW8\n81P4kk2E+2lHEz1JrXHoqEWHSeBiB6vWWGxeDWDvJTkDuPdH5xbzadHJLumatEuU\nNqzHP0tpOEGFb2zYnCZA74SpPrtyGWJ9yKZknP/xzX/65IIMgK40/N705t9EKP/a\n2u5nNVPsDJlTusb6UEY0kD8=\n-----END PRIVATE KEY-----\n",
  "client_email": "finance@finance-tracker-386612.iam.gserviceaccount.com",
  "client_id": "116656560626002631929",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/finance%40finance-tracker-386612.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


def json_func(cridentials_Dict):

    jsonString = json.dumps(cridentials_Dict)
    jsonFile = open("credentials.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    return 'Credentials json file created!!'

# Replace the credentials_file_path with the path to your credentials JSON file
credentials_file_path = '/Users/sakhile/Documents/Scripts/credentials.json'
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, scope)
gc = gspread.authorize(credentials)

# Replace the spreadsheet_url with your Google Sheets document URL
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1K5ZurKeEt7KX_PKx1oOXJrg7EQLfVwyVFJ7swS2uQhM/edit#gid=0'
sh = gc.open_by_url(spreadsheet_url)
worksheet = sh.sheet1

# Read the worksheet data into a pandas DataFrame
data = worksheet.get_all_values()
headers = data.pop(0)
data_df = pd.DataFrame(data, columns=headers)


def query_data_send_mails(df):
    present = date.today()
    email_counter = 0

    for _, row in df.iterrows():

        # condition to send email, if present day is greater than reminder date and submitted = N
        if (present >= datetime.strptime(row['Reminder_Date'], '%Y-%m-%d').date()) and (row['Submitted'] == 'N'):
            Email_Scripts.send_mail(sender = 'sakhilembane2@gmail.com',recipient = row['Email'],
                                     subject = 'WMG-SA finance department: Checklist Reminder',
                                     body = f"""
                                                <html>
                                                <head></head>
                                                <body>
                                                    <h1>WMG-SA finance department: {row['Items']} Reminder</h1>
                                                    
                                                    <p> Hello {row['Name']},</p>
                                                    
                                                    <p>I hope this mail finds you well.</p>
                                                    
                                                    <p>WMSA Finance department would like to reminds you that our record states that the {row['Items']} is due submission which is at {datetime.strptime(row['Due_Date'], '%Y-%m-%d').date()}.</p>
                                                    
                                        
                                                    <p>Please contact Thato Chiloane (thato.chiloane@warnermusic.com) regarding the outstanding documents. Your responses will be appreciated. </p>
                                                   
                                                    <p>Best Regards.</p>
                                                    <p>WMG_ZA - Bot reminder</p>
                                                </body>
                                                </html>
                                                """
                                                )
            
            email_counter += 1

    return f"Total Emails sent: {email_counter}"
        

results = query_data_send_mails(data_df)
print(results)


# Spreadsheet link
# <p> Link: https://docs.google.com/spreadsheets/d/1K5ZurKeEt7KX_PKx1oOXJrg7EQLfVwyVFJ7swS2uQhM/edit#gid=0 </p>