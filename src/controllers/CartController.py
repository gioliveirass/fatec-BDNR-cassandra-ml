
import sys
sys.path.insert(0,'d:\\GithubProjetos\\fatec-BDNR-cassandra-ml\\src\\')

import BDconnect as BDconnect;
import simplejson as json

def getAllRedisInformations():
    myRedis = BDconnect.connectRedis()
    allInformations = myRedis.keys()
    return allInformations

def findCartValueInRedis(key):
    myRedis = BDconnect.connectRedis()
    cart = myRedis.get(key)
    print(f'PRODUTOS DO CARRINHO {key}')
    print(cart)

def addInfosInCassandra(infos):
    myCassandra = BDconnect.connectCassandra()
    myRedis = BDconnect.connectRedis()
    myCassandra.execute('use mercadolivre;')
    for key in infos:
        value = myRedis.get(key)
        myCassandra.execute(f"insert into cart (key, value) values('{key}', '{value}');")

def getAllInfosFromCassandra():
    myCassandra = BDconnect.connectCassandra()
    myCassandra.execute('use mercadoLivre;')
    cassData = myCassandra.execute(f'select * from cart;')

    print('TODOS OS CARRINHOS CADASTRADOS')
    
    if(not cassData):
        print(json.dumps({"message":"Dados não encontrados"}))
    
    for data in cassData:
        print(json.dumps({"key": data.key, "value": data.value}))
    