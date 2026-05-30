function toggleMenu() {
    let menu = document.getElementById("dropdown");

    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

// ESC bosilganda yopish
document.addEventListener("keydown", function(e) {
    if (e.key === "Escape") {
        document.getElementById("dropdown").style.display = "none";
    }
});

// CLICK OUTSIDE yopish
document.addEventListener("click", function(e) {
    let box = document.querySelector(".user-box");
    let menu = document.getElementById("dropdown");

    if (!box.contains(e.target)) {
        menu.style.display = "none";
    }
});