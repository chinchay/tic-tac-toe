function handleOnclick(){
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

listen()