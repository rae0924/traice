function post() { 
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