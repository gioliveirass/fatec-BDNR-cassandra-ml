import redis
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import config as CONFIG

def connectCassandra():
    cloud_config= {
            'secure_connect_bundle': CONFIG.secure_connect_bundle_path
    }

    auth_provider = PlainTextAuthProvider(CONFIG.cassandra_clientID, CONFIG.cassandra_client_secret)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    
    return session

def connectRedis():
    myRedis = redis.StrictRedis(
        host= CONFIG.redis_host,
        port= CONFIG.redis_port,
        password= CONFIG.redis_password,
        decode_responses=True
    )
    return myRedis