const x  = {'storeId': 'Kitty Buds', 'machineId': 'WarmMoon', 'spools': [{'mandatory': {'keys': 'SPOOL', 'spool': 'A1', 'uid': '15643151 - A1', 'count': 9, 'price': 25}, 'optional': {'type': 'Flower', 'grams': 3.5, 'producer': 'Paddle Creek Cannabis', 'strain': 'Green Arrow', 'classification': 'Sativa', 'batchinfo': 'KLT - 685115300', 'harvest': '06/22/23', 'canabinoids': 21, 'thc-a': 4, 'delta_9': 9, 'cbd': 5}}]}

//console.log( Object.keys( x['spools'][0]['mandatory']  )) 
//console.log( Object.keys( x['spools'][0]['optional']  )) 

x['spools'].forEach(( row ) => { 
	mandatory = row['mandatory'] 
	optional = row['optional'] 
	console.log(mandatory ) 
	console.log(optional) 
}) 


