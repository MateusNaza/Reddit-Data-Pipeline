import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(
            anon=False,
            key=AWS_ACCESS_KEY_ID,
            secret=AWS_SECRET_ACCESS_KEY
        )
        return s3
        print('Conectado ao S3 com sucesso!')
    except Exception as e:
        print(e)


def create_bucket_if_not_exists(s3: s3fs.S3FileSystem, bucket_name:str):
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            print(f'Bucket {bucket_name} criado com sucesso!')
        else:
            print(f'Bucket {bucket_name} já existe!')
    except Exception as e:
        print(e)


def upload_to_s3(s3: s3fs.S3FileSystem, bucket_name:str, file_path: str, file_name:str):
    try:
        s3.put(file_path, bucket_name+'/bronze/'+file_name)
        print(f'Arquivos carregados com sucesso no Bucket {bucket_name}')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        