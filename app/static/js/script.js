

// Navigation bar

window.addEventListener('scroll', function() {
    if (window.scrollY >= 40) {
      document.querySelector('.navigation-bar-1').classList.add('hidden');
      document.querySelector('.navigation-bar-2').classList.remove('hidden');
    } else {
      document.querySelector('.navigation-bar-1').classList.remove('hidden');
      document.querySelector('.navigation-bar-2').classList.add('hidden');
    }
  });


  function myFunction() {
    var element = document.getElementById("myDIV");
    element.classList.toggle("mystyle");
  }


// Button submit spinner

                           




// Slide container-1
 
var swiper = new Swiper(".slide-container-1", {
  slidesPerView: 10,
  spaceBetween: 20,
  slidesPerGroup: 1, // Set to 1 to slide one group at a time
  loop: true,
  centerSlide: true,
  fade: true,
  grabCursor: true,
  pagination: {
      el: ".swiper-pagination-1",
      clickable: true,
      dynamicBullets: true,
  },
  navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
  },
  breakpoints: {
      0: {
          slidesPerView: 1,
          slidesPerGroup: 1,
      },
      520: {
          slidesPerView: 2,
          slidesPerGroup: 1,
      },
      768: {
          slidesPerView: 3,
          slidesPerGroup: 1, // Adjust here to slide one group at a time
      },
      1000: {
          slidesPerView: 5,
          slidesPerGroup: 1, // Adjust here to slide one group at a time
      },
  },
});

// slider-container-2

var swiper = new Swiper(".slide-container-2",{
  slidesPerView: 3,
  spaceBetween: 20,
  sliderPerGroup: 3,
  loop: true,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  pagination: {
    el: ".swiper-pagination-2",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1000: {
  slidesPerView: 3,
},
  },
});



// Slider-container-3

var swiper = new Swiper(".slide-container-3",{
  slidesPerView: 3,
  spaceBetween: 20,
  sliderPerGroup: 3,
  loop: true,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  pagination: {
    el: ".swiper-pagination-3",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1000: {
  slidesPerView: 3,
},
  },
});


// Slider-container-4

var swiper = new Swiper(".slide-container-4",{
  slidesPerView: 3,
  spaceBetween: 20,
  sliderPerGroup: 3,
  loop: true,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  pagination: {
    el: ".swiper-pagination-4",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1000: {
  slidesPerView: 3,
},
  },
});


// gallery
lightbox.option({
  'resizeDuration': 200,
  'wrapAround': true
});

