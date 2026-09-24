
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

function startCountdown(duration) {
    const timerElement = document.getElementById('time');
    let timeRemaining = duration;

    function updateTimer() {
        const hours = Math.floor(timeRemaining / 3600);
        const minutes = Math.floor((timeRemaining % 3600) / 60);
        const seconds = timeRemaining % 60;

        timerElement.textContent = 
            `${hours}:${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        
        if (timeRemaining > 0) {
            timeRemaining--;
        } else {
            clearInterval(countdownInterval);
            timerElement.textContent = "Time's up!";
        }
    }

    updateTimer();
    const countdownInterval = setInterval(updateTimer, 1000);
}

// 24 hours = 86400 seconds
startCountdown(86400);

function enrollInClinic(event) {
    // 1. Prevents the form from refreshing the page
    event.preventDefault();

    // 2. Your destination WhatsApp number (country code 234 without +)
    const phoneNumber = "2349057666827";

    // 3. Extract exact values entered into the input fields
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const business = document.getElementById("business_type").value.trim();

    // 4. Build the structured message
    const formattedMessage = 
        `Hello TIDA, I am applying for the *Sales & Marketing Clinic Premium* membership.%0A%0A` +
        `*Full Name:* ${encodeURIComponent(name)}%0A` +
        `*Email:* ${encodeURIComponent(email)}%0A` +
        `*Phone:* ${encodeURIComponent(phone)}%0A` +
        `*Business Type:* ${encodeURIComponent(business)}`;

    // 5. Open WhatsApp pre-filled with all their responses
    const whatsappUrl = `https://wa.me/${phoneNumber}?text=${formattedMessage}`;
    window.open(whatsappUrl, "_blank");
}
