function makeInventoryTable(inventory, domNodeToPopulate) { 
    function getType(candidate) {
        let t = typeof candidate
        if ( t === "string") {
            if ( candidate.length === 8 && candidate.includes("/")) {
                t = "date"
            } 
        }  
        return t
    }

    // const special = new Set(["brand", "name", "itemId"])
    let table = "<table border='1'><tr>"
    const keys = ['itemId','price','instock','deployed','brand','cbd','desc','farm','harvest','name','product','strain','thc','type','Wt_Num']
    let headers = "<tr>"
    keys.forEach((k)=>{
        headers += "<th>" + k + "</th>"
    })
    headers += "</tr>"
    table += headers




    inventory.forEach((row, i ) => { 
        // const brand = row["brand"]
        // const name = row["name"]
        // const itemId = row["itemId"]
console.log(row)
        // let tr = `<tr><td class='needed'>${itemId}<td class='needed'>${brand}</td><td class='needed'>${name}<td>`
        let tr = "<tr>"
        keys.forEach((k)=>{
            const v = row[k]
            const clazz = getType(v)   
            tr += `<td class='${clazz}'>${v}</td>`                
        })
        tr += "</tr>"
        table += tr 
    })
    table += "</table>"
    document.getElementById(domNodeToPopulate).innerHTML = table

} 