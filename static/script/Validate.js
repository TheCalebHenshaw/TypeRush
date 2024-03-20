document.addEventListener("DOMContentLoaded", function() {
    const username = document.getElementById('username');
    const firstname = document.getElementById('firstname');
    const surname = document.getElementById('surname');
    const password = document.getElementById('password');
    const form = document.getElementById('form');
    const errorElement = document.getElementById('error');

    form.addEventListener('submit', (e) => {
        let messages = [];
        var hasNumber = /\d+/;  
        const sqlChars = /[ ;'"\\]/;

        if (username.value.length <= 2) {
            messages.push('Username is too short')
        }

        if (sqlChars.test(username.value)) {
            messages.push(`Username cannot contain [ ; ' " \\ ]`);
        }

        if (hasNumber.test(firstname.value)) {
            messages.push('First name cannot contain numbers')
        }

        if (hasNumber.test(surname.value)) {
            messages.push('Surname cannot contain numbers')
        }

        if (password.value.length <= 5) {
            messages.push('Password must be longer than 6 characters')
        }

        if (password.value.length >= 15) {
            messages.push('Password must be shorter than 15 characters')
        }
  
        if (sqlChars.test(password.value)) {
            messages.push(`Password cannot contain [ ; ' " \\ ]`);
        }

        errorElement.textContent = ''; 
        errorElement.classList.remove('show'); 
        if (messages.length > 0) {
            e.preventDefault();
            errorElement.innerHTML = messages.join('<br>');
            errorElement.classList.add('show'); 
        } 
        else { 
        }
    
    })

    function handleFileSelect(event) {
        const file = event.target.files[0];
        const reader = new FileReader();
        
        reader.onload = function(event) {
            const imageUrl = event.target.result;
            // Display the selected image preview
            document.getElementById('profile-picture-preview').src = imageUrl;
        }
        
        reader.readAsDataURL(file);
    }

    // Add event listener to input element for file selection
    document.getElementById('profile_picture').addEventListener('change', handleFileSelect);
});