
// player = "B"
// `player` is defined in app.py, and read by index.html in <script> tags
function handleOnclick(){

    // var id = document.getSelection().anchorNode.parentElement.id
    // var element = document.getElementById(id)

    console.log("You are player: ", player)

    var element = document.getSelection().anchorNode
    element.style.backgroundColor = ( player === "A" ) ? "blue" : "red"
}

function autoClick(){
    const id = document.getElementById("whatId").value
    console.log("the other player has clicked on: ", id)
    
    var element = document.getElementById(id)
    element.style.backgroundColor = ( player === "A" ) ? "red" : "blue"

}

var element = document.getElementById("submitWhatId")
element.addEventListener( "click", () => autoClick() )