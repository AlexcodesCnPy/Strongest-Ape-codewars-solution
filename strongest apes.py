#tried my hardest sorry if its inefficient comment on how i can make it better please



types =['Gorilla', 'Gibbon','Orangutan', 'Chimpanzee']
def TYPE(l_):
	typeDICT ={types[0]:[], types[1]:[],types[2]:[],types[3]:[]}
	for t in types:
		for f in l_:
			if f['type'] == t:
				typeDICT[t].append(f)
	return typeDICT

def find_the_strongest_apes(l_):
	sorted_=TYPE(l_)
	typeDICT ={types[0]:'', types[1]:'',types[2]:'',types[3]:''}
	for t in types:
		strength = []
		if len(sorted_[t]) > 1:			
			for i in range(len(sorted_[t])):
				point = sorted_[t][i]['weight'] + sorted_[t][i]['height']
				strength.append(point)
			if strength.count(strength[0]) != len(strength):
				highest = max(strength)
				for p in sorted_[t]:
					if sum([p['height'],p['weight']] == highest):
						typeDICT[t] = p['name']
			else:
				names=[]
				for q in sorted_[t]:
					names.append(q['name'])				
				typeDICT[t] = sorted(names)[0]
				
		elif len(sorted_[t]) == 1:
			typeDICT[t] = sorted_[t]['name']
		else:
			typeDICT[t] = None

	return typeDICT

print(find_the_strongest_apes([{"name": "aba", "weight": 101, "height": 99, "type": "Gorilla"},
             {"name": "abb", "weight": 99, "height": 101, "type": "Gorilla"},
             {"name": "abc", "weight": 101, "height": 99, "type": "Orangutan"},
             {"name": "abd", "weight": 99, "height": 101, "type": "Orangutan"}]))
