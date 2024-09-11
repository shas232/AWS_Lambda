# Testing URL's

## POST

![image](https://github.com/user-attachments/assets/48933e70-a0a5-4789-af4f-72b60f947cb6)
![image](https://github.com/user-attachments/assets/f2813c8f-9bf6-40a3-8deb-4f4229599141)

## PUT
![image](https://github.com/user-attachments/assets/ce7b4cd3-ca2b-4125-a09a-6cdb41314d9a)
![image](https://github.com/user-attachments/assets/303791ab-9517-4148-bed3-c9b9504ba7c7)
 
## GET
![image](https://github.com/user-attachments/assets/f6517a0d-0755-406b-99fd-9a0bc081ed5e)
![image](https://github.com/user-attachments/assets/d0885195-da5a-483f-9992-ade91f376e8a)
  
## DELETE:
![image](https://github.com/user-attachments/assets/4e6d72a1-7387-4512-af6e-085c4bee1108)
![image](https://github.com/user-attachments/assets/e5c04a90-ae85-4e78-a281-c4eb6971e10f)

## Setting up Lambda 
![image](https://github.com/user-attachments/assets/f0f461bb-9869-48ac-bd41-ba6fa21632ac)

Have added the Lambda code in the repository 

## Setting up DynamoDB

![image](https://github.com/user-attachments/assets/fce10a86-8acb-4a31-b2c6-de7acf415723)
![image](https://github.com/user-attachments/assets/767220f4-9abd-4cbc-9b38-ef4fc28ccd8f)
![image](https://github.com/user-attachments/assets/090c58f9-a1f8-406d-a99f-e085c74be355)

## Setting up API Gateway
![image](https://github.com/user-attachments/assets/00fb9f12-ea7b-43ed-a1f9-19ab5cc73601)

## IAM Policy

![image](https://github.com/user-attachments/assets/20374152-b363-43b2-bf3f-03216bddef8e)

## Reflection 

Throughout this project, I had 2 good outcomes which helped me learn more about lambda

An interesting aspect of this project was completing it entirely within the AWS Free Tier.

1. Permission Configuration
One of the initial hurdles I faced was correctly configuring the IAM permissions. When I first deployed the Lambda function, I overlooked the importance of setting up the proper permissions for accessing DynamoDB. This led to "Access Denied" errors. To resolve this issue, I had to dive deeper into AWS IAM policies. I learned about the principle of least privilege and how to create a custom IAM policy that granted only the necessary permissions to my Lambda function.

2. Error Handling
As I developed the application, I realized the need for error handling. My initial implementation lacked comprehensive error management, which made debugging difficult and would have provided a poor user experience in a production environment. I addressed this by implementing more thorough try-except blocks, adding detailed logging, and ensuring that the API returned appropriate HTTP status codes along with descriptive error messages.





 

