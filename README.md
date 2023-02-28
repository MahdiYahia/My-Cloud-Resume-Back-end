# My-Cloud-Resume
![Cloud Resume Diagram](https://user-images.githubusercontent.com/112518287/221832908-ec4a1c4d-9160-4770-b1ec-a3cd3ec1eed2.png)

Lately, I have been delving into the Cloud, and one of the things that came around was the Cloud resume challenge.
The main idea behind the challenge is to get your hands dirty using the cloud services and put your theoretical knowledge to work by creating a resume and hosting it on the Cloud.
You can check out the final result of my work here: www.mahdiyahia.com
You can find the code I wrote and some configuration files in this repository.
I started the challenge by working on the website front-end by writing the necessary HTML, CSS, and JavaScript. 
Afterward, I worked on deploying the front-end on S3 buckets and pointed my DNS domain name to them using the CloudFlare Content Delivery Network and also used its SSL/TLS to ensure traffic end-to-end encryption. 
Besides, I included a visitor counter on my website, the count is stored on a dynamodb table that is incremented by python code using the boto3 library, and the code is stored in a lambda function that is triggered by calling a REST API that I created using AWS API Gateway from Javascript. 
After setting up everything, I worked on automating my work. So I started by configuring the services mentioned above as Infrastructure as Code by defining them in an AWS Serverless Application Model as a 'yaml' template to be able to manage and provision the infrastructure through code instead of the manual process.
I also wrote python test cases and automated testing the lambda function against them by creating a GitHub actions workflow triggered when pushing modifications on the original code.
During my work, I also had the chance to set up policies and permissions using the AWS IAM and JSON.
