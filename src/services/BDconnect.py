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

    row = session.execute("select release_version from system.local").one()
    if row:
        print(row[0])
    else:
        print("An error occurred.")

def connectRedis():
    myRedis = redis.Redis(
        host= CONFIG.redis_host,
        port= CONFIG.redis_port,
        password= CONFIG.redis_password
    )
    return myRedis