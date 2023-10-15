# #aws lambda function to validate the file
# """{
#   "resource":"/file",
#   "path":"/report",
#   "httpMethod":"POST",
#   "headers":{},
#   "multiValueHeaders":{},
#   "queryStringParameters":"None",
#   "multiValueQueryStringParameters":"None",
#   "pathParameters":"None",
#   "stageVariables":"None",
#   "requestContext":{},
#   "body":"---------------------------048403183655214093472440\r\nContent-Disposition: form-data; name=\"file\"; filename=\"sample.csv\"\r\nContent-Type: text/csv\r\n\r\nName,Roll No.,Date"
# }"""
# import json
# import boto3
#
# def validate_file(event):
#       #validate  Body
#      if event['body']== None:
#          return 'File should be attached'
#
#      #validate the file type:
#       file_type = None#= get_file_type(event)
#      if file_type !='text/csv':
#         logger.error('')
#         return 'file type should be csv'
#
#
#
#
# def lambda_handler(event,context):
#
# err = validate_file(event)
#    if err!=None:
#        return create_response(400,err)
#
# err = upload_File(event)
#    if err!=None:
#      return create_response(400, err)
#
# return create_response(200, 'file uploaded successfully')
#
#  def create_response(status_code,reposne):
#      return {
#          "statuscode":status_code,
#          "body":json.dumps({"result":reposne})
#      }
#
#
# def upload_File():
#
#
#
#
