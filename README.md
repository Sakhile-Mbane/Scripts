# Title: Google Sheets Reminder Email Script

## Description:
The Google Sheets Reminder Email Script is a Python script that reads data from a Google Sheets document, checks for overdue reminders, and sends reminder emails to the specified recipients. The script uses the Gmail API to send emails and the gspread library to interact with the Google Sheets API.

## Prerequisites:
- Python 3.x installed
- Required Python libraries: Email_Scripts, pandas, gspread, oauth2client
- Access to the Gmail API and Google Sheets API (enabled and configured)
- Service account credentials JSON file from Google Cloud API

## Installation:
1. Clone or download the script files from the GitHub repository.
2. Install the required Python libraries by running the following command:
```
pip install -r requirements.txt
```
3. Obtain the service account credentials JSON file from the Google Cloud API:
   - Go to the Google Cloud Console (https://console.cloud.google.com).
   - Create a new project or select an existing one.
   - Enable the Gmail API and Google Sheets API for the project.
   - Create a service account key and download the credentials JSON file.
   - Copy the downloaded credentials JSON file to the script directory and rename it to `credentials.json`.

## Configuration:
1. Open the script file in a text editor.
2. Modify the `credentials_Dict` dictionary with the appropriate values from your credentials JSON file. This dictionary should contain the following keys: `type`, `project_id`, `private_key_id`, `private_key`, `client_email`, `client_id`, `auth_uri`, `token_uri`, `auth_provider_x509_cert_url`, `client_x509_cert_url`, and `universe_domain`.
3. Set the `credentials_file_path` variable to the path of your credentials JSON file.
4. Replace the `spreadsheet_url` variable with the URL of your Google Sheets document.

## Usage:
1. Make sure that the Google Sheets document contains the necessary data and headers.
2. Run the script using the following command:
```
python reminder_email_script.py
```
3. The script will read the data from the specified Google Sheets document, check for overdue reminders, and send reminder emails to the recipients whose reminders are overdue.
4. The script will print the total number of emails sent.

## Notes:
- The script uses the `Email_Scripts.send_mail` function to send emails. Make sure that the `send_mail` function is implemented correctly or replace it with your own email sending logic.
- The script assumes that the Google Sheets document has a header row and that the relevant columns are named 'Reminder_Date', 'Submitted', 'Email', 'Items', 'Name', and 'Due_Date'. Modify the script if your sheet has different column names.
- The email body in the script is written in HTML format. Modify the email template as needed to fit your requirements.
- The script provides a spreadsheet link in the email body. Update the link if necessary.

## License:
This script is licensed under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.

For any questions or issues, please contact [your-email@example.com].
