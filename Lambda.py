import json
import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event, indent=2)}")
    
    try:
        http_method = event['httpMethod']
        logger.info(f"HTTP Method: {http_method}")

        if http_method == 'POST':
            body = event.get('body', '{}')
            if isinstance(body, str):
                body = json.loads(body)
            return create_student(body)
        elif http_method == 'GET':
            student_id = event.get('queryStringParameters', {}).get('student_id')
            return read_student(student_id)
        elif http_method == 'PUT':
            body = event.get('body', '{}')
            if isinstance(body, str):
                body = json.loads(body)
            return update_student(body)
        elif http_method == 'DELETE':
            student_id = event.get('queryStringParameters', {}).get('student_id')
            return delete_student(student_id)
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Unsupported HTTP method')
            }
    except KeyError as e:
        logger.error(f"KeyError: Missing key in event: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"Invalid request: Missing {e}")
        }
    except json.JSONDecodeError as e:
        logger.error(f"JSONDecodeError: Invalid JSON in request body: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid JSON in request body')
        }
    except Exception as e:
        logger.error(f"Unexpected error in lambda_handler: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal server error')
        }

def create_student(student_data):
    logger.info(f"Attempting to create student with data: {json.dumps(student_data)}")
    
    try:
        # Validate required fields
        required_fields = ['student_id', 'name', 'course']
        for field in required_fields:
            if field not in student_data:
                logger.error(f"Missing required field: {field}")
                return {
                    'statusCode': 400,
                    'body': json.dumps(f"Missing required field: {field}")
                }
        
        # Ensure student_id is a string
        student_data['student_id'] = str(student_data['student_id'])
        
        logger.info(f"Putting item into DynamoDB: {json.dumps(student_data)}")
        table.put_item(Item=student_data)
        
        logger.info("Student created successfully")
        return {
            'statusCode': 200,
            'body': json.dumps('Student created successfully')
        }
    except ClientError as e:
        logger.error(f"DynamoDB ClientError: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error creating student: Database operation failed')
        }
    except Exception as e:
        logger.error(f"Unexpected error in create_student: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Unexpected error creating student')
        }

def read_student(student_id):
    logger.info(f"Attempting to read student with ID: {student_id}")
    
    try:
        response = table.get_item(Key={'student_id': student_id})
        
        if 'Item' in response:
            logger.info(f"Student found: {json.dumps(response['Item'])}")
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            logger.info(f"Student with ID {student_id} not found")
            return {
                'statusCode': 404,
                'body': json.dumps('Student not found')
            }
    except ClientError as e:
        logger.error(f"DynamoDB ClientError in read_student: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error reading student: Database operation failed')
        }
    except Exception as e:
        logger.error(f"Unexpected error in read_student: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Unexpected error reading student')
        }

def update_student(student_data):
    logger.info(f"Attempting to update student with data: {json.dumps(student_data)}")
    
    try:
        if 'student_id' not in student_data:
            logger.error("Missing student_id in update data")
            return {
                'statusCode': 400,
                'body': json.dumps('Missing student_id in update data')
            }
        
        student_id = str(student_data['student_id'])
        update_expression = "set "
        expression_attribute_values = {}
        
        for key, value in student_data.items():
            if key != 'student_id':
                update_expression += f"#{key} = :{key}, "
                expression_attribute_values[f':{key}'] = value
        
        update_expression = update_expression.rstrip(', ')
        
        response = table.update_item(
            Key={'student_id': student_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames={f'#{k}': k for k in student_data.keys() if k != 'student_id'},
            ReturnValues="UPDATED_NEW"
        )
        
        logger.info(f"Student updated successfully: {json.dumps(response['Attributes'])}")
        return {
            'statusCode': 200,
            'body': json.dumps('Student updated successfully')
        }
    except ClientError as e:
        logger.error(f"DynamoDB ClientError in update_student: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error updating student: Database operation failed')
        }
    except Exception as e:
        logger.error(f"Unexpected error in update_student: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Unexpected error updating student')
        }

def delete_student(student_id):
    logger.info(f"Attempting to delete student with ID: {student_id}")
    
    try:
        response = table.delete_item(
            Key={'student_id': student_id},
            ReturnValues="ALL_OLD"
        )
        
        if 'Attributes' in response:
            logger.info(f"Student deleted successfully: {json.dumps(response['Attributes'])}")
            return {
                'statusCode': 200,
                'body': json.dumps('Student deleted successfully')
            }
        else:
            logger.info(f"Student with ID {student_id} not found for deletion")
            return {
                'statusCode': 404,
                'body': json.dumps('Student not found')
            }
    except ClientError as e:
        logger.error(f"DynamoDB ClientError in delete_student: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error deleting student: Database operation failed')
        }
    except Exception as e:
        logger.error(f"Unexpected error in delete_student: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Unexpected error deleting student')
        }
