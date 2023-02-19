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
    // const keys = ['itemId','price','instock','deployed','brand','cbd','desc','farm','harvest','name','product','strain','thc','type','Wt_Num']

    const lookup = {'itemId':'id','price':'$','instock':'in','deployed':'out','brand':'brand','cbd':'cbd %','desc':'description','farm':'farm','harvest':'harvest','name':'name','product':'product','strain':'strain','thc':'thc%','type':'type','Wt_Num':'wt or #'}
    const keys = Object.keys(lookup)
    let headers = "<tr>"
    keys.forEach((k)=>{
        headers += "<th>" + lookup[k] + "</th>"
    })
    headers += "</tr>"
    table += headers
    inventory.forEach((row, i ) => { 
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