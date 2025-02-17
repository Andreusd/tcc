import uuid
import boto3

NOME_TABELA = "tcc-lab"

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(NOME_TABELA)

# Gera um identificador aleatório
id = str(uuid.uuid4())

# Escrita
result = table.put_item(
    Item={
        "Id": id,
        "Nome": "André Uziel",
        "Github": "Andreusd",
        "Idade": 23,
    }
)

# Leitura
item = table.get_item(Key={"Id": id})
print(item["Item"])

# Exclusão
table.delete_item(Key={"Id": id})
