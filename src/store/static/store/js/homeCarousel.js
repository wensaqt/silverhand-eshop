class Carousel {
    /**
     * @param {HTMLElement} element 
     * @param {Object} options 
     * @param {Object} options.slidesToScroll --> nombre d'éléments à faire défiler
     * @param {Object} options.slidesVisible --> nombre d'éléments visibles dans un slide
     */
    constructor(element, options = {}) {
        this.element = element;
        this.options = Object.assign({}, {
            slidesToScroll: 1,
            slidesVisible: 1
        }, options)
    }
}

document.addEventListener('DOMContentLoaded', function () {
    new Carousel(document.querySelector('.news'), {
        slidesToScroll: 3,
        slidesVisible: 3
    });
});

