const DATA_NO_OPINION = "no_opinion"
const DATA_IS_GOOD = "is_good"
const DATA_IS_BAD = "is_bad"
const possibleCommands = ["machine", "store", "spool", "keys"];
const mandatoryColumns = ["spool", "uid", "count", "price"];
let dataObject = null;
const NILL = "NILL"
class DataObject { 

    constructor() { 
        this.spools = [] 
        this.columns = {} 
        this.storeId = NILL
        this.machineId = NILL 
        this.errors = {

        }
        
    }

    addSpool(row) {
        this.spools.push(row)
    }
    setMachine(machineId) {
        if ( machineId !== undefined && machineId.length > 0 ) { 
            this.machineId = machineId
        }

    }
    setStore(storeId) {
        if ( storeId !== undefined && storeId.length > 0 ) { 
            this.storeId = storeId
        }
    }
    setKeys(columns) {
        columns.forEach((c, i)=>{
            const k = c.trim().toLowerCase()
            this.columns[k] = i
        })
    }
    addInfo(row) {
        const candidate = row[0].trim().toLowerCase()
        if ( candidate === "spool") {
            this.addSpool(row)
        }

        if ( candidate === "machine") {
            this.setMachine(row[1])
        }

        if ( candidate === "store") {
            this.setStore(row[1])
        }
        if ( candidate === "keys") {
            this.setKeys(row)
        }
    }

    _checkTheShape() { 
        // Did we get a store id? 
        if ( this.storeId !== NILL && this.storeId.length > 0 ) {
        } else {
            this.errors["storeId"] = "is missing"
        }
        // Did we get a machine id? 
        if ( this.machineId !== NILL && this.machineId.length > 0 ) {
        } else {
            this.errors["machineId"] = "is missing"
        }
        // Did we get the minimum of the proper keys? 
        mandatoryColumns.forEach((col) => { 
            if ( ! this.columns.hasOwnProperty(col)) {
                this.errors[col] = "is missing"
            }
        })
        // Do all the spools have the minimum of the proper values AND is the spool ID reasonible? 
        let isFine = true 
        let dataErrors = {} 
        const idReg_oneLetter_oneNumber = /^[A-Za-z][0-9]$/;
        const spoolIds_dupeCheck = {} 
        this.spools.forEach((spool)=> {     
            const spoolId = spool[this.columns["spool"]]
            const price = spool[this.columns["price"]]
            const count = spool[this.columns["count"]]
            const uid = spool[this.columns["uid"]]
            // spools - See if missing OR if duplicated
            if ( spoolId !== undefined && idReg_oneLetter_oneNumber.test(spoolId)) {
                // spoolId is well shaped! Something like 'B5' 
                if ( ! spoolIds_dupeCheck.hasOwnProperty(spoolId)) {
                    spoolIds_dupeCheck[spoolId] = 1
                } else {
                    spoolIds_dupeCheck[spoolId] += 1
                    dataErrors["spool duplicate " + spoolId] = spoolIds_dupeCheck[spoolId]
                }
            } else {
                dataErrors["spool id error"] = NILL
            }
            // prices - See if missing OR if not a whole number
            if ( price !== undefined ) {
                const num = Number.parseInt(price);
                if ( Number.isInteger(num) === true ) { 
                    // GOOD!
                } else {
                    dataErrors["price" + price] = "Price " + price + " is not a number"
                }
            } else {
                dataErrors["price"] = "A price is missing"
            }
            // count - See if missing OR if not a whole number
            if ( count !== undefined ) {
                const num = Number.parseInt(count);
                if ( Number.isInteger(num) === true ) { 
                    // GOOD!
                } else {
                    dataErrors["count" + count] = "Count '" + count + "' is not a number"
                }
            } else {
                dataErrors["count"] = "A count is missing"
            }
            // uid - See if missing or empty
            if ( uid !== undefined ) {
                // GOOD!
            } else {
                dataErrors["uid"] = "A uid " + uid + " is missing"
            }
        });

        for ( let k in dataErrors) { 
            this.errors[k] = dataErrors[k]
        }
        return this.errors
    }

    checkTheShape() { 
        const theErrors = this._checkTheShape()
        const n = Object.keys(theErrors).length 
        const result = {
            isOk : n === 0 ? true : false,
            errors:theErrors
        }
        return result
    }

}

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

function createDataObject(rows) {
    dataObject = new DataObject() 
    rows.forEach((row, i) => {
        if (row.length > 0) {
            dataObject.addInfo(row)
        }
    })
    const result = dataObject.checkTheShape()
    log_obj(result)
}


function fileUpload(event) {
    function isValidCommand(candidate) {
        return possibleCommands.includes(candidate);
    }

    function createTable(data, storeId, machineId, columns) { 
        // log_obj(data)
        // log_info( "storeIdTuple " + JSON.stringify( storeIdTuple ))
        // log_info( "machine " + JSON.stringify( machine ))
        // log_info( "columns " + JSON.stringify( columns ))

        let table = "<table border='1' class='machineTable'><tr>"

        table += "<tr><th>Store</th><th>" + storeId + "</th><tr>"
        table += "<tr><th>MachineId</th><th>" + machineId + "</th><tr>"


        Object.keys(columns).forEach((c, i)=> {
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
        createDataObject(rows ) // Broken out to make testing easy 
    };
    reader.readAsBinaryString(file);
};
