# aws-serverless-app
Serverless test app. Static website in S3 that communicates with an API Gateway endpoint that triggers a Lambda. We will use Step Functions also.
The diagram of the solution is the following:
![Alt text](https://github.com/dACEvid/aws-serverless-app/blob/main/diagram.png?raw=true)

Things to consider:
1) The email needs to be registered first in Simple Email Service (SES)
2) We need to create an S3 bucket to host our static website
3) Create Step Functions State Machine from the template. This just sends a remainder with a method of our choice
4) We need to create an API Gateway Endpoint, a Resource with CORS enabled and a POST method (Use Lambda Proxy Integration to run the api_handler.py Lambda)
