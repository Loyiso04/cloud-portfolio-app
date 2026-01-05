let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar'); 
let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height){
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active')
            })
        }
    })
}

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}


document.getElementById("contactBtn").addEventListener("click", function (e) {
    e.preventDefault();

    const contactSection = document.getElementById("contact");

    contactSection.scrollIntoView({
        behavior: "smooth",
        block: "start"

    });

    contactSection.classList.add("highlight");

    setTimeout(() => {
        contactSection.classList.remove("highlight");
    }, 1200);
});

document.getElementById("hireBtn").addEventListener("click", function (e) {
    e.preventDefault();

    window.location.href = "mailto:loyisokhumalo38@outlook.com?subject=Hiring%20Inquiry";
});

  const flash = document.getElementById("flash-message");

  if (flash && flash.dataset.scroll === "true") {
    document.getElementById("contact").scrollIntoView({
      behavior: "smooth"
    });
  }

  setTimeout(() => {
    if (flash) {
      flash.style.transition = "opacity 1s ease";
      flash.style.opacity = "0";
      setTimeout(() => flash.remove(), 1000);
    }
  }, 30000);
