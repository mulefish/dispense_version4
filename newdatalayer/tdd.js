let letters = ["A", "B", "C", "D", "E"]
let rows_cols = {}
letters.forEach((letter, i)=> { 
    for (let index = 0; index < 8; index++) {
        const key = letter + index 
      
        rows_cols[key] = {}

    }
})
console.log( rows_cols)