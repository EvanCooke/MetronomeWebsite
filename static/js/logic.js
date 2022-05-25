// https://stackoverflow.com/questions/10671174/changing-button-text-onclick
function change()
{
    var elem = document.getElementById("startStopButton");
    if (elem.value=="Start") elem.value = "Stop";
    else elem.value = "Start";
}

var slider = document.getElementById("myRange");
var output = document.getElementById("bpmNum");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
output.innerHTML = this.value;
}