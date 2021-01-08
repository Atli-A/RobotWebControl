// prep---
let slidersArea = document.getElementById("slidersArea")

let sliderSuffixes = ["A", "B", "C", "D", "E", "F"]


let sliderValues = [90, 90, 90, 90, 90, 90]

// let sliderExample = '< input type = "range" name = "slide' +  + '" id = "slide' +  + '" >'


//functions-------------------------------------------------------



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
    xhr.open("POST", "http://localhost:8888", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        positions: sliderValues
    }));
    return false;
}




//not funtions---------------------------------------


slidersArea.innerHTML = createInnerHTMLforSliders(sliderSuffixes);





console.log("test")


// for (let i = 0; i < sliderSuffixes.length; i++) {
//     eval("slide" + sliderSuffixes[i]).addEventListener("change", function() {
//         console.log("settig inner html")
//         document.getElementById(sliderSuffixes[i] + "value").innerHTML = "90";
//     });
// }
for (let i = 0; i < sliderSuffixes.length; i++) {
    eval("slide" + sliderSuffixes[i]).addEventListener("change", function () {
        console.log(sliderSuffixes[i] + " changed to " + document.getElementById("slide" + String(sliderSuffixes[i])).value)
        sliderValues[i] = document.getElementById("slide" + String(sliderSuffixes[i])).value
        document.getElementById(sliderSuffixes[i] + "value").innerHTML = sliderValues[i];
        // writeToFile('positions.json', JSON.stringify(sliderValues))                //old useless code
    });
}



let sendButton = document.getElementById("sendButton")

sendButton.onclick = function () {
    sendSliderValues();
}