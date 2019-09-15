
window.addEventListener("load", () => {
    const canvas = document.querySelector(".canvas");
    const context = canvas.getContext("2d"); 

    canvas.height = 300;
    canvas.width = 300; 

    let painting = false;
    // context.putImageData(, 0, 0);
    function startPosition() {
        painting = true; 
    }
    
    function endPosition(){ 
        painting = false;
        context.beginPath();
    }

    function draw(e){
        if(!painting) return;
        context.lineWidth = 10;
        context.lineCap = "round";
        context.strokeStyle = "black"
        context.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        context.stroke();
        context.beginPath();
        context.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    }

    canvas.addEventListener("mousedown", startPosition);
    canvas.addEventListener("mouseup", endPosition);
    canvas.addEventListener("mousemove", draw);
});
function clear_canvas() {
    const canvas = document.querySelector(".canvas");
    const context = canvas.getContext("2d"); 
    var imgData = context.createImageData(300, 300);
    var i;
    for (i = 0; i < imgData.data.length; i += 4) {
    imgData.data[i+0] = 255;
    imgData.data[i+1] = 255;
    imgData.data[i+2] = 255;
    imgData.data[i+3] = 255;
    }
    context.putImageData(imgData, 0, 0);
}