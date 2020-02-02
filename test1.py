import pymongo,argparse

myclient = pymongo.MongoClient('mongodb://localhost:27017')
artefact = myclient['Artefact']
collection=artefact['superhero']
myquery = {"Height":{"$type":"string"}}
newvalues = {"$set":{"Height":{"$type":"int"}}}
x = collection.update_many(myquery, newvalues)#set the type of "Height" as int
print(x.modified_count, "Height has been modified")

def output(gender,height):
	for item in list(collection.find({'Gender':gender,'Height':height})):
		print(item['\ufeffName'])

def appro_query(gender:str,height:int):
	if not gender=='Male' and not gender=='Female':
		print('wrong query!')
		exit()
	myfind=list(collection.find({'Gender':gender,'Height':height}))
	if not myfind:
		greatfind=list(collection.find({'Gender':gender,'Height':{'$gte':height}}).sort('Height'))
		littlefind=list(collection.find({'Gender':gender,'Height':{'$lte':height}}).sort('Height',-1))
		if not greatfind:
			output(gender, littlefind[0]['Height'])
		elif not littlefind:
			output(gender,greatfind[0]['Height'])
		elif abs(height-greatfind[0]['Height'])<abs(height-littlefind[0]['Height']):
			output(gender,greatfind[0]['Height'])
		elif abs(height-greatfind[0]['Height'])==abs(height-littlefind[0]['Height']):
			output(gender, littlefind[0]['Height'])
			output(gender, greatfind[0]['Height'])
		else:output(gender,littlefind[0]['Height'])
	else:
		output(gender,height)

parser = argparse.ArgumentParser()
parser.add_argument('-gender', type=str, help='input Male or Female')
parser.add_argument('-height', type=int, help='input height')
args = parser.parse_args()
appro_query(args.gender,args.height)