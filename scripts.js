document.getElementById("input").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        search();
    }
});

function search() {
    clean();        
    var text = document.getElementById("input").value
    var theUrl = 'http://127.0.0.1:5000/search?text=' + text;
    console.log(theUrl);
    fetch(theUrl).then(response => response.text()).then(function(data) {
        if (data === "NULL") {
            document.getElementById("label").innerHTML = "Total Images Found: 0";
            return; 
        }
        var result = data.split("\n");
        var image_path = result[1].split(" ");
        var length = image_path.length;

        document.getElementById("words").innerHTML = "Cadidate words: " + result[0];
        document.getElementById("label").innerHTML = "Total Images Found: " + length.toString();

        if (length > 100) {
            length = 100;
        }

        for (var i = 0; i < length; i++) {
            path = "image/" + image_path[i];
            var div_par = document.createElement("div");
            div_par.className = "hvrbox"

            var img = document.createElement("img");
            img.src = path;
            img.alt = image_path[i];
            img.className = "hvrbox-layer_bottom";

            var div_overlay = document.createElement("div");
            div_overlay.className = "hvrbox-layer_top";

            var div_text = document.createElement("div");
            div_text.className = "hvrbox-text";
            div_text.innerHTML = image_path[i];

            div_overlay.appendChild(div_text);
            div_par.appendChild(img);
            div_par.appendChild(div_overlay);

            document.getElementById("image").appendChild(div_par);
        }
        return;
    });
    document.getElementById("label").innerHTML = "Server has died.  Please Check Server.";
}

function clean() {
    document.getElementById("label").innerHTML = "";
    document.getElementById("words").innerHTML = "";
    var myNode = document.getElementById("image");
    while (myNode.firstChild) {
        myNode.removeChild(myNode.firstChild);
    }
}