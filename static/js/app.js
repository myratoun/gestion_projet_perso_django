function togglePassword() {
    var passwordField = document.getElementById("password");
    var icon = document.querySelector(".toggle-password");

    if (passwordField.type === "password") {
      passwordField.type = "text";
      icon.classList.remove("fa-eye");
      icon.classList.add("fa-eye-slash");
    } else {
      passwordField.type = "password";
      icon.classList.remove("fa-eye-slash");
      icon.classList.add("fa-eye");
    }
}

[...document.querySelectorAll('li')].forEach(li =>
  li.addEventListener('click', e => (e.stopPropagation(), li.classList.toggle('done')))
);

$(document).ready(function () {
    $('#addProjectForm').submit(function (e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/',
            data: $(this).serialize(),
            success: function (data) {
                if (data.status === 'success') {
                    $('#addProjectModal').modal('hide');
                } else if (data.status === 'error') {
                    console.log(data.errors);
                }
            }
        });
    });
});