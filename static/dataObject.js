class DataObject { 

    constructor() { 
        this.spools = [] 
        this.health = [] 
        this.columns = {} 
        this.storeId = NILL
        this.machineId = NILL 
        this.errors = {

        }
        this.health = [] 
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
        this.spools.forEach((spool, j)=> {     
            this.health.push([])
             Object.keys(this.columns).forEach((x, index)=> { 
                this.health[j][index] = "ok"
            })

            const spoolId_index = this.columns["spool"]
            const price_index = this.columns["price"]
            const count_index= this.columns["count"]
            const uid_index = this.columns["uid"]

            const spoolId = spool[spoolId_index]
            const price = spool[price_index]
            const count = spool[count_index]
            const uid = spool[uid_index]


            // spools - See if missing OR if duplicated
            if ( spoolId !== undefined && idReg_oneLetter_oneNumber.test(spoolId)) {
                // spoolId is well shaped! Something like 'B5' 
                if ( ! spoolIds_dupeCheck.hasOwnProperty(spoolId)) {
                    spoolIds_dupeCheck[spoolId] = 1
                } else {
                    spoolIds_dupeCheck[spoolId] += 1
                    dataErrors["spool duplicate " + spoolId] = spoolIds_dupeCheck[spoolId]
                    this.health[j][spoolId_index] = "dupe"
                }
            } else {
                dataErrors["spool id error"] = NILL
                this.health[j][spoolId_index] = NILL
            }
            // prices - See if missing OR if not a whole number
            if ( price !== undefined ) {
                const num = Number.parseInt(price);
                if ( Number.isInteger(num) === true ) { 
                    // GOOD!
                } else {
                    dataErrors["price" + price] = "Price " + price + " is not a number"
                    this.health[j][price_index] = "NaN"
                }
            } else {
                this.health[j][price_index] = NILL
                dataErrors["price"] = "A price is missing"
            }
            // count - See if missing OR if not a whole number
            if ( count !== undefined ) {
                const num = Number.parseInt(count);
                if ( Number.isInteger(num) === true ) { 
                    // GOOD!
                } else {
                    dataErrors["count" + count] = "Count '" + count + "' is not a number"
                    this.health[j][this.columns["count"]] = "NaN"
                }
            } else {
                dataErrors["count"] = "A count is missing"
                this.health[j][count_index] = NILL
            }
            // uid - See if missing or empty
            if ( uid !== undefined ) {
                // GOOD!
            } else {
                dataErrors["uid"] = "A uid is missing"
                this.health[j][uid_index] = NILL
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
