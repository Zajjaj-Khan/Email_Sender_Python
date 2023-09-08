
# Email Sender Using Python

Using a *to_emails* variable as a list to send an email to the group of people at once, Its a handly tool when it comes to emailing multiple people or clients




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

add your gmail username:
`MY_USERNAME`
add your gmail password:
`MY_PASSWORD`


## Python Libraries

```python
import os #for .env file
import smtplib #smtp server connection
import MIMEText #text formattor for emails
import MIMEMultipart
```
