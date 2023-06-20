// Código JavaScript para o funcionamento do slider
let sliderIndex = 0;
const sliderItems = document.querySelectorAll("#slider li");
function showSlide(index) {
    for (let i = 0; i < sliderItems.length; i++) {
        sliderItems[i].style.display = "none";
    }
    sliderItems[index].style.display = "block";
}

function nextSlide() {
    sliderIndex++;
    if (sliderIndex >= sliderItems.length) {
        sliderIndex = 0;
    }
    showSlide(sliderIndex);
}

function previousSlide() {
    sliderIndex--;
    if (sliderIndex < 0) {
        sliderIndex = sliderItems.length - 1;
    }
    showSlide(sliderIndex);
}

// Exibe o primeiro slide ao carregar a página
showSlide(sliderIndex);

// Avança para o próximo slide a cada 3 segundos
setInterval(nextSlide, 3000);