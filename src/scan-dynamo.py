import boto3

NOME_TABELA = "tcc-lab"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(NOME_TABELA)

result = table.scan()

print(result["Items"])
