
class DataObject {

    constructor() {
        this.isTesting = false
        this.mandatoryColumns = ["keys", "spool", "uid", "count", "price"];
        this.NILL = "NILL"
        this.spools = []
        this.health = []
        this.columns = {}
        this.storeId = this.NILL
        this.machineId = this.NILL
        this.errors = {}
        this.health = []
        this.storeId_health = "ok"
        this.machineId_health = "ok"
        this.idReg_oneLetter_oneNumber = /^[A-Za-z][0-9]$/;
    }
    getSpools() {
        let LoH = []
        this.spools.forEach((row, i) => {
            if (i === 0) {
                // Skip it! This is just the 
            }
            let mandatory = {}
            let optional = {}
            for (let k in this.columns) {
                const index = this.columns[k]
                const v = row[index]
                if (this.mandatoryColumns.includes(k)) {
                    mandatory[k] = v
                } else {

                    if (k.toLowerCase() === "harvest") {

                        // const pretty_date = this.getDate_fromExcelSerialDate(v)
                        // optional[k] = pretty_date
                        optional[k] = v

                    } else {
                        optional[k] = v

                    }


                }
            }
            LoH.push({ mandatory, optional })
        })
        return LoH
    }
    addSpool(row) {
        // spool = row 
        this.spools.push(row)
    }
    setMachine(machineId) {
        if (machineId !== undefined) { // && machineId.length > 0 ) {         
            this.machineId = machineId
        }
    }
    setStore(storeId) {
        if (storeId !== undefined && storeId.length > 0) {
            this.storeId = storeId
        }
    }
    setKeys(columns) {
        columns.forEach((c, i) => {
            const k = c.trim().toLowerCase()
            this.columns[k] = i
        })
    }
    addInfo(row) {

        try {
            const candidate = row[0].trim().toLowerCase()
            if (candidate === "spool") {
                this.addSpool(row)
            }

            if (candidate === "machine") {
                this.setMachine(row[1])
            }

            if (candidate === "store") {
                this.setStore(row[1])
            }
            if (candidate === "keys") {
                this.setKeys(row)
            }
        } catch (rowIsIllFormed) {
            const msg = rowIsIllFormed.message
            if (msg.includes("Cannot read properties of undefined")) {
                // ignore it
            } else {
                if (this.isTesting === false) {
                    console.log(rowIsIllFormed.message + "   |" + row + "|")
                }
            }
        }
    }

    _checkTheShape() {
        // Did we get a store id? 
        if (this.storeId !== this.NILL && this.storeId.length > 0) {
        } else {
            this.errors["storeId"] = "is missing"
            this.storeId_health = this.NILL
        }
        // Did we get a machine id? 
        if (this.machineId !== this.NILL) { // } && this.machineId.length > 0 ) {
        } else {
            this.errors["machineId"] = "is missing"
            this.machineId_health = this.NILL
        }
        // Did we get the minimum of the proper keys? 
        this.mandatoryColumns.forEach((col) => {
            if (!this.columns.hasOwnProperty(col)) {
                this.errors[col] = "is missing"
            }
        })
        // Do all the spools have the minimum of the proper values AND is the spool ID reasonible? 
        let isFine = true
        let dataErrors = {}
        const spoolIds_dupeCheck = {}

        this.spools.forEach((spool, j) => {
            this.health.push([])
            Object.keys(this.columns).forEach((x, index) => {
                this.health[j][index] = "ok"
            })

            const spoolId_index = this.columns["spool"]
            const price_index = this.columns["price"]
            const count_index = this.columns["count"]
            const uid_index = this.columns["uid"]
            // Dates like 01/01/23 are converted into a seriel date like '44937'. 
            // getDate_fromExcelSerialDate will convert 44937 back to human friendly date 
            const harvest_index = this.columns["harvest"]
            const pretty_date = this.getDate_fromExcelSerialDate(spool[harvest_index])
            spool[harvest_index] = pretty_date
            const spoolId = spool[spoolId_index]
            const price = spool[price_index]
            const count = spool[count_index]
            const uid = spool[uid_index]


            // spools - See if missing OR if duplicated
            if (spoolId !== undefined && this.idReg_oneLetter_oneNumber.test(spoolId)) {
                // spoolId is well shaped! Something like 'B5' 
                if (!spoolIds_dupeCheck.hasOwnProperty(spoolId)) {
                    spoolIds_dupeCheck[spoolId] = 1
                } else {
                    spoolIds_dupeCheck[spoolId] += 1
                    dataErrors["spool duplicate " + spoolId] = spoolIds_dupeCheck[spoolId]
                    this.health[j][spoolId_index] = "dupe"
                }
            } else {
                dataErrors["spool id error"] = this.NILL
                this.health[j][spoolId_index] = this.NILL
            }
            // prices - See if missing OR if not a whole number
            if (price !== undefined) {
                const num = Number.parseInt(price);
                if (Number.isInteger(num) === true) {
                    // GOOD!
                } else {
                    dataErrors["price" + price] = "Price " + price + " is not a number"
                    this.health[j][price_index] = "NaN"
                }
            } else {
                this.health[j][price_index] = this.NILL
                dataErrors["price"] = "A price is missing"
            }
            // count - See if missing OR if not a whole number
            if (count !== undefined) {
                const num = Number.parseInt(count);
                if (Number.isInteger(num) === true) {
                    // GOOD!
                } else {
                    dataErrors["count" + count] = "Count '" + count + "' is not a number"
                    this.health[j][this.columns["count"]] = "NaN"
                }
            } else {
                dataErrors["count"] = "A count is missing"
                this.health[j][count_index] = this.NILL
            }
            // uid - See if missing or empty
            if (uid !== undefined) {
                // GOOD!
            } else {
                dataErrors["uid"] = "A uid is missing"
                this.health[j][uid_index] = this.NILL
            }
        });

        for (let k in dataErrors) {
            this.errors[k] = dataErrors[k]
        }
        return this.errors
    }

    checkTheShape() {
        const theErrors = this._checkTheShape()
        const n = Object.keys(theErrors).length
        const result = {
            isOk: n === 0 ? true : false,
            errors: theErrors
        }
        return result
    }

    getDate_fromExcelSerialDate(serialDate) {
        // Dates like 01/01/23 are converted into a seriel date like '44937'. 
        // getDate_fromExcelSerialDate will convert 44937 back to human friendly date 
        function isValidDate(d) {
            return d instanceof Date && !isNaN(d);
        }
        function zeroPad(n) {
            return n.toString().padStart(2, '0');
        }

        function formatDate(date) {
            const month = zeroPad(date.getMonth() + 1);
            const day = zeroPad(date.getDate());
            const year = zeroPad(date.getFullYear() % 100);
            return `${month}/${day}/${year}`;
        }

        const unixTimestamp = (serialDate - 25569) * 86400000;
        const d = new Date(unixTimestamp);
        if (isValidDate(d)) {
            let prettyDate = formatDate(d)
            return prettyDate
        } else {
            return d // it will say 'Invalid date'
        }
    }

}
try {
    module.exports = DataObject
} catch (ignore) {
    // This is here for TDD from the CLI. In a browser this would throw an error!
    // Ignore it! 
}
