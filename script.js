document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const url = document.getElementById('url').value;
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `url=${encodeURIComponent(url)}`
        });

        const result = await response.json();
        resultDiv.innerHTML = result.result;
    });
});