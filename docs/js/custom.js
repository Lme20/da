document.addEventListener("DOMContentLoaded", function() {
    const activeLink = document.querySelector('.md-nav__link--active');
    if (activeLink) {
        let parent = activeLink.parentElement;
        while (parent && !parent.classList.contains('md-sidebar--primary')) {
            if (parent.classList.contains('md-nav__item')) {
                parent.classList.add('md-nav__item--open');
            }
            parent = parent.parentElement;
        }
    }
});