import json
import multiline

# some JSON:
x =  """{
  "Records": [
    {
      "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
      "receiptHandle": "MessageReceiptHandle",
      "body":{
              "Type" : "Notification",
              "MessageId" : "84102bd5-8890-4ed5-aeba-c15fafc926dc",
              "TopicArn" : "arn:aws:sns:eu-west-1:534706846367:HelloWorld",
              "Message" : "hello World",
              "Timestamp" : "2012-06-05T13:44:22.360Z",
              "SignatureVersion" : "1",
              "Signature" : "Qzh0qXhijBKylaFwc9PGE+lQQDwHGWkIzCW2Ld1eVrxNfSem4yyBTgouqGX26V0m1qhFD4RQcBzE3oNqx5jFhJfV4hN45FNcsFVnmfLPGNUTmJWblSk8f6znWgTy8UtK9xrTeNYzK59k3VJ4WTJ5kCEj+2vH7sBV15fAXeCAtdQ=",
              "SigningCertURL" : "https://sns.eu-west-1.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem",
              "UnsubscribeURL" : "https://sns.eu-west-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-1:534706846367:HelloWorld:8a3acde2-cb0b-4a56-9b9c-b75ed7307556"
            },
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1523232000000",
        "SenderId": "123456789012",
        "ApproximateFirstReceiveTimestamp": "1523232000001"
      },
      "messageAttributes": {},
      "md5OfBody": "{{{md5_of_body}}}",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
      "awsRegion": "us-east-1"
    }
  ]
}"""


eventDict = json.loads(x)
b1Text = json.dumps(eventDict['Records'][0])

print( b1Text )

# parse x:
y = multiline.loads(x, multiline=True)

# the result is a Python dictionary:
# print(y["Records"])

message = y['Records'][0]['body']

print( message['Type'] )

data = json.loads(message)


CustID = data['CustID']
Name = data['Name']
print( Name )
