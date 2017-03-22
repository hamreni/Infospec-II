//SEGÉDFV///////////////////////////////////////////////////////////
function $(selector) {
    return document.querySelector(selector);
}

function $$(selector) {
    return document.querySelectorAll(selector);
}

/*let $ = document.querySelector;
let $$ = document.querySelectorAll; //kevésbé lassú és energiapazarló, mint az ea-s példa*/

//ADATOK///////////////////////////////////////////////////////////////

let todos = [];

//ESEMÉNYKEZELŐK/////////////////////////////////////////////////////////

function buttonClickHandler() {//minek, milyét, milyen típusú fv
    //beolvasás
    let todoTxt = $('#todoInput').value
    //feldolgozás
    todos.push(todoTxt)
    //kiírás
    $('#todoList').innerHTML = TodoList(todos)
    //$('#todoList').innerHTML += TodoItem(todTxt)

}

$('#addButton').addEventListener('click', buttonClickHandler, false); //nem meghívjuk, hanem hozzárendeljük a fv-t nincs () a buttonClickHandler után
//HTML GENERÁTOROK////////////////////////////////////////////////////////

function TodoList(todoList){ /*TODO-k tömbje*/
    // let html = '';
    // for (let todo of todoList) {
    //     html += TodoItem(todo);
    // }
    // return html;

    return todoList.map(todo => TodoItem(todo)).join("");
}

function TodoItem(todo) { /*1db todo*/
    return `<li>${todo}</li>`;


}