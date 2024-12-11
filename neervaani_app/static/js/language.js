document.addEventListener('DOMContentLoaded', () => {
    const languageSelect = document.getElementById('languageSelect');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    languageSelect.addEventListener('change', async (event) => {
        const selectedLang = event.target.value;

        const response = await fetch('/set-language/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ lang_id: selectedLang }),
        });

        const data = await response.json();
        if (data.status === 'success') {
            location.reload();
        } else {
            console.error('Language change failed:', data.message);
        }
    });
});
