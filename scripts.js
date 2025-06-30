
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
