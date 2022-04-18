let slideIndex = 0;
// set time chuyển slide=8s
let timeout = setInterval(showSlides, 5000);
function prev_slide() {
  slideIndex = slideIndex - 2
  if (slideIndex < 0) { slideIndex = 2 } // goi ham showslide() se thanh slide 3
  // reset timeout
  showSlides()
  clearInterval(timeout);
  timeout = setInterval(showSlides, 5000);
}
function next_slide() {
  slideIndex = slideIndex
  // reset timeout
  showSlides()
  clearInterval(timeout);
  timeout = setInterval(showSlides, 5000);
}
function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  // hidden all slide
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  // làm mờ hết tất cả các chấm
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  // xac dinh vi tri slide
  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1 }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}
showSlides()