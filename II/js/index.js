//SEGÉDFV////////////////

const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

//ADATOK/////////////////



//ESEMÉNYKEZELŐK/////////

//amikor lenyomok egy billentyűt
function keyupEditor(event) {
    //console.log(event)
    if (event.ctrlKey && event.keyCode === 13) {
        //eredeti funkció letiltása
        event.preventDefault();
        //beolv
        let text = $('#_editor').value; 
        //kiir
        $('#_output').innerHTML = TextOutput(text);
    }
}

$('#_editor').addEventListener('keyup', keyupEditor, false);

function rightClickNo(e) {
    event.prevetDefault();

}
$('html').addEventListener('contextmenu', rightClickNo, false);

function copyNo(e) {
    if (event.ctrlKey && (event.keyCode === 67 || event.keyCode == 86)){
    event.prevetDefault();
    }
}
$('html').addEventListener('keydown', copyNo, false);

//HTML GENERÁTOROK///////

function TextOutput(markdown) {
    return marked(markdown); //külső könyvtár
}
