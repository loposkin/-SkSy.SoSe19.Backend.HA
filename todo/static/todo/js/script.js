document.getElementById('datePicker').valueAsDate = new Date();

let slide = document.getElementById("percentReady");
let y = document.getElementById("rangeValue");
y.value = slide.value;

slide.oninput = function() {
    y.value = this.value;
};

y.oninput = function () {
    if(isNaN(this.value)) {
        slide.value = 50;
    } else if(this.value > 100) {
        slide.value = 100;
    } else if(this.value < 0) {
        slide.value = 0;
    } else {
        slide.value = this.value;
    }
};