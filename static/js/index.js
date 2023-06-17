
// player = "B"
// `player` is defined in app.py, and read by index.html in <script> tags
function handleOnclick(){

    // var id = document.getSelection().anchorNode.parentElement.id
    // var element = document.getElementById(id)

    // `player` is defined in index.html as `player = "{{player}}"`
    

    var element = document.getSelection().anchorNode
    element.style.backgroundColor = ( player === "1" ) ? "blue" : "red"
    
    var id = document.getSelection().anchorNode.id
    console.log("You are player: ", player, " and you tapped: ", id)

    // now you are ready to listen
    listen()


    // send this `id` to the other player so he can color it in his screen  
    fetch(
        "/send",
        {
            headers: {
                "Content-Type" : "application/text"
            },
            
            method: "POST",

            body: id
        }
    
    )


}

function listen(){
    // const id = document.getElementById("whatId").value
    // console.log("the other player has clicked on: ", id)
    // var element = document.getElementById(id)
    // element.style.backgroundColor = ( player === "A" ) ? "red" : "blue"

    // // `squarePartnerTapped` is defined in index.html
    // // as `squarePartnerTapped = "{{squarePartnerTapped}}"`
    // console.log("the other player has clicked on: ", squarePartnerTapped)
    // var element = document.getElementById(squarePartnerTapped)
    // element.style.backgroundColor = ( player === "A" ) ? "red" : "blue"

    fetch('/receive')
    .then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('GET response text:')
        console.log(text)

        var element = document.getElementById(text)
        element.style.backgroundColor = ( player === "1" ) ? "red" : "blue"
    
    })



}

console.log("hi there")

listen()

// if (player == "2") {
//     listen()
// }

// var element = document.getElementById("submitWhatId")
// element.addEventListener( "click", () => autoClick() )

// https://healeycodes-com.translate.goog/talking-between-languages?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc&_x_tr_hist=true