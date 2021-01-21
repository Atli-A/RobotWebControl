let instructions = document.getElementById("instructions");


let motorList = ["A", "B", "C", "D", "E", "F"]

let currentMotor = 0

instructions.innerHTML = "Hold space until motor " + motorList[currentMotor] + " stops"


var r = document.querySelector(':root');

let spaceDown = false;



/* functions */
function setBGto(nameOfBG) {

    if (nameOfBG === "dark") {
        r.style.setProperty('--backColor', '#888');

    }
    else if (nameOfBG === "light") {
        r.style.setProperty('--backColor', '#ccc');

    }
    else {
        console.error("Warning: color " + nameOfBG + " is not recognized")
    }
}

/* check if space key is down */
document.body.onkeyup = function (e) {
    if (e.keyCode == 32) {
        spaceDown = false
        setBGto("light")
    }
}


document.body.onkeydown = function (e) {
    if (e.keyCode == 32) {
        spaceDown = true
        setBGto("dark")
    }
}



function calibrationSequence() {
    
}