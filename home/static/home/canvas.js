
window.addEventListener("load", () => {
    const canvas = document.querySelector(".canvas");
    const context = canvas.getContext("2d"); 

    let painting = false;
    
    function startPosition() {
        painting = true;
    }
    
    function endPosition(){
        painting = false;
    }

    function draw(e){
        if(!painting) return;
        context.lineWidth = 10;
        context.lineCap = "round";
    }
});
