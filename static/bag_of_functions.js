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
    console.log( JSON.stringify( obj, null, 2 ))
}


////// Show the human if the data is well shaped or not 
const colorDiv = document.getElementById('isItWellFormed');
function indicateIsWellFormed(isOk_orIsNothing_orIsBad, issues) {
    console.log("IWF: " + isOk_orIsNothing_orIsBad)
    if (isOk_orIsNothing_orIsBad == undefined) {
        if (colorDiv.classList.contains(DATA_IS_GOOD)) {

            console.log("A A")
            colorDiv.classList.remove(DATA_IS_GOOD);
            colorDiv.classList.add(DATA_NO_OPINION);
            colorDiv.innerHTML = ""
        } else if (colorDiv.classList.contains(DATA_IS_BAD)) {
            console.log("A B")

            colorDiv.classList.remove(DATA_IS_BAD);
            colorDiv.classList.add(DATA_NO_OPINION);
            colorDiv.innerHTML = ""
        } else {
            console.log("hello the classList is " + colorDiv.classList)
        }
    } else {
        if (isOk_orIsNothing_orIsBad === true) {

            if (colorDiv.classList.contains(DATA_NO_OPINION)) {
                console.log("B A")
                colorDiv.classList.remove(DATA_NO_OPINION);
                colorDiv.classList.add(DATA_IS_GOOD);
                colorDiv.innerHTML = DATA_IS_GOOD
            } else if (colorDiv.classList.contains(DATA_IS_BAD)) {
                console.log("B B")
                colorDiv.classList.remove(DATA_IS_BAD);
                colorDiv.classList.add(DATA_IS_GOOD);
                colorDiv.innerHTML = DATA_IS_GOOD
            }
        } else if (isOk_orIsNothing_orIsBad === false) {
            if (colorDiv.classList.contains(DATA_NO_OPINION)) {
                console.log("C A")

                colorDiv.classList.remove(DATA_NO_OPINION);
                colorDiv.classList.add(DATA_IS_BAD);
                colorDiv.innerHTML = issues
            } else if (colorDiv.classList.contains(DATA_IS_GOOD)) {
                console.log("C B")

                colorDiv.classList.remove(DATA_IS_GOOD);
                colorDiv.classList.add(DATA_IS_BAD);
                colorDiv.innerHTML = issues
            }
        }
    }
}
//////////


///// Most important func /////////////////
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
        const data = []
        const seen = {} 

        rows.forEach((row, i) => {
            if (row.length > 0) {
                const candidate = row[0].trim().toLowerCase()
                if (isValidCommand(candidate)) {
                    seen[candidate]=1
                    data.push(row)
                }
            }
        })

        let issues = "" 
        let isOk = true 
        possibleCommands.forEach((cmd)=> { 
            if ( ! seen.hasOwnProperty(cmd)) {
                issues += cmd + " "
                isOk = false 
            }
        })
        indicateIsWellFormed(isOk, issues)
        log_obj(seen )
    };
    reader.readAsBinaryString(file);
    // function dataIsOkSoFar(data) {
    //     data.each()



    // }
};







const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', (event) => {
     fileUpload(event)
})


