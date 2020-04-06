function validateEmail() {
    const email_regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const email_input = document.getElementById("email");
    email_input.value = email_input.value.trim();
    if (email_regex.test(email_input.value)) {
        email_input.className = "form-control is-valid";
        document.getElementById("submit").disabled = false;

    } else {
        email_input.className = "form-control is-invalid";
    }
}
