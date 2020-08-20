let currentSlide = 0;
const elements = document.getElementsByClassName('figure-cover');

setInterval(() => {
    for (let i = 0; i < elements.length; i++) {
        elements[i].classList.remove('right');
    }
    elements[currentSlide].classList.remove('active');
    elements[currentSlide].classList.add('right');
    if (currentSlide <= 1) {
        currentSlide += 1;
    } else {
        currentSlide = 0;
    }
    elements[currentSlide].classList.add('active');
}, 5000);

const pages = {
    1: '0%',
    2: '-105.8%'
};

let currentPage = 1;

function change() {
    console.log('asd');
    currentPage = currentPage == 1 ? 2 : 1;
    document.getElementById('companies').style.transform = `translate(${pages[currentPage]})`;
}
