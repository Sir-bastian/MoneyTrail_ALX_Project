document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const registrationForm = document.getElementById('registrationForm');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Make a POST request to login endpoint
        fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Invalid username or password');
        })
        .then(data => {
            console.log(data.message); // Print success message
            // Redirect to dashboard or perform desired action
        })
        .catch(error => {
            console.error('Login Error:', error.message);
            // Display error message to user
        });
    });

    registrationForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const newUsername = document.getElementById('newUsername').value;
        const newPassword = document.getElementById('newPassword').value;

        // Make a POST request to register endpoint
        fetch('http://localhost:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: newUsername,
                password: newPassword
            })
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Registration failed');
        })
        .then(data => {
            console.log(data.message); // Print success message
            // Redirect to login page or perform desired action
        })
        .catch(error => {
            console.error('Registration Error:', error.message);
            // Display error message to user
        });
    });

    // Function to toggle visibility of help box
    function toggleHelpBox() {
        var helpBox = document.getElementById('help-box');
        var helpBtn = document.getElementById('help-btn');
      
        if (!helpBox) {
            return; // Exit if helpBox is not found
        }

        if (helpBox.classList.contains('active')) {
            helpBox.classList.remove('active');
            helpBtn.innerHTML = '<i class="fas fa-question-circle"></i>';
        } else {
            helpBox.classList.add('active');
            helpBtn.innerHTML = '<i class="fas fa-times"></i>';
        }
    }

    // Attach click event listener to help button
    var helpBtn = document.getElementById('help-btn');
    if (helpBtn) {
        helpBtn.addEventListener('click', toggleHelpBox);
    }
});
