import pymongo as pm
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)
col_libros=serv.Libreria.libros
col_libros.update_one({'isbn': 'yu12'},{'$set':{'precio': 10.7}})
libros=col_libros.find({"categoria":"programación"})
for lb in libros:
    print(lb)
serv.close()