from time import sleep
from uuid import uuid4

def create_guid():
    guid = str(uuid4()).replace('-','').upper()
    return guid

while True:
    print(create_guid())
    sleep(5)


