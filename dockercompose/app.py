from ast import Return
import time

import redis
from flask import Flask
from datetime import datetime
import hashlib

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def insertTableS(id):
    id='id'+str(id)
    time=getTimeStamp()
    hash=str(generateHash(id, time))
    time=str(time)
    print('el hash es: '+hash)
    temporal=str(time+','+hash)
    cache.set(id, temporal)
    print(cache.get(id))

def insertTableA(id, hashIn):
    id='id'+str(id)
    hash=str(getHashTableS(id))
    time=str(getTimeStamp())
    respuesta=id
    cache.set(hash,str(id)+','+time+','+respuesta)

def getHashTableS(id):
    auxiliar=cache.get(id)
    auxiliar=str(auxiliar)
    vector=auxiliar.split(',')
    print (vector)
    return vector[1]

def getTimeTableS(id):
    auxiliar=cache.get(id)
    return auxiliar.split(',')[0]

def isValid(id):
    
    return 

def generateHash(id, time):
    id=str(id)
    time=str(time)
    salida = hash(id+time)
    return salida

def getTimeStamp():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp

def listenEntrada(entrada):
    #saber si es una entrada con hash o no
    return 

def getId(entrada):
    #falta sacar id
    return

def getHash(entrada):
    #falta sacar hash
    return

def clean (vector):
 for i in range (len(vector)):
    vector[i]=str(vector[i]).replace('b','')
    vector[i]=str(vector[i]).replace("'",'')
    vector[i]=str(vector[i]).replace("i",'')
    vector[i]=str(vector[i]).replace("d",'')
 return vector


def scan_keys(r, pattern):

    result = []
    cur, keys  = cache.scan(cursor=0, match=pattern, count=2)
    result.extend(keys)
    while cur != 0:
        cur, keys = cache.scan(cursor=cur, match=pattern, count=2)
        result.extend(keys)
        
    return result

@app.route('/')
def hello():
 entrada=1000
 insertTableS(1000)
 insertTableS(1001)
 insertTableS(1002)
 print(scan_keys(cache,'id******'))
 print(clean(scan_keys(cache,'id******')))
 hayhash=listenEntrada(entrada)
 hayHash=True
 if (hayHash):
        id=getId(entrada)
        hash=getHash(entrada)
        insertTableA(id, entrada)
 else:
        id=getId(entrada)
        insertTableS(id)  

 return 'hello'  
    #id=algo

    #insertTableS(id)
    #return 'Hello World! I have been seen {} times.\n'.format(count)