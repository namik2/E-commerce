let subscriberForm = document.getElementById("subscribe-form");
subscriberForm.addEventListener('submit', function (e) {
    e.preventDefault();
    let postData = {
        "email": subscriberForm.email.value
    }
    let res = fetch(url = '/api/subscribe/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": subscriberForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify(postData),
    })
        .then(function (response) {
            if (response.ok) {
                alert('Ugurla Abone Oldunuz');
            } else {
                return response.json().then(text => {

                    alert(text.email.join(','));
                    `
                    {
                        "email": ["Subscriber with this subscriber email already exists."]
                    }
                    `
                })
            }
            return response.json();
        })
})