function show_reply_form(id) {
    const reply_form = document.getElementById("reply-form-" + id);
    if (reply_form.style.display === "none") {
        reply_form.style.display = "block";
    } else {
        reply_form.style.display = "none";
    }
}