from contextlib import _GeneratorContextManager
import json
import sys
import random
import requests
if __name__ == '__main__':
    url = "https://hooks.slack.com/services/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"
    locale1="de-de"
    username="ganga"
    ticketnum=1234
    message = ("Deployment for {} with ticket no: {} has been deployed by {} ".format(locale1,ticketnum,username))
    title = (f"New Incoming Message :zap:")
    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":satellite:",
        "channel" : "alerts",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Deplyment Completed",
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Ticket Number:*\n%s" %ticketnum
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Sanity URL:*\n<example.com|Fred Enriquez>"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Locale:*\n%s" %locale1
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Triggered By:*\%s" %username
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Image Tag:*\n1.21.0.3"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "*Env:*\nSTG"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Successfully Completed"
                }
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
