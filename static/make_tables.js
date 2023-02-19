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
    let table = "<table border='1' id='inventoryTable'><tr>"
    // const keys = ['itemId','price','instock','deployed','brand','cbd','desc','farm','harvest','name','product','strain','thc','type','Wt_Num']

    const lookup = {'itemId':'id','price':'$','instock':'in','deployed':'out','brand':'brand','cbd':'cbd %','desc':'description','farm':'farm','harvest':'harvest','name':'name','product':'product','strain':'strain','thc':'thc%','type':'type','Wt_Num':'wt or #', "deploy":"deploy"} // , "save":"save"}
    const keys = Object.keys(lookup)
    let headers = "<tr>"
    keys.forEach((k)=>{
        headers += "<th>" + lookup[k] + "</th>"
    })
    headers += "</tr>"
    table += headers
    inventory.forEach((row, i ) => { 
        let tr = `<tr id='r_${row['itemId']}'>`
        keys.forEach((k)=>{
            if ( k === "deploy") {
                tr += `<td><button onClick="makeThisRowActive_inventoryTable(${row['itemId']}, ${i})">Select ${row['itemId']} </button></td>`      
            // } else if ( k === "save") {
            //     tr += `<td><button onClic   k="saveChanges_toProduct(${row['itemId']}, ${i})">Save ${row['itemId']} </button></td>`      
            } else {
                const v = row[k]
                // const clazz = getType(v)   
                // tr += `<td class='${clazz}'>${v}</td>`                    
                const t = getType(v) 
                if ( t === "string" || t === "date") {
                    //tr += `<td><input type='text' value='${v}' class='rc_string' ></input></td>`
                    tr += `<td>${v}</td>`
                } else { 
                    if ( k === "deployed") {
                        tr += `<td id="deployed_${row['itemId']}" class='rc_number'>${v}</td>`                
                    } else if ( k === "instock") {
                        tr += `<td id="instock_${row['itemId']}" class='rc_number'>${v}</td>`                
                    } else {
                        // tr += `<td><input type='number' min='0' value='${v}' class='rc_number'  ></input></td>`
                        tr += `<td class='rc_number'>${v}</td>`                
                    }
                }
            }
        })
        tr += "</tr>"
        table += tr 
    })
    table += "</table>"
    document.getElementById(domNodeToPopulate).innerHTML = table

} 


function saveChanges_toProduct(itemId, i) {
    alert("saveChanges_toProduct " + itemId )
}

function makeThisRowActive_inventoryTable(itemId, i) { 


    setSelectedItem(itemId)

    const table = document.getElementById('inventoryTable');
    const cells = table.getElementsByTagName('td');

    for (var i = 0; i < cells.length; i++) {
        // Take each cell
        const cell = cells[i];
        // do something on onclick event for cell
        cell.onclick = function () {
            // Get the row id where the cell exists
            const rowId = this.parentNode.rowIndex;

            const rowsNotSelected = table.getElementsByTagName('tr');
            for (let row = 0; row < rowsNotSelected.length; row++) {
                rowsNotSelected[row].style.backgroundColor = "";
                rowsNotSelected[row].classList.remove('selected');
            }
            const rowSelected = table.getElementsByTagName('tr')[rowId];
            rowSelected.style.backgroundColor = "yellow";
            rowSelected.className += " selected";

            // msg = 'The ID of the company is: ' + rowSelected.cells[0].innerHTML;
            // msg += '\nThe cell value is: ' + this.innerHTML;
            // console.log(msg);
        }
    }
}


///////////// VENDING MACHINE FOLLOWS 
