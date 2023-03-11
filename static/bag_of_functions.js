const colorDiv = document.getElementById('isItWellFormed');
function toggleColor() {
  if (colorDiv.classList.contains('white')) {
    colorDiv.classList.remove('white');
    colorDiv.classList.add('red');
    colorDiv.innerHTML = "NO"
  } else if (colorDiv.classList.contains('red')) {
    colorDiv.classList.remove('red');
    colorDiv.classList.add('green');
    colorDiv.innerHTML = "YES"
  } else {
    colorDiv.classList.remove('green');
    colorDiv.classList.add('white');
    colorDiv.innerHTML = ""
  }
}


function indicateIsWellFormed(isOk_orIsNothing_orIsBad) {
    if ( isOk_orIsNothing_orIsBad === undefined ) {
        if (colorDiv.classList.contains("green")) {
            colorDiv.classList.remove("green");
            colorDiv.classList.add("white");
            colorDiv.innerHTML = "NOTHING"
        } else if (colorDiv.classList.contains('red')) {
            colorDiv.classList.remove('red');
            colorDiv.classList.add('white');
            colorDiv.innerHTML = "NOTHING"
        }
    } else {
        if (isOk_orIsNothing_orIsBad === true ) {
            if (colorDiv.classList.contains('white')) {
                colorDiv.classList.remove('white');
                colorDiv.classList.add('green');
                colorDiv.innerHTML = "YES"
            } else if (colorDiv.classList.contains('red')) {
                colorDiv.classList.remove('red');
                colorDiv.classList.add('green');
                colorDiv.innerHTML = "YES"
            }
        } else if ( isOk_orIsNothing_orIsBad === false ) { 
            if (colorDiv.classList.contains('white')) {
                colorDiv.classList.remove('white');
                colorDiv.classList.add('red');
                colorDiv.innerHTML = "NO"
            } else if (colorDiv.classList.contains('green')) {
                colorDiv.classList.remove('green');
                colorDiv.classList.add('red');
                colorDiv.innerHTML = "NO"
            }
        }
     }
  }
  