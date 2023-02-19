

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