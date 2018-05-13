document.getElementById("input").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        search();
    }
});

function search() {
    clean();
    var text = document.getElementById("input").value
    while (text.indexOf(" ") > -1) {
        text = text.replace(" ", "_");
    }
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

        document.getElementById("words").innerHTML = "Query: " + result[0];
        document.getElementById("label").innerHTML = "Total Images Found: " + length.toString();

        //if (length > 100) {
        //    length = 100;
        //}

        for (var i = 0; i < length; i++) {
            path = "image/" + image_path[i];

            var div_par = document.createElement("div");
            div_par.className = "hvrbox"

            var check_box = document.createElement("input");
            check_box.name = "cb";
            check_box.id = "cb" + i.toString()
            check_box.type = "checkbox";
            check_box.value = image_path[i];
            check_box.onchange = function() {
                var values = [];
                var boxes = document.getElementsByName("cb");

                boxes.forEach(box => {
                    if (box.checked == true) {
                        values.push(box.value);
                    }
                });
                var string = "";
                for (var i = 0; i < values.length; i++) {
                    string = string + values[i] + ",";
                    var t = i % 5;
                    if ((t == 0) && (i > 0))
                        string = string + "\n";
                }
                document.getElementById("generated_text").innerHTML = string;
            };

            var img = document.createElement("img");
            img.src = path;
            img.alt = image_path[i];
            img.className = "hvrbox-layer_bottom";
            img.id = "img_" + i.toString();

            img.addEventListener("click", function(e) {
                var img_id = e.path[0].id.split("_");
                var cbid = "cb" + img_id[1];
                var box = document.getElementById(cbid);
                box.checked = !box.checked;

                var values = [];
                var boxes = document.getElementsByName("cb");

                boxes.forEach(box => {
                    if (box.checked == true) {
                        values.push(box.value);
                    }
                });

                var string = "";
                for (var i = 0; i < values.length; i++) {
                    string = string + values[i] + ",";
                    var t = i % 5;
                    if ((t == 0) && (i > 0))
                        string = string + "\n";
                }
                console.log(string);
                document.getElementById("generated_text").innerHTML = string;
            });
            
            div_par.appendChild(check_box)
            div_par.appendChild(img);


            document.getElementById("image").appendChild(div_par);
        }
        return;
    });
    document.getElementById("label").innerHTML = "Server has died.  Please Check Server.";
}

function clean() {
    document.getElementById("label").innerHTML = "";
    document.getElementById("words").innerHTML = "";
    document.getElementById("generated_text").innerHTML = ""
    var myNode = document.getElementById("image");
    while (myNode.firstChild) {
        myNode.removeChild(myNode.firstChild);
    }
}

// document.getElementById("export").addEventListener("click", function () {
//     var filepath = document.getElementById("topic-id").value + ".txt"
//     var txtFile = new File([""], filepath);
//    // var file = fopen(filepath, 3)
//     var output = document.getElementById("generated_text").innerHTML;
//     output = output.split(",");
//     var length = output.length;
//     txtFile.open("w"); 
//     for (var i = 0; i < length; i++) {
//         txtFile.writeln(output[i]);
//      //   fwrite(file, output[i]);
//     }
//     //txtFile.close();
//     console.log("Successfully Export");
// });