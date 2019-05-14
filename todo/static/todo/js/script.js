try {
    datePicker = document.getElementById('datePicker');
    if(!datePicker.value) {
        datePicker.valueAsDate = new Date();
    }
} catch (e) {
    console.log('not right page');
}

try {
    let slide = document.getElementById("percentReady");
    let y = document.getElementById("rangeValue");
    y.value = slide.value;

    slide.oninput = function () {
        y.value = this.value;
    };

    y.oninput = function () {
        if (!this.value) {
            slide.value = 50;
        } else if (this.value > 100) {
            slide.value = 100;
        } else if (this.value < 0) {
            slide.value = 0;
        } else {
            slide.value = this.value;
        }
    };
} catch (e) {
    console.log('not right page')
}