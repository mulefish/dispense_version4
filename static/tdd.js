const DataObject = require('./dataObject.js');
const Reset = "\x1b[0m"
const BgRed = "\x1b[41m"
const BgGreen = "\x1b[42m"
/**
 * Mini UnitTest
 * @param {*} a Do both a and b exactly match? Then pass! 
 * @param {*} b else fail 
 * @param {*} msg Is a msg about the test 
 */
function verify(a, b, msg) {
    if (JSON.stringify(a) === JSON.stringify(b)) {
        console.log(`${BgGreen}PASS:${Reset} ${msg}`)
    } else {
        console.log(`${BgRed}FAIL:${Reset} ${msg}`)
    }
}
/**
 * Happypath! 
 * Give it well formed data. 
 * Note that capitalization does not matter. 
 * Note that extra fields exist 
 * Note that 'This is not a key' row get ignored 
 * Note that the pointless colum 'COLUMN_NAME_THIS_DOES_NOT_MATTER' will be ignored 
 *   because 'COLUMN_NAME_THIS_DOES_NOT_MATTER' is not in the system of things to care about
 * Note that the extra field in the Spool, here with the value '"THIS WILL BE IGNORED" is ignored
 */
function dataObject_populateProperty_HAPPYPATH() {
    const dataObject = new DataObject() 
    const excel = [
        // See? Some slop is OK -  undefined to out of place things will be ignored
        ["store", "Test", undefined, undefined, "ignore"],
        ["machine", "888"], // The last machine will be picked up  
        ["machine", "999"],
        ['keys', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD', "COLUMN_NAME_THIS_DOES_NOT_MATTER"],
        ['This is not a key', 'blah blah'],
        ['SPOOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 44932, 21, 4, 9, 5, "THIS WILL BE IGNORED"],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()
    verify(shape["isOk"], true, "dataObject_populateProperty_HAPPYPATH")
}
/**
 * Needs storeId and machineId! 
 * Note: Here using the 'dataObject.isTesting = true' to 
 * suppress annoying console.log that would otherwise complain
 */
function dataObject_populateProperty_SADPATH_missingStuff() {
    dataObject = new DataObject() 
    dataObject.isTesting = true
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

/**
 * Excel converts human readable dates like '01/05/23' into 'serial dates' under the hood. 
 * Check that a serial date in re-converted into a more reasonible format
 * Note 44932 is a serial date
 * Note Kittycat is not a serial date
 */
function dataObject_populateProperty_serialDateConvertAndCheck() {
    const dataObject = new DataObject() 
    const good = "" + dataObject.getDate_fromExcelSerialDate(44932)
    const bad = "" + dataObject.getDate_fromExcelSerialDate("Kittycat")
    const isOk = good === "01/05/23" && bad === "Invalid Date"

    verify(isOk, true, "dataObject_populateProperty_serialDateConvertAndCheck")
}
/**
 * Spoolids NEED to be unique! A1 is duplicated here
 */
function dataObject_populateProperty_SADPATH_DUPLICATED_spoolIds() {
    const dataObject = new DataObject() 
    const excel = [
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
/**
 * The fields of ["spool","uid","count","price"] are mandatory! 
 * Some of them are missing here. 
 */
function dataObject_populateProperty_SADPATH_missingMandatoryFields() {
    const dataObject = new DataObject() 
    const excel = [
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
/**
 * The columns ["spool","uid","count","price"] are mandatory! 
 * They are missing here. 
 */
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
/** 
 * All rows need to be fully left justified
*/
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
/**
 * There are only so many spools that a vending machine can have! 
 * Here, the id is 'A20' but it must be one letter + one single digit number
 */
function dataObject_populateProperty_SADPATH_spoolIdIsInformed() { 
    const dataObject = new DataObject() 
    const excel = [
        ["store", "Test"],
        ["machine", "999"],
        ['keys', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD'],
        ['SPOOL', 'A20', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()

    const errors = Object.keys(shape['errors'])
    const expectedValues = ["spool id error"]
    const isOk = expectedValues.every(val => errors.includes(val));
    verify(isOk, true, "dataObject_populateProperty_SADPATH_spoolIdIsInformed")

}
/**
 * There are only so many spools that a vending machine can have! 
 * Spool ids must be one letter + one single digit number
 */
function dataObject_regex_oneLetterOneNumber_spoolId() { 
    const dataObject = new DataObject() 
    const potentialSpoolIds = {
        "dog":false,
        "a1":true,
        "a11":false,
        "":false,
        "1":false,
        "a":false,
        "aa":false,
        "aaa":false
    }
    let isOk = true 
    for ( let k in potentialSpoolIds ) {
        const outghtToBe = potentialSpoolIds[k]
        const howItIs = dataObject.idReg_oneLetter_oneNumber.test(k)
        if ( howItIs !== outghtToBe ) {
            isOk = false 
        }
    }    
    verify(isOk, true, "dataObject_regex_oneLetterOneNumber_spoolId")
}



/**
 * Harvest has a complex lifecycle
 * Honestly, I sort of forget it...
 * BUT! 
 * Part of it is 'what gets to the web page'
 * and another part of it is 'what gets sent to the backend'. 
 * Now, these two things ought to be the same but...  ...it is not the same. 
 * This is a test to make sure things are synced up. 
 * 
 * TODO: Make 'syncing up' unneeded!  
*/
function dataObject_harvest() {
    const dataObject = new DataObject() 
    const excel = [
        // See? Some slop is OK -  undefined to out of place things will be ignored
        ["store", "Test", undefined, undefined, "ignore"],
        ["machine", "888"], // The last machine will be picked up  
        ["machine", "999"],
        ['keys', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD', "COLUMN_NAME_THIS_DOES_NOT_MATTER"],
        ['This is not a key', 'blah blah'],
        ['SPOOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 44932, 21, 4, 9, 5, "THIS WILL BE IGNORED"],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const shape = dataObject.checkTheShape()
    verify(shape["isOk"], true, "dataObject_harvest")
}


/**
 * The backend will expect a LoH 
 * Double check that the shape is good
 * 
 * TODO! In the dataObject force all keys to UPPER or LOWER case!! 
 */
function dataObject_getSpools_whichIsWhatIsSubmittedToBackend() { 
    const dataObject = new DataObject() 
    const excel = [
        ["storE", "Test"],
        ["macHine", "999"],
        ['keyS', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD'],
        ['SPoOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', '44932', 21, 4, 9, 5],
        ['SPOOL', 'A2', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', '44932', 21, 4, 9, 5],
        ['SPOOL', 'A3', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', '44932', 21, 4, 9, 5],
    ]
    excel.forEach((row)=> { 
        dataObject.addInfo(row)
    })
    const LoH = dataObject.getSpools() 
    actual = [LoH.length, Object.keys(LoH[0]).length]
    expected = [3,2]
    verify(actual, expected, "dataObject_getSpools_whichIsWhatIsSubmittedToBackend")
}

function split_string() { 
    const string_from_input_field = "Mary    HAD a                  little\n lamb\n."
    const text = string_from_input_field.toLowerCase() 
    const actual = text.split(/\W+/).filter(Boolean);
    const expected = [ 'mary', 'had', 'a', 'little', 'lamb' ]
    verify(actual, expected, "split_string: " + actual)
}

function multidimensionalsort_test() { 

    const products = [
        {id:0,"desc":"Pre-roll flower hybrid | introspection, hungery, creative",score:0},
        {id:1,"desc":"Pre-roll flower ruderalis | hungery, relaxation, energy",score:0},
        {id:2,"desc":"edibel thc | energy, energy, vivid colors",score:0},
        {id:3,"desc":"tincture indica highly | relaxation, energy, calm",score:0},
        {id:4,"desc":"Pre-roll flower indica | happy, relax, laughter",score:0},
        {id:5,"desc":"Pre-roll flower sativa | vivid colors, spacey, relax",score:0},
        {id:6,"desc":"concentrate  shatter | creative, relax, happy",score:0},
        {id:7,"desc":"tincture sativa | euphoria, happy, happy",score:0},
        {id:8,"desc":"tincture sativa | hungery, euphoria, euphoria",score:0},
        {id:9,"desc":"tincture sativa | creative, relax, energy",score:0},
        {id:10,"desc":"edibel gummies | introspection, spacey, relaxation",score:0},
        {id:11,"desc":"edibel gummies | introspection, laughter, introspection",score:0},
        {id:12,"desc":"edibel gummies | laughter, relaxation, energy",score:0},
        {id:13,"desc":"concentrate | relax, energy, energy",score:0},
        {id:14,"desc":"concentrate | laughter, creative, slow time",score:0},
        {id:15,"desc":"tincture sativa | euphoria, hungery, spacey",score:0},
        {id:16,"desc":"tincture sativa | introspection, creative, vivid colors",score:0},
        {id:17,"desc":"tincture indica | hungery, hungery, relaxation",score:0},
        {id:18,"desc":"tincture indica | laughter, calm, euphoria",score:0},
        {id:19,"desc":"tincture indica | relaxation, spacey, euphoria",score:0},
        {id:20,"desc":"concentrate shatter | laughter, vivid colors, relax",score:0},
        {id:21,"desc":"concentrate shatter | creative, happy, relaxation",score:0},
        {id:22,"desc":"concentrate shatter | relaxation, energy, vivid colors",score:0},
        {id:23,"desc":"concentrate crumble | laughter, creative, energy",score:0}
    ]
    const list_of_words_from_input_field = ["tincture", "sativa", "happy", "someword"]
    const HIGH_VALUE_WORDS = ["pre-roll", "hybrid", "oil", "sativa", "tincture", "calm", "edibel", "gummie", "gummy", "concentrate", "wax"]
    let t1 = new Date().getTime()
    products.forEach((product)=> { 
        product.score = 0 
    })
    products.forEach((product)=> { 
        list_of_words_from_input_field.forEach((word) => { 
            if ( product.desc.includes(word)) {
                product.score += 1
                if ( HIGH_VALUE_WORDS.includes(word)) {
                    product.score += 10
                }
            }
        }) 
    })
    products.sort((a, b) => b.score -  a.score );

    // products.forEach((product, i )=> { 
    //     console.log( i + "   " + product.id + "   score=" + product.score + "   " + product.desc ) 
    // })
    const milsec = new Date().getTime() - t1; 
    let isOk = milsec < 10 && products[0].score === 23 && products[1].score === 22 && products[products.length - 1].score === 0
    verify(isOk, true, "multidimensionalsort_test milsec=" + milsec)





}


/**
* Test runner
*/
if (require.main === module) {
    dataObject_populateProperty_HAPPYPATH()
    dataObject_populateProperty_SADPATH_missingStuff()
    dataObject_populateProperty_serialDateConvertAndCheck()
    dataObject_populateProperty_SADPATH_DUPLICATED_spoolIds()
    dataObject_populateProperty_SADPATH_missingMandatoryFields()
    dataObject_populateProperty_SADPATH_missingAMandatoryColumns()
    dataObject_populateProperty_SADPATH_notLeftJustified()
    dataObject_populateProperty_SADPATH_spoolIdIsInformed()
    dataObject_regex_oneLetterOneNumber_spoolId() 
    dataObject_harvest()
    dataObject_getSpools_whichIsWhatIsSubmittedToBackend()
    split_string()
    multidimensionalsort_test()
}

