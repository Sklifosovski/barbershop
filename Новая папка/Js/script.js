const galleryContainer = document.querySelector('.gallery-container');

function slideGallery() {
    const scrollAmount = 300; // Adjust as needed
    galleryContainer.scrollLeft += scrollAmount;
}


// swiper  

new Swiper(".swiper-container", {
    spaceBetween: 30,
    slidesPerView: 1,
    centeredSlides: true,
    roundLengths: true,
    loop: true,
    autoplay: {
      display: 1,
      loopAdditionalSlides: 30,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev"
    },

  });