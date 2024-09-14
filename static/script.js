// Addition form submit
document.getElementById('addition-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let num1 = document.getElementById('num1').value;
    let num2 = document.getElementById('num2').value;

    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `num1=${num1}&num2=${num2}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('add-result').textContent = `Result: ${data.result}`;
    });
});

// Factorial form submit
document.getElementById('factorial-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let number = document.getElementById('factorial-num').value;

    fetch('/factorial', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `number=${number}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('factorial-result').textContent = `Result: ${data.result}`;
    });
});
