const DataObject = require('./dataObject.js');
const Reset = "\x1b[0m"
const BgRed = "\x1b[41m"
const BgGreen = "\x1b[42m"

function verify(a, b, msg) {
    if (JSON.stringify(a) === JSON.stringify(b)) {
        console.log(`${BgGreen}PASS:${Reset} ${msg}`)
    } else {
        console.log(`${BgRed}FAIL:${Reset} ${msg}`)
    }
}

function dataObject_populateProperty_HAPPYPATH() {
    const dataObject = new DataObject() 
    const excel = [
        // See? Some slop is OK -  undefined to out of place things will be ignored
        ["store", "Test", undefined, undefined, "ignore"],
        ["machine", "888"], // The last machine will be picked up  
        ["machine", "999"],
        ['keys', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD'],
        ['This is not a key', 'blah blah'],
        ['SPOOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()
    verify(shape["isOk"], true, "dataObject_populateProperty_HAPPYPATH")
}

function dataObject_populateProperty_SADPATH_missingStuff() {
    dataObject = new DataObject() 
    dataObject.isTesting = true // suppress annoying console.log
    const excel = [
        ['This is not a key', 'blah blah'],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })

    const shape = dataObject.checkTheShape()
    const errors = Object.keys(shape['errors'])
    const expectedValues = ["storeId","machineId","spool","uid","count","price"]
    const isOk = expectedValues.every(val => errors.includes(val));
    verify(isOk, true, "dataObject_populateProperty_SADPATH_missingStore_and_machine")
}


function dataObject_populateProperty_serialDateConvertAndCheck() {
    const dataObject = new DataObject() 
    const good = "" + dataObject.getDate_fromExcelSerialDate(44932) // This is a 'serial date'
    const bad = "" + dataObject.getDate_fromExcelSerialDate("Kittycat") // This is not a 'serial date'
    const isOk = good === "01/05/23" && bad === "Invalid Date"

    verify(isOk, true, "dataObject_populateProperty_serialDateConvertAndCheck")
}

function dataObject_populateProperty_SADPATH_DUPLICATED_spoolIds() {
    const dataObject = new DataObject() 
    const excel = [
        // See? Some slop is OK -  undefined to out of place things will be ignored
        // See? Capitalization does not matter
        ["storE", "Test", undefined, undefined, "ignore"],
        ["machIne", "888"], // The last machine will be picked up  
        ["macHine", "999"],
        ['keyS', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD'],
        ['This is not a key', 'blah blah'],
        ['SPoOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
        ['SPOOL', 'A2', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
        ['SPOOL', 'A3', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
        ['SPOOl', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()
    const isOk = shape["errors"]["spool duplicate A1"] === 2
    verify(isOk, true, "dataObject_populateProperty_SADPATH_DUPLICATED_spoolIds " )
}

function dataObject_populateProperty_SADPATH_missingMandatoryFields() {
    const dataObject = new DataObject() 
    const excel = [
        // See? Some slop is OK -  undefined to out of place things will be ignored
        ["store", "Test"],
        ["machine", "999"],
        ['keys', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD'],
        ['SPOOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
        ['SPOOL']
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()
    const errors = Object.keys(shape["errors"])
    const expectedValues = ["spool id error", "price","count","uid"]
    const isOk = expectedValues.every(val => errors.includes(val));
    verify(isOk, true, "dataObject_populateProperty_SADPATH_missingMandatoryFields")
}

function dataObject_populateProperty_SADPATH_missingAMandatoryColumns() {
    const dataObject = new DataObject() 

    const excel = [
        ["store",	"Kitty Buds"],										
        ["machine",	1],										
        ["keys","Type","grams","Producer","Strain","Classification","BatchInfo","Harvest","Canabinoids","THC-A","Delta_9","CBD"]
        ["SPOOL","Flower","3.5","Paddle Creek Cannabis","Green Arrow","Sativa","KLT - 68511530","dinoblank",21,4,9,5]
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()
    const errors = Object.keys(shape['errors'])
    const expectedValues = ["spool","uid","count","price"]
    const isOk = expectedValues.every(val => errors.includes(val));

    verify(isOk, true, "dataObject_populateProperty_SADPATH_missingAMandatoryColumns")
} 

function dataObject_populateProperty_SADPATH_notLeftJustified() {
    const dataObject = new DataObject() 
    const excel = [
        ["store", "Test"],
        ["", "machine", "999"], // See? Leading empty element
        ['keys', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD'],
        ['SPOOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()

    const errors = Object.keys(shape['errors'])
    const expectedValues = ["machineId"]
    const isOk = expectedValues.every(val => errors.includes(val));

    verify(isOk, true, "dataObject_populateProperty_SADPATH_notLeftJustified")
}


if (require.main === module) {
    dataObject_populateProperty_HAPPYPATH()
    dataObject_populateProperty_SADPATH_missingStuff()
    dataObject_populateProperty_serialDateConvertAndCheck()
    dataObject_populateProperty_SADPATH_DUPLICATED_spoolIds()
    dataObject_populateProperty_SADPATH_missingMandatoryFields()
    dataObject_populateProperty_SADPATH_missingAMandatoryColumns()
    dataObject_populateProperty_SADPATH_notLeftJustified()
}
