async function fetchTopWords() {
    const url = document.getElementById('urlInput').value;
    if (!url) {
        alert("Please enter a URL");
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/fetch-words', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
    });

    const result = await response.json();
    if (response.ok) {
        displayResults(result);
    } else {
        alert(result.error || "An error occurred");
    }
}

function displayResults(words) {
    const tbody = document.querySelector('#resultTable tbody');
    tbody.innerHTML = '';
    words.forEach(([word, freq]) => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${word}</td><td>${freq}</td>`;
        tbody.appendChild(row);
    });
}
