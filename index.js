let rm_copy_notif = () => {
    let copy_notif = document.querySelector(".copy-notif");
    if (!copy_notif) return;

    copy_notif.remove();
}

// make email clickable
document.addEventListener("DOMContentLoaded", () => {
    let mail_link = document.querySelector("#email-link");
    if (!mail_link) return;

    mail_link.addEventListener("click", (e) => {
        navigator.clipboard.writeText("s.rhee@nyu.edu");

        let copy_notif = document.createElement("div");
        copy_notif.classList.add("copy-notif");
        let copy_text = document.createTextNode("copied!");
        copy_notif.style.top = (e.clientY - 16).toString() + "px";
        copy_notif.style.left = e.clientX.toString() + "px";
        copy_notif.appendChild(copy_text);
        document.body.appendChild(copy_notif);
        setTimeout(rm_copy_notif, 500);
    });
})
