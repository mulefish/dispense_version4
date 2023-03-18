const { DATA_NO_OPINION, DATA_IS_GOOD, DATA_IS_BAD, HIDE_ME, SHOW_ME, possibleCommands, mandatoryColumns, NILL } = require('./globals.js');
const DataObject = require('./dataObject.js');
const Reset = "\x1b[0m"
const BgRed = "\x1b[41m"
const BgGreen = "\x1b[42m"
function log(msg) {
    console.log(msg)
}
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
    dataObject.addInfo(excel[0])
    dataObject.addInfo(excel[1])
    dataObject.addInfo(excel[2])
    dataObject.addInfo(excel[3])
    dataObject.addInfo(excel[4])
    dataObject.addInfo(excel[5])
    const shape = dataObject.checkTheShape()
    verify(shape["isOk"], true, "dataObject_populateProperty_HAPPYPATH")
}

function dataObject_populateProperty_SADPATH_missingStore_and_machine() {
    dataObject = new DataObject() 
//    log( dataObject )
    const excel = [
        // See? Some slop is OK -  undefined to out of place things will be ignored
        ["store", "Test", undefined, undefined, "ignore"],
        ["machine", "888"], // The last machine will be picked up  
        ["machine", "999"],
        ['keys', 'spool', 'uid', 'count', ' price', 'Type', 'grams', 'Producer', 'Strain', 'Classification', 'BatchInfo', 'Harvest', 'Canabinoids', 'THC-A', 'Delta_9', 'CBD'],
        ['This is not a key', 'blah blah'],
        ['SPOOL', 'A1', '15643151 - A1', 9, 25, 'Flower', 3.5, 'Paddle Creek Cannabis', 'Green Arrow', 'Sativa', 'KLT - 685115300', 'dinoblank', 21, 4, 9, 5],
    ]
    dataObject.addInfo(excel[0])
    dataObject.addInfo(excel[1])
    dataObject.addInfo(excel[2])
    dataObject.addInfo(excel[3])
    dataObject.addInfo(excel[4])
    dataObject.addInfo(excel[5])
    const shape = dataObject.checkTheShape()
    verify(shape["isOk"], true, "dataObject_populateProperty_HAPPYPATH")
}



if (require.main === module) {
    dataObject_populateProperty_HAPPYPATH()
    dataObject_populateProperty_SADPATH_missingStore_and_machine()

}
