


let keys = ["merchantId_fk","price","instock","deployed","brand","cbd","desc","farm","harvest","name","strain","thc","type","weight","count","product"]
// [13,42,-1,-1,"Estraweeda",-1,"Relaxed, Euphoric, Sleepy, Hungry, Happy","","21/05/20","Indica_5","Estraweeda",-1,"preroll",5,-1,"preroll"] 


let brackets = [] 

let things = ""

keys.forEach((k, i) => { 

    if ( i === 0 || i === 1 || i === 2 || i === 3 || i === 5 || i === 11 || i === 13 || i === 14 ) {
        brackets.push({})
    } else {
        brackets.push('{}')
    }
    things += k + ","


}) 
console.log( JSON.stringify( brackets ) )
console.log( things )



sql = "insert into Item2(merchantId_fk,price,instock,deployed,brand,cbd,desc,farm,harvest,name,strain,thc,type,weight,count,product) values (0,1,2,3,"4",5,"6","7","8","9","10",11,"12",13,14,"15")


sql = "insert into Item2(merchantId_fk,price,instock,deployed,brand,cbd,desc,farm,harvest,name,strain,thc,type,weight,count,product) values [{},{},{},{},"{}",{},"{}","{}","{}","{}","{}",{},"{}",{},{},"{}"]

// sql = "insert into Item(merchantId_fk, price, instock, deployed, JSON) values ({}, {},{},{}, '{}');".format(
//     merchantId_fk, price, instock, deployed, json
// )