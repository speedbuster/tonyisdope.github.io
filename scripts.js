document.addEventListener("DOMContentLoaded", function() {
    // Form validation
    const contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        if (name && email && message) {
            alert('Thank you for contacting us!');
            contactForm.reset();
        } else {
            alert('Please fill in all fields.');
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.getElementById('mobile-menu');
    const navList = document.querySelector('.nav-list');

    menuToggle.addEventListener('click', function() {
        menuToggle.classList.toggle('active');
        navList.classList.toggle('active');
    });
});


// document.addEventListener("DOMContentLoaded", function() {
//     const ctaButtons = document.querySelectorAll('.cta');

//     ctaButtons.forEach(button => {
//         button.addEventListener('click', function(event) {
//             event.preventDefault();
//             const whatsappNumber = 'YOUR_WHATSAPP_NUMBER';
//             const message = encodeURIComponent("I'm interested in the Facebook Ads Mastery Course");
//             window.location.href = `https://wa.me/${whatsappNumber}?text=${message}`;
//         });
//     });
// });
