
// player = "B"
// `player` is defined in app.py, and read by index.html in <script> tags
function change(){

    // var id = document.getSelection().anchorNode.parentElement.id
    // var element = document.getElementById(id)

    var element = document.getSelection().anchorNode
    console.log("player is: ", player)
    element.style.backgroundColor = ( player === "A" ) ? "blue" : "red"
}