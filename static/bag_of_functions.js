const DATA_NO_OPINION = "no_opinion"
const DATA_IS_GOOD = "is_good"
const DATA_IS_BAD = "is_bad"
const possibleCommands = ["machine", "store", "spool", "keys"];

//// commmon funcs 
function log_info(msg) {
    console.log("%c" + msg, "background:lightgreen;")
}

function log_error(msg) {
    console.log("%c" + msg, "background:lightred;")
}

function log_obj(obj) {
    console.log(JSON.stringify(obj, null, 2))
}


////// Show the human if the data is well shaped or not 
const colorDiv = document.getElementById('isItWellFormed');

function indicateIsWellFormed(isOk_orIsNothing_orIsBad, issues) {
    switch (isOk_orIsNothing_orIsBad) {
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
            if (colorDiv.classList.contains(DATA_NO_OPINION)) {
                colorDiv.classList.remove(DATA_NO_OPINION);
                colorDiv.classList.add(DATA_IS_BAD);
                colorDiv.innerHTML = issues
            } else if (colorDiv.classList.contains(DATA_IS_GOOD)) {
                colorDiv.classList.remove(DATA_IS_GOOD);
                colorDiv.classList.add(DATA_IS_BAD);
                colorDiv.innerHTML = issues
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
            break;
    }
}
///// Most important func /////////////////
function fileUpload(event) {
    function isValidCommand(candidate) {
        return possibleCommands.includes(candidate);
    }

    function createTable(data, storeId, machineId, columns) { 
        log_obj(data)
        log_info( "storeId " + JSON.stringify( storeId ))
        log_info( "machineId " + JSON.stringify( machineId ))
        log_info( "columns " + JSON.stringify( columns ))

        let table = "<table border='1' class='machineTable'><tr>"
        columns.forEach((c, i)=> {
            table += "<th>" + c + "</th>"
        })
        table += "</tr>"
        data.forEach((row, i)=> {
            table += "<tr>"
            row.forEach((column)=> { 
                table += "<td>" + column + "</td>"
            })
            table += "</tr>"
        })
        table += "</table>"
        document.getElementById("machineTable").innerHTML = table 




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
        const data = []
        const seen = {}
        let storeId = []
        let machineId = []
        let columns = []
        rows.forEach((row, i) => {
            if (row.length > 0) {
                const candidate = row[0].trim().toLowerCase()
                if (isValidCommand(candidate)) {
                    seen[candidate] = 1
                    if ( candidate === "store") {
                        storeId = row
                    } else if ( candidate === "keys") {
                        columns = row
                    } else if ( candidate === "machine") { 
                        machine = row
                    } else if ( candidate === "spool") {
                        data.push(row)
                    }
                }
            }
        })

        let issues = ""
        let isOk = true
        possibleCommands.forEach((cmd) => {
            if (!seen.hasOwnProperty(cmd)) {
                issues += cmd + ","
                isOk = false
            }
        })
        if ( isOk === false ) { 
            // snip the trailing comma
            issues = issues.substring(0, issues.length - 1)
            indicateIsWellFormed(isOk, "Missing " + issues)
        } else {
            createTable(data, storeId, machineId, columns)
            indicateIsWellFormed(isOk)
        }




    };
    reader.readAsBinaryString(file);
};

