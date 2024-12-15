
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

function showSidebar() {
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
}

function hideSidebar() {
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
}

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

// const menuToggle = document.getElementsByClassName('menu-toggle')[0]
// const navbarLinks = document.getElementsByClassName('navbar-links')[0]

// menuToggle.addEventListener('click', () => {
//     navbarLinks.classList.toggle('active')
// })


