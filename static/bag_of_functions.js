const DATA_NO_OPINION = "no_opinion"
const DATA_IS_GOOD = "is_good"
const DATA_IS_BAD = "is_bad"
const possibleCommands = ["machine", "store", "spool", "keys"];
const mandatoryColumns = ["spool", "uid", "count", "price"];
let dataObject = null;
const NILL = "NILL"

//// commmon funcs 
function log_info(msg) {
    console.log("%c" + msg, "background:lightgreen;")
}

function log_blue(msg) {
    console.log("%c .... |" + msg + "|", "background:lightblue;")
}

function log_obj(obj) {
    console.log(JSON.stringify(obj, null, 2))
}


////// Show the human if the data is well shaped or not 
const colorDiv = document.getElementById('isItWellFormed');

function indicateHowWellFormed(shapeOfTheData) {

    switch (shapeOfTheData["isOk"]) {
        case true:
            if (colorDiv.classList.contains(DATA_NO_OPINION)) {
                colorDiv.classList.remove(DATA_NO_OPINION);
                colorDiv.classList.add(DATA_IS_GOOD);
                colorDiv.innerHTML = DATA_IS_GOOD
            } else if (colorDiv.classList.contains(DATA_IS_BAD)) {
                colorDiv.classList.remove(DATA_IS_BAD);
                colorDiv.classList.add(DATA_IS_GOOD);
                colorDiv.innerHTML = DATA_IS_GOOD
            }
            break;
        case false:
            let issues = "<table border='1'>"
            for ( let k in shapeOfTheData["errors"]) { 
                const v = shapeOfTheData["errors"][k]
                issues += `<tr><td>${k}</td><td>${v}</td></tr>`
            }
            issues += "</table>"
            if (colorDiv.classList.contains(DATA_NO_OPINION)) {
                colorDiv.classList.remove(DATA_NO_OPINION);
                colorDiv.classList.add(DATA_IS_BAD);
            } else if (colorDiv.classList.contains(DATA_IS_GOOD)) {
                colorDiv.classList.remove(DATA_IS_GOOD);
                colorDiv.classList.add(DATA_IS_BAD);
            }
            colorDiv.innerHTML = issues

            break;
        default:
            if (colorDiv.classList.contains(DATA_IS_GOOD)) {
                colorDiv.classList.remove(DATA_IS_GOOD);
                colorDiv.classList.add(DATA_NO_OPINION);
                colorDiv.innerHTML = ""
            } else if (colorDiv.classList.contains(DATA_IS_BAD)) {
                colorDiv.classList.remove(DATA_IS_BAD);
                colorDiv.classList.add(DATA_NO_OPINION);
                colorDiv.innerHTML = ""
            }
            break;
    }
}
function makeTable(dataObject) {
    let table = "<table border='1' id='machineTable'>"
    table += `<tr><th>storeId</th><td>${dataObject.storeId}</td></tr>`
    table += `<tr><th>machineId</th><td>${dataObject.machineId}</td></tr>`
    table += "<tbody><tr>"
    for ( let k in dataObject['columns']) { 
        const v = dataObject['columns'][k]
        table += `<th>${k}</th>`
    }
    table += "</tr>"
    dataObject.spools.forEach((spool)=> { 
        table += "<tr>"
        spool.forEach((thing)=> { 
            table += `<td>${thing}</td>`
        })
        table += "</tr>"
    })


    table += "</tbody></table>"
    return table 


}

function createDataObject(rows) {
    dataObject = new DataObject() 
    log_info( dataObject )
    log_blue("well? ")
    rows.forEach((row, i) => {
        if (row.length > 0) {
            dataObject.addInfo(row)
        }
    })
    const isTheDataAllOk = dataObject.checkTheShape()
    // log_info( JSON.stringify( dataObject ) )
    indicateHowWellFormed(isTheDataAllOk)
    const theTable = makeTable(dataObject)
    document.getElementById("machineTable").innerHTML = theTable
}


function fileUpload(event) {
    function isValidCommand(candidate) {
        return possibleCommands.includes(candidate);
    }

    // function createTable(data, storeId, machineId, columns) { 
    //     let table = "<table border='1' class='machineTable'><tr>"

    //     table += "<tr><th>Store</th><th>" + storeId + "</th><tr>"
    //     table += "<tr><th>MachineId</th><th>" + machineId + "</th><tr>"
    //     table += "<tbody>"


    //     table += "</tbody>"
    //     table += "</table>"


    //     // Object.keys(columns).forEach((c, i)=> {
    //     //     table += "<th>" + c + "</th>"
    //     // })
    //     // table += "</tr>"
    //     // data.forEach((row, i)=> {
    //     //     table += "<tr>"
    //     //     row.forEach((column)=> { 
    //     //         table += "<td>" + column + "</td>"
    //     //     })
    //     //     table += "</tr>"
    //     // })
    //     // table += "</table>"
    //     document.getElementById("machineTable").innerHTML = table 

    // }


    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = (event) => {
        const fileData = event.target.result;
        const workbook = XLSX.read(fileData, {
            type: 'binary'
        });
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const rows = XLSX.utils.sheet_to_json(worksheet, {
            header: 1
        });
        createDataObject(rows ) // Broken out to make testing easy 
    };
    reader.readAsBinaryString(file);
};
