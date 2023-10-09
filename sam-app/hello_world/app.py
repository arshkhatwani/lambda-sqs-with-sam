import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    logger.info('Received event: %s', event)
    event = event['Records'][0]

    event_body = json.loads(event['body'])

    length = int(event_body['length'])
    width = int(event_body['width'])
    
    logger.info('Input length: %s, width: %s', length, width)

    area = length * width

    logger.info('Calculated area %s', area)

    return {
        "area": area
    }
