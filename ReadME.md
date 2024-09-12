## Setting up Lambda 
![image](https://github.com/user-attachments/assets/f0f461bb-9869-48ac-bd41-ba6fa21632ac)

To handle the logic for CRUD operations, I created a Lambda function named StudentRecordHandler. This function processes all incoming requests to the API and interacts with DynamoDB to create, read, update, and delete student records. The lambda.py file contains the actual code that performs these operations

## Setting up DynamoDB

![image](https://github.com/user-attachments/assets/fce10a86-8acb-4a31-b2c6-de7acf415723)
![image](https://github.com/user-attachments/assets/767220f4-9abd-4cbc-9b38-ef4fc28ccd8f)
![image](https://github.com/user-attachments/assets/090c58f9-a1f8-406d-a99f-e085c74be355)

I set up a DynamoDB table named StudentRecords, with student_id as the primary key. This ensures each student record has a unique identifier. DynamoDB was chosen because of its scalability and integration with AWS services like Lambda. Every operation (POST, GET, PUT, DELETE) interacts with this table to manage student data effectively.

## Setting up API Gateway
![image](https://github.com/user-attachments/assets/00fb9f12-ea7b-43ed-a1f9-19ab5cc73601)

API Gateway acts as the front door for the student record application. I created a new API with endpoints for each CRUD operation and connected it to the Lambda function. https://f7xphuzmw3.execute-api.us-east-2.amazonaws.com/dev/students

## IAM Policy

![image](https://github.com/user-attachments/assets/20374152-b363-43b2-bf3f-03216bddef8e)

When setting up Lambda, I had to create an IAM policy to grant the function the necessary permissions. This policy ensures that the Lambda function can read and write to the DynamoDB table, without giving it any excess permissions.

## Testing URL's

## POST

![image](https://github.com/user-attachments/assets/48933e70-a0a5-4789-af4f-72b60f947cb6)
![image](https://github.com/user-attachments/assets/f2813c8f-9bf6-40a3-8deb-4f4229599141)

The POST method is used to create a new student record. You'll need to include the student’s data in the request body (such as name, course and ID). Once the POST request is made, the API will insert this data into our DynamoDB table, and you'll receive a success message along with the new student’s ID.

## PUT
![image](https://github.com/user-attachments/assets/ce7b4cd3-ca2b-4125-a09a-6cdb41314d9a)
![image](https://github.com/user-attachments/assets/303791ab-9517-4148-bed3-c9b9504ba7c7)

The PUT method allows you to update an existing student’s record. You'll send the updated data in the request body, specifying the student ID.

## GET
![image](https://github.com/user-attachments/assets/f6517a0d-0755-406b-99fd-9a0bc081ed5e)
![image](https://github.com/user-attachments/assets/d0885195-da5a-483f-9992-ade91f376e8a)

The GET method retrieves a student’s record based on their ID. You’ll send a GET request to the API with the student’s ID in the URL. If the student exists, their information is returned in the response.

## DELETE:
![image](https://github.com/user-attachments/assets/4e6d72a1-7387-4512-af6e-085c4bee1108)
![image](https://github.com/user-attachments/assets/e5c04a90-ae85-4e78-a281-c4eb6971e10f)

The DELETE method removes a student’s record from the system. To delete a record, simply make a DELETE request to the API with the student ID in the URL. If the record is successfully deleted, you'll receive a confirmation response.

## Reflection 

Throughout this project, I had 2 good outcomes which helped me learn more about lambda

An interesting aspect of this project was completing it entirely within the AWS Free Tier.

1. Permission Configuration
One of the initial hurdles I faced was correctly configuring the IAM permissions. When I first deployed the Lambda function, I overlooked the importance of setting up the proper permissions for accessing DynamoDB. This led to "Access Denied" errors. To resolve this issue, I had to dive deeper into AWS IAM policies. I learned about the principle of least privilege and how to create a custom IAM policy that granted only the necessary permissions to my Lambda function.

2. Error Handling
As I developed the application, I realized the need for error handling. My initial implementation lacked comprehensive error management, which made debugging difficult and would have provided a poor user experience in a production environment. I addressed this by implementing more thorough try-except blocks, adding detailed logging, and ensuring that the API returned appropriate HTTP status codes along with descriptive error messages.





 

