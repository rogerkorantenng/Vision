// static/scripts/main.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', (event) => {
            const fileInput = form.querySelector('input[type="file"]');
            if (!fileInput.files.length) {
                alert('Please select a file to upload.');
                event.preventDefault();
            }
        });
    }
});
