
import sys
sys.path.insert(0,'d:\\GithubProjetos\\fatec-BDNR-cassandra-ml\\src\\')

import controllers.CartController as cartController

infos = cartController.getAllRedisInformations()
cartController.addInfosInCassandra(infos)
cartController.getAllInfosFromCassandra()
cartController.findCartValueInRedis("carrinho:gio")