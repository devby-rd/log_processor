# log_processor
Python log processing tool integrated with AWS Lambda

This project is a Python-based log processing tool designed to extract error information from logs. The tool provides the total count of errors and a list of unique error messages. It includes:

- A function to process logs and extract error details.
- An AWS Lambda handler for deploying the solution on the cloud.
- Unit tests to ensure code reliability.



Prerequisites:

- Python 3.9 or higher.
- pytest for testing.
- AWS Account (for Lambda deployment)



Setup Instructions:

1. Clone git repository:
- git clone https://github.com/devby-rd/log_processor.git
- cd log_processor

2. Install dependencies:
- pip install -r requirements.txt

3. Run lambda_functions.py:
might need to modify function to accept custom inputs (from files or inputs)
- python lambda_functions.py



Deployment instructions:

1.  Zip the code: Create a ZIP archive containing lambda_function.py.
2.  Go to the AWS Lambda Console: Navigate to the Lambda service in the AWS Management Console.
3.  Create Lambda Function:
    - If creating a new function, click "Create function".
    - Select language python 3.9+
    - In "Configuration > General Configuration" set Memory - 128MB and Timeout - 30sec
4.  Upload the ZIP:
    - Under "Code source", choose "Upload from".
    - Select ".zip file" and upload the "lambda_function.zip" file you created.
5.  Save and Test: Save your function and test using Test Events.



Known Limitations:

- This function has a timeout of 30 seconds. If processing takes longer, the function will time out. 
- For longer tasks need to implement batching, asynchronous functions.

