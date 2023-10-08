const socket = new WebSocket('ws://' + location.host + '/echo');

urls = ["https://storage.googleapis.com/hackuta2023-image-bucket/img_camera_out/raul.png?authuser=1",
        "https://storage.googleapis.com/hackuta2023-image-bucket/img_camera_out/MainPic.jpg?authuser=1",
        "https://storage.googleapis.com/hackuta2023-image-bucket/img_camera_out/MainPic.png?authuser=1"]
activ_url = 1

socket.addEventListener('message', ev => {
    console.log("recieved:" + ev.data)
    if (ev.data.startsWith("newImage1: ")){
        urls[0] = ev.data.slice(11);
        document.getElementById(activ_url+"th").src = urls[0];
    } else if (ev.data.startsWith("newImage2: ")){
        urls[1] = ev.data.slice(11);
        document.getElementById(activ_url+"th").src = urls[1];
    } else if (ev.data.startsWith("newImage3: ")){
        urls[2] = ev.data.slice(11);
        document.getElementById(activ_url+"th").src = urls[2]
    } else {
        console.log("Nothing to report")
    }
})

function clear_div(id){
    document.getElementById(id).innerHTML="";
}

function change_image(direct){
    if (direct == "right"){
        console.log("right")
        // document.getElementById(activ_url+"th").style.animation = "right .5s"
        activ_url += 1;
    } else if (direct == "left"){
        console.log("left")
        // document.getElementById(activ_url+"th").style.animation = "left .5s"
        activ_url -= 1;
    }
    
    document.getElementById("qr").innerHTML = "";
    new QRCode(document.getElementById("qr"),  urls[activ_url]);

    if (activ_url == 0) {
        disable_left();
        enable_right();
    } else if (activ_url == 2){
        disable_right()
        enable_left();
    } else {
        enable_right();
        enable_left();
    }

    for(var i = 0; i < 3; i++){
        if (i != activ_url){
            document.getElementById(i+"th").style.display = "none"
        } else {
            document.getElementById(activ_url+"th").style.display = "block"
        }
    }

    console.log(activ_url)
}

function disable_left(){
    document.getElementById("left").setAttribute("onclick", "");
}

function disable_right(){
    document.getElementById("right").setAttribute("onclick", "");
}

function enable_left(){
    document.getElementById("left").setAttribute("onclick", "change_image('left')");
}

function enable_right(){
    document.getElementById("right").setAttribute("onclick", "change_image('right')");
}