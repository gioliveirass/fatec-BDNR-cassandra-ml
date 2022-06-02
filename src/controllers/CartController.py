import sys
sys.path.insert(0,'d:\\GithubProjetos\\fatec-BDNR-cassandra-ml\\src\\services\\')
import BDconnect as BDconnect;

def getAllRedisInformations():
    myRedis = BDconnect.connectRedis()
    allInformations = myRedis.keys()
    print(allInformations)
    return allInformations

getAllRedisInformations()