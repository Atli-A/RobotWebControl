function sendData() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:65432", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        value: 100
    }));
    false;
}