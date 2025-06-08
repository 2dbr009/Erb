document.addEventListener('DOMContentLoaded', () => {
  const imageElement = document.getElementById('gallery-single-image');
  const imageSources = [
    "img/1.jpeg",
    "img/3.jpeg",
    "img/4.jpeg",
    "img/5.jpeg",
    "servicos/img2/photo.jpg",
    "servicos/img2/photo1.jpg",
    "servicos/img2/photo3.jpg",
    "servicos/img2/photo4.jpeg"
  ];
  let currentIndex = 0;

  function showNextImage() {
    currentIndex = (currentIndex + 1) % imageSources.length;
    imageElement.src = imageSources[currentIndex];
  }

  setInterval(showNextImage, 8000); // Change time
});
