const possibleCommands = ["machine", "store", "spool", "keys"];

const seen = {} 


const allKeysHaveValueOne = possibleCommands.every(key => {
    const value = seen[key];
    return value === 1;
  });

possibleCommands.forEach((cmd)=> { 
    seen[cmd] = 1
})

console.log(  allKeysHaveValueOne) 


const allKeysHaveValueOne1 = possibleCommands.every(key => {
    const value = seen[key];
    return value === 1;
  });

  console.log(  allKeysHaveValueOne1) 



seen["store"]=0
// console.log( allKeysHaveValueOne(seen)) 
