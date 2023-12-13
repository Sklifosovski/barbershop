const galleryContainer = document.querySelector('.gallery-container');

function slideGallery() {
    const scrollAmount = 300; // Adjust as needed
    galleryContainer.scrollLeft += scrollAmount;
}