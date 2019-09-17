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
    const dataurl = document.querySelector(".canvas").toDataURL();
    const firstname = document.getElementById("firstname").value;
    const lastname = document.getElementById("lastname").value;
    const email = document.getElementById("email").value;
    const digit = document.getElementById("digit").value;
    const form = document.querySelector(".post-form");
    const hiddenField = document.createElement('input');
    
    form.method = 'post';
    form.action = document.URL;
    hiddenField.type = 'hidden';
    hiddenField.name = 'data';

    var data = {
        "dataurl": dataurl,
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "digit": digit
    };
    
    data = JSON.stringify(data);
    hiddenField.value = data;
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
}
