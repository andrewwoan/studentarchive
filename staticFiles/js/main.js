window.addEventListener("scroll", () => {
    let navbar = document.getElementsByClassName("header")[0];
    navbar.classList.toggle("sticky", scrollY > 0);
});
