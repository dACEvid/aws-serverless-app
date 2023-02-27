var API_ENDPOINT = '<myAPIEndpooint>/reminders';

// divs to display interactive messages
var errorDiv = document.getElementById('error-message')
var successDiv = document.getElementById('success-message')
var resultsDiv = document.getElementById('results-message')

function clearNotifications() {
    errorDiv.textContent = '';
    resultsDiv.textContent = '';
    successDiv.textContent = '';
}

// Add listeners for each button that make the API request
document.getElementById('bothButton').addEventListener('click', function(e) {
    sendData(e, 'both');
});

document.getElementById('emailButton').addEventListener('click', function(e) {
    sendData(e, 'email');
});

document.getElementById('smsButton').addEventListener('click', function(e) {
    sendData(e, 'sms');
});

function sendData (e, pref) {s
    e.preventDefault()
    clearNotifications()

    fetch(API_ENDPOINT, {
        headers:{
            "Content-type": "application/json"
        },
        method: 'POST',
        body: JSON.stringify({
            waitSeconds: document.getElementById('waitSeconds').value,
            preference: pref,
            message: document.getElementById('message').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value
        }),
        mode: 'cors'
    })
    .then((resp) => resp.json())
    .then(function(data) {
        console.log(data)
        successDiv.textContent = 'Looks OK. Check the result below!';
        resultsDiv.textContent = JSON.stringify(data);
    })
    .catch(function(err) {
        errorDiv.textContent = 'There was an error:\n' + err.toString();
        console.log(err)
    });
};
