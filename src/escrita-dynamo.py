import uuid
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("tcc-lab")

table.put_item(
    Item={
        "Id": str(uuid.uuid4()),
        "Nome": "André Uziel",
        "Github": "Andreusd",
        "Idade": 23,
    }
)
