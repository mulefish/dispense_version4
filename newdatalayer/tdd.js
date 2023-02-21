

const l = ['a', 'b', 'c','d', 'e']
const n = [1,2,3,4,5,6]
let table = "<table border='1'>"
l.forEach((letter) => { 
    let tr = "<tr>"
    n.forEach((number) => { 
        const key = letter + number 
        tr += `<td><button onClick="setSelectedRoCol(${key})">${key}</button></td>`
        tr += `<td><input type="number" id="v_${key}" min='0' </td>`
        tr += `<td><div <input type="number" id="v_${key}" min='0' </td>`
    })
    tr += "</tr>"
    table += tr
})
table += "</table>"
