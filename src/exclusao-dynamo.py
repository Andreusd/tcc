import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("tcc-lab")

table.delete_item(Key={"Id": "460c03ce-80e7-4876-9978-25afbc802c31"})
