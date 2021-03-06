// prep---
let slidersArea = document.getElementById("slidersArea")

let sliderSuffixes = ["A", "B", "C", "D", "E", "F"]


let sliderValues = [90, 90, 90, 90, 90, 90]

let host = "localhost"
host = location.host



function createInnerHTMLforSliders(lSliderSuffixes) {
    let result = '';
    for (let i = 0; i < lSliderSuffixes.length; i++) {
        result += '<label for="slide"' + lSliderSuffixes[i] + '>' + lSliderSuffixes[i] + ":  0" + '</label>'

        result += '<label for="slide"' + lSliderSuffixes[i] + '>' + '<input type = "range" min = "0" max = "180" class = "sliders" name = "slide' + lSliderSuffixes[i] + '" id = "slide' + lSliderSuffixes[i] + '">' + '180 </label> <br />';
        let val = "value";
        result += '<p class = "resultingValue" id="' + lSliderSuffixes[i] + val + '">90</p> <br />';
    }


    return result;
}




// //send data



function sendSliderValues() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://" + host, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        positions: sliderValues
    }));
    return false;
}


function sendCommand(inputCommand) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://" + host, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        command: inputCommand
    }));
    return false;
}



//not funtions---------------------------------------


slidersArea.innerHTML = createInnerHTMLforSliders(sliderSuffixes);





function readSlides() {
    for (let i = 0; i < sliderSuffixes.length; i++) {
        eval("slide" + sliderSuffixes[i]).addEventListener("input", function () {
            console.log(sliderSuffixes[i] + " changed to " + document.getElementById("slide" + String(sliderSuffixes[i])).value)
            sliderValues[i] = document.getElementById("slide" + String(sliderSuffixes[i])).value
            document.getElementById(sliderSuffixes[i] + "value").innerHTML = sliderValues[i];
            sendSliderValues();
            // writeToFile('positions.json', JSON.stringify(sliderValues))                //old useless code
        });
    }
}

readSlides();


let restartButton = document.getElementById("restartButton")

restartButton.onclick = function () {
    sendCommand('restart');
}

let shutdownButton = document.getElementById("shutdownButton")

shutdownButton.onclick = function () {
    sendCommmand('shutdown');
}

let resetButton = document.getElementById("resetMotorsButton")

resetButton.onclick = function () {
    sendCommand('reset');

    //reseting positions so that it does not just go right back to where it was
    
    slidersArea.innerHTML = createInnerHTMLforSliders(sliderSuffixes);
}

let exitButton = document.getElementById("exitButton")

exitButton.onclick = function () {
    let choice = confirm("Are you sure you want to exit? \n You will have to ssh in to restart it.")
    if (choice == true) {
        sendCommand('exit');
    	setTimeout(function() {
	    location.reload()
	}, 1000)
	    
    }
    //closes the program
    
}
