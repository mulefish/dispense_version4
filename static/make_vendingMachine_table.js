function showVendingMachine(vendingMachineId) {

    const headers = { "Content-Type": "application/json" }
        const body = JSON.stringify({"vendingId":vendingMachineId});
        const requestOptions = {
            method: 'POST',
            headers,
            body,
            redirect: 'follow'
        };
        fetch("/get_vending_machine", requestOptions)
            .then(response => response.json())
            .then(obj => {
                const data = obj["data"][0]
                let table = "<table border='1'><tr><th>vendingId</th><th>storeId</th><th>merchantId</th><th>version</th><th>averageMark</th></tr>"
                table += "<tr>"
                table += "<td>" + data[0] + "</td>"                                  
                table += "<td>" + data[1] + "</td>"       
                table += "<td>" + data[2] + "</td>"       
                table += "<td>" + data[3] + "</td>"       
                table += "<td>" + data[4] + "</td>"       
                table += "</tr>"
                table += "<tr><td colspan='5'>" + data[5] + "</td></tr>"
                table += "</table>"

                // document.getElementById("vendingMachine").innerHTML = table; 
            })
            .catch(error => {
                console.log("%c This was an error because: " + error.message, "background:lightred;")
            })
}
