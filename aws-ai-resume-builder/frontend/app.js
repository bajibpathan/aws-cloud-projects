const loginForm = document.getElementById("login-form");
const statusMessage = document.getElementById("status-message");

loginForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;

    statusMessage.textContent =
        `Sign-in form submitted for ${email}. Cognito integration will be added next.`;
});