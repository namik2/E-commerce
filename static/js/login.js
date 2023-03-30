const LoginLogic = {
    'url': `${location.origin}/api/token/`,

    fetchToken(email, password) {
        fetch(this.url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'email': email,
                'password': password
            })
        }
        ).then(response => response.json()).then(data => {
            localStorage.setItem('data', data)
            if (data.access) {
                localStorage.setItem('token', data.access);
            }
            else {
                alert(data.message)
            }
        })
    }
}

const submit = document.getElementById('send2');
const form = document.getElementById('login-form');

submit.onclick = function() {
    const email = document.querySelector('#id_username').value;
    console.log(email);
    const password = document.querySelector('#id_password').value;
    LoginLogic.fetchToken(email, password);
    setTimeout(form.submit(), 1000);
}
 