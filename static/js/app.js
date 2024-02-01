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
    $('input[type="checkbox"]').change(function () {
        var tacheId = $(this).closest('form').data('tache-id');
        var isChecked = $(this).prop('checked');

        $.ajax({
            url: '/projects/update_tache/' + tacheId + '/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                checked: isChecked ? 'true' : 'false'
            },
            success: function (data) {
                console.log('Tâche mise à jour avec succès!');
            },
            error: function (error) {
                // Gérez les erreurs
                console.error('Erreur lors de la mise à jour de la tâche:', error);
            }
        });
    });
});