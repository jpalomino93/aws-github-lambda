def lambda_handler(event, context):
   message = 'Hello {} !'.format(event['key1'])
   return {
       'Mensaje4' : message
   }
