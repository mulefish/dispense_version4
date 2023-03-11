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
