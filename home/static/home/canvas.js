
window.addEventListener("load", () => {
    const canvas = document.querySelector(".canvas");
    const context = canvas.getContext("2d"); 

    canvas.height = 200;
    canvas.width = 200;

    let painting = false;

    function startPosition() {
        painting = true;
    }
    
    function endPosition(){
        painting = false;
        context.beginPath();
        console.log(canvas.toDataURL())
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
