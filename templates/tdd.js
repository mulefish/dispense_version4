
const inventory = [{"brand":"Kellog","cbd_percent":0.09,"count":10,"description":"Indoor/outdoor terpenes","farm":"Noble","harvest":"10/22/19","itemId":8,"name":"Peanut","price":12,"product":"flower","strain":"Peanut Butter Pie","thc_percent":27.3,"type":"Indica","weight_in_grams":1.09},{"brand":"Kellog","cbd_percent":0.1,"count":10,"description":"Indoor/outdoor terpenes","farm":"HighWinds","harvest":"11/05/19","itemId":9,"name":"Sunset","price":11,"product":"flower","strain":"Sunset Sherbert","thc_percent":28.4,"type":"Hybrid","weight_in_grams":1.01},{"brand":"Kellog","cbd_percent":0.07,"count":10,"description":"Indoor/outdoor terpenes","farm":"Heros of the Farm","harvest":"11/14/19","itemId":10,"name":"Headdog","price":8,"product":"flower","strain":"Headdog","thc_percent":26.64,"type":"Hybrid","weight_in_grams":1.04},{"brand":"Indica_5","cbd_percent":30.49,"description":"Relaxed,Euphoric,Sleepy,Hungry,Happy","harvest":"21/05/20","itemId":15,"name":"Estraweeda","number_of_joints":5,"price":46.92,"product":"prerolls","stock":5,"store":1,"strain":"Estraweeda","thc_percent":20.11,"type":"Indica"},{"brand":"Hybrid_15","cbd_percent":32.86,"description":"Happy,Relaxed,Uplifted,Euphoric,Sleepy","harvest":"23/11/20","itemId":16,"name":"Estraweeda","number_of_joints":15,"price":17.92,"product":"prerolls","stock":9,"store":2,"strain":"Estraweeda","thc_percent":10.08,"type":"Hybrid"},{"brand":"Hybrid_5","cbd_percent":20.45,"description":"Relaxed,Creative,Uplifted,Euphoric,Hungry","harvest":"15/05/20","itemId":17,"name":"Red Flight","number_of_joints":5,"price":29.77,"product":"prerolls","stock":9,"store":2,"strain":"Red Flight","thc_percent":38.64,"type":"Hybrid"},{"brand":"Hybrid_5","cbd_percent":16.01,"description":"Relaxed,Creative,Uplifted,Euphoric,Hungry","harvest":"02/02/19","itemId":18,"name":"Estraweeda","number_of_joints":5,"price":47.35,"product":"prerolls","stock":9,"store":1,"strain":"Estraweeda","thc_percent":38.66,"type":"Hybrid"},{"brand":"Hybrid_15","cbd_percent":36.29,"description":"Relaxed,Creative,Uplifted,Euphoric,Hungry","harvest":"23/04/20","itemId":19,"name":"Estraweeda","number_of_joints":15,"price":23.84,"product":"prerolls","stock":9,"store":1,"strain":"Estraweeda","thc_percent":13.8,"type":"Hybrid"},{"brand":"Indica_10","cbd_percent":39.87,"description":"Relaxed,Sleepy,Euphoric,Happy,Uplifted","harvest":"15/04/20","itemId":20,"name":"Silky","number_of_joints":10,"price":19.93,"product":"prerolls","stock":10,"store":4,"strain":"Silky","thc_percent":19.99,"type":"Indica"},{"brand":"Indica_10","cbd_percent":28.85,"description":"Relaxed,Euphoric,Sleepy,Hungry,Happy","harvest":"17/01/21","itemId":21,"name":"Silky","number_of_joints":10,"price":33.63,"product":"prerolls","stock":10,"store":1,"strain":"Silky","thc_percent":23.32,"type":"Indica"},{"brand":"Sativa_15","cbd_percent":26.13,"description":"Euphoric,Uplifted,Relaxed,Talkative,Happy","harvest":"27/09/21","itemId":22,"name":"Red Flight","number_of_joints":15,"price":37.73,"product":"prerolls","stock":10,"store":4,"strain":"Red Flight","thc_percent":11.79,"type":"Sativa"},{"brand":"Indica_15","cbd_percent":24.8,"description":"Happy,Relaxed,Sleepy,Euphoric,Creative","harvest":"21/09/21","itemId":23,"name":"Silky","number_of_joints":15,"price":49.36,"product":"prerolls","stock":10,"store":4,"strain":"Silky","thc_percent":26.22,"type":"Indica"}]

function makeInventoryTable() { 
    function getType(candidate) {
        let t = typeof candidate
        if ( t === "string") {
            if ( candidate.length === 8 && candidate.includes("/")) {
                t = "date"
            } 
        }  
        return t
    }

    const special = new Set(["brand", "name", "itemId"])
    let table = "<table border='1'>"
    inventory.forEach((row, i ) => { 
        const brand = row["brand"]
        const name = row["name"]
        const itemId = row["itemId"]

        let tr = `<tr><td>${itemId}<td>${brand}</td><td>${name}<td>`

        for ( let k in row ) {
            if ( ! special.has(k)) {
                const v = row[k]
                const clazz = getType(v)
               
                tr += `<td class='${clazz}'>${v}</td>`                
            }
        }
        tr += "</tr>"
        table += tr 
    })
    return table += "</table>"
} 

const result = makeInventoryTable() 
console.log( result )