const DATA_NO_OPINION = "no_opinion"
const DATA_IS_GOOD = "is_good"
const DATA_IS_BAD = "is_bad"
const HIDE_ME = "hideMe"
const SHOW_ME = "showMe"
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
const saveButton = document.getElementById('saveButton')

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

            if ( saveButton.classList.contains(HIDE_ME)) {
                saveButton.classList.remove(HIDE_ME)
                saveButton.classList.add(SHOW_ME)
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

            if ( saveButton.classList.contains(SHOW_ME)) {
                saveButton.classList.remove(SHOW_ME)
                saveButton.classList.add(HIDE_ME)
            }



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
            if ( saveButton.classList.contains(SHOW_ME)) {
                saveButton.classList.remove(SHOW_ME)
                saveButton.classList.add(HIDE_ME)
            }
            break;
    }
}
function makeTable(dataObject) {
    log_blue("makeTable for "  + dataObject.storeId + " machine " + dataObject.machineId)
    let table = "<table border='1' class='machineTable'>"
    if ( dataObject['storeId_health'] === "ok") {
        table += `<tr><th>storeId</th><td>${dataObject.storeId}</td></tr>`
    } else {
        table += `<tr><th>storeId</th><td class='is_bad'>${dataObject.storeId}</td></tr>`
    }

    if ( dataObject['machineId_health'] === "ok") {
        table += `<tr><th>machineId</th><td>${dataObject.machineId}</td></tr>`
    } else {
        table += `<tr><th>machineId</th><td class='is_bad'>${dataObject.machineId}</td></tr>`
    }
    table += "<tbody><tr>"
    for ( let k in dataObject['columns']) { 
        const v = dataObject['columns'][k]
        table += `<th>${k}</th>`
    }
    table += "</tr>"
    dataObject.spools.forEach((spool, i )=> { 
        table += "<tr>"
        for ( let k in dataObject['columns']) { 
            const index = dataObject['columns'][k]
            const value = spool[index]
            if ( dataObject.health[i][index] === "ok") {
                table += `<td>${value}</td>`
            } else {
                table += `<td class='is_bad'>${value}  ${dataObject.health[i][index]}</td>`
            }
        }
        table += "</tr>"
    })
    table += "</tbody></table>"
    return table 
}

function createDataObject(rows) {
    dataObject = new DataObject() 
    rows.forEach((row, i) => {
        if (row.length > 0) {
            dataObject.addInfo(row)
        }
    })
    const isTheDataAllOk = dataObject.checkTheShape()
    indicateHowWellFormed(isTheDataAllOk)
    const theTable = makeTable(dataObject)
    document.getElementById("machineTable").innerHTML = theTable
}


function fileUpload(event) {
    function isValidCommand(candidate) {
        return possibleCommands.includes(candidate);
    }

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
