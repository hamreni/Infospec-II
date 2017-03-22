//Segéd

const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

//Állapottér 

let store = {
    state : {

    },
    actions : {
        init : init,
        reveal : reveal
    }
};

function callAction(action, data) {
    store.actions[action](data); //melyik action-t és melyik cellára
    update();
    checkEnd();
}

function reveal(cell) {
    cell.isRevealed = true;
}


function update() {
    $('#_game').innerHTML = '';
    $('#_game').appendChild (Game(store.state.game))
}

function checkEnd() {
    if (store.state.game.some(row => 
    row.some(cell => 
    cell.isRevealed && cell.isMine))) {
        alert ('Game Over');
    } //keresek egy olyat hogy
}

function init() {
    const width = parseInt($('#_width').value);
    const height = parseInt($('#_height').value);
    const minecount = parseInt($('#_minecount').value);
// üres pálya
    store.state.game=[];
    for (let i = 0; i < height; i++) {
        store.state.game[i] = [];
        for (let j = 0; j < width; j++) {
            store.state.game[i][j] = {
                x: i,
                y: j,
                isMine: false,
                isRevealed: false,
                isMarked: false,
                neighborCount: 0,
            } 
        }
    }
    //aknák felrakása
    for (let i = 0; i < minecount; i++) {
        //hátultesztelős ciklussal
        let randomX, randomY
        do {
            randomX = Math.floor (Math.random() * width);//[0,1) 
            randomY = Math.floor (Math.random() * height);
        } while (store.state.game[randomY][randomX].isMine);
        store.state.game[randomY][randomX].isMine = true;
        //szomszédok kezelése
        for (let i = -1; i <= +1; i++) {
            for (let j = -1; j <= +1; j++) {
                if ((i != 0 || j != 0) && 
                (randomX + j >= 0) && 
                (randomX + j < width) &&
                (randomY + i >= 0) && 
                (randomY + i < height) &&
                (!store.state.game[randomY + i][randomX + j].isMine)) {
                store.state.game[randomY + i][randomX + j]
                    .neighborCount++;
                }
            }
        }
    }
    //újragenerálás
    update();
}
 //eseménykezelők
 $('#_start').addEventListener('click', function () {callAction('init');}, false)

//Komponens (html generátorok és eseménykezelők)

function Game(board) {
    return html `<table>${board.map(row => Row(row))}</table`;
}

function Row(row) {
    return html `<tr>${row.map(cell => Cell(cell))}</tr>`;
}

function Cell(cell) {
    function click() {
        callAction('reveal',cell);
    }

    if (store.state.debug) { //ezt konzolba írva = true val használható
    return html `<td>
    <button>${cell.isMine ? '💣' : cell.neighborCount}</button>
    </td>`;
    } else {
    return  html `<td>
    <button onclick = ${click} class = "${cell.isRevealed ? 'revealed' : ''}" >
    ${cell.isRevealed ? (cell.isMine ? '💣' : cell.neighborCount) : ''}
    </button>
    </td>`;//nonbreakablespace
    }
}

//