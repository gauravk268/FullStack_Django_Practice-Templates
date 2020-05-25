var clickRestart = document.querySelector('#b');

var currentBox = document.querySelectorAll('td');

var playerLabel = getStartingPlayer();
showPlayer();

//Get Starting player randomly
function getStartingPlayer(){
    var randomPlayer = Math.floor((Math.random() * 2) + 1);
    if(randomPlayer == 1){
      return 'X';
    }
    else{
      return 'O';
    }
}

function showPlayer(){
    document.querySelector('#currentPlayerLabel').textContent = "Current Player: "+ playerLabel;
}

function restart(){
    for (var i = 0; i < currentBox.length; i++) {
        currentBox[i].textContent='';
    }
    
    playerLabel = getStartingPlayer();
    showPlayer();
}

clickRestart.addEventListener('click', restart);

function changeMarker(){
    if(this.textContent === ''){
      this.textContent = playerLabel;
      changePlayer();
    }
};

function changePlayer(){
    if(playerLabel === 'X'){
        playerLabel = 'O';
    }
    else{
        playerLabel = 'X';
    }
    showPlayer();
}

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < currentBox.length; i++) {
    currentBox[i].addEventListener('click', changeMarker);
}