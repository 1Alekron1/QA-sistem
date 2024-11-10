document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("questionForm");
    const loading = document.getElementById("loading");

    form.addEventListener("submit", () => {
        // Показать анимацию загрузки
        loading.classList.add("show");
    });
});
