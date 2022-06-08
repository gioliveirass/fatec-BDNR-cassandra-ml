
import json
import sys
sys.path.insert(0,'d:\\GithubProjetos\\fatec-BDNR-cassandra-ml\\src\\services\\')
import BDconnect as BDconnect;

def getAllRedisInformations():
    myRedis = BDconnect.connectRedis()
    allInformations = myRedis.keys()
    return allInformations

def findCartInRedis(key):
    myRedis = BDconnect.connect()
    cart = myRedis.get(key)
    return cart

def addInfosInCassandra(infos):
    myCassandra = BDconnect.connectCassandra()
    myRedis = BDconnect.connectRedis()
    for key in infos:
        myInfo = myRedis.get(key)
        myCassandra.execute('use mercadoLivre;')
        myCassandra.execute(f"insert into carrinho (rediskey, products) values('{key}', {myInfo});")

def getAllInfosFromCassandra():
    myCassandra = BDconnect.connectCassandra()
    myCassandra.execute('use mercadoLivre;')
    myCassandra.execute(f'select * from carrinho;')
        
infos = getAllRedisInformations()
addInfosInCassandra(infos)
getAllInfosFromCassandra()