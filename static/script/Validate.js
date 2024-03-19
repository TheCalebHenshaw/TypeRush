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
            messages.push('username is too short')
        }

        if (sqlChars.test(username.value)) {
            messages.push(`username cannot contain [ ; ' " \\ ]`);
        }

        if (hasNumber.test(firstname.value)) {
            messages.push('firstname cannot contain numbers')
        }

        if (hasNumber.test(surname.value)) {
            messages.push('surname cannot contain numbers')
        }

        if (password.value.length <= 5) {
            messages.push('password must be longer than 6 characters')
        }

        if (password.value.length >= 15) {
            messages.push('password must be shorter than 15 characters')
        }
  
        if (sqlChars.test(password.value)) {
            messages.push(`password cannot contain [ ; ' " \\ ]`);
        }
        
        if (messages.length > 0) {
            e.preventDefault();
            errorElement.innerHTML = messages.join('<br>');
            errorElement.classList.add('show'); 
        } else {
            errorElement.textContent = ''; 
            errorElement.classList.remove('show'); 
        }
    
    })
});