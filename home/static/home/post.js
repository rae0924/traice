function detect() { 
    const canvas = document.querySelector(".canvas");
    // const context = canvas.getContext("2d"); 
    const form = document.querySelector(".post-form");
    form.method = 'post';
    form.action = document.URL;
    const hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'data';
    hiddenField.value = canvas.toDataURL();
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
}
function submit_sample(){
    console.log("hello");
    const canvas = document.querySelector(".canvas");
    const form = document.querySelector(".post-form");
    form.method = 'post';
    form.action = document.URL;
    const hiddenField = document.createElement('input');
    hiddenField.type = 'hidden';
    hiddenField.name = 'data';
    var data = {"x": 10};
    //hiddenField.value = canvas.toDataURL();
    data = JSON.stringify(data);
    hiddenField.value = data;
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
}
