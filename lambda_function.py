import re
import traceback
from typing import Dict, List


def process_log_file(log_content: str) -> Dict[str, List[str]]:

    try:
        # Initialize result dictionary
        result = {
            'total_errors': 0,
            'unique_error_messages': []
        }

        log_content.strip()

        # Regex to match log entries with level and message
        # log entry format: "[YYYY-MM-DD HH:MM:SS] LEVEL: Message"
        log_pattern = re.compile(r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] ERROR: (.+)$', re.MULTILINE)
        
        # Extract all error messages
        error_messages = log_pattern.findall(log_content)

        # Update total_errors count
        result['total_errors'] = len(error_messages)

        # Extract unique error messages using set function
        result['unique_error_messages'] = list(set(error_messages))

        return result
    
    except Exception as e:
        raise ValueError(f"An error occurred while processing the log file: {e}")


def lambda_handler(event, context):
    # get data from event else assign default values
    candidate_id = event.get('candidate_id', '')
    log = event.get('log_content', '')

    try:
        result = process_log_file(log)

        # return status 200 and result on success
        response = {
            "statusCode": 200,
            "body": {
                "candidate_id": candidate_id,
                "result": result
            } 
        }
        return response
    
    except Exception as e:
        # print stack trace
        traceback.print_exc()
        print('\n')

        # return status 400 and error on exception
        response = {
            "statusCode": 400,
            "error": str(e)
        }
        return response