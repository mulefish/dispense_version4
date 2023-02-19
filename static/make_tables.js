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

    const lookup = {'itemId':'id','price':'$','instock':'in','deployed':'out','brand':'brand','cbd':'cbd %','desc':'description','farm':'farm','harvest':'harvest','name':'name','product':'product','strain':'strain','thc':'thc%','type':'type','Wt_Num':'wt or #', "deploy":"deploy"}
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
                tr += `<td><button onClick="makeThisRowActive(${row['itemId']}, ${i})">Select item ${row['itemId']} </button></td>`      
            } else {
                const v = row[k]
                const clazz = getType(v)   
                tr += `<td class='${clazz}'>${v}</td>`                    
            }
        })
        tr += "</tr>"
        table += tr 
    })
    table += "</table>"
    document.getElementById(domNodeToPopulate).innerHTML = table

} 

function makeThisRowActive(itemId, i) { 


    var table = document.getElementById('inventoryTable');
    var cells = table.getElementsByTagName('td');

    for (var i = 0; i < cells.length; i++) {
        // Take each cell
        var cell = cells[i];
        // do something on onclick event for cell
        cell.onclick = function () {
            // Get the row id where the cell exists
            var rowId = this.parentNode.rowIndex;

            var rowsNotSelected = table.getElementsByTagName('tr');
            for (var row = 0; row < rowsNotSelected.length; row++) {
                rowsNotSelected[row].style.backgroundColor = "";
                rowsNotSelected[row].classList.remove('selected');
            }
            var rowSelected = table.getElementsByTagName('tr')[rowId];
            rowSelected.style.backgroundColor = "yellow";
            rowSelected.className += " selected";

            msg = 'The ID of the company is: ' + rowSelected.cells[0].innerHTML;
            msg += '\nThe cell value is: ' + this.innerHTML;
            console.log(msg);
        }
    }
    
}