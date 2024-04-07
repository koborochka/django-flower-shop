let filtersButton = document.querySelector('.personal-cabinet__button-filters');
let filtersList = document.querySelector('.category-header__dropdown-filters');
filtersButton.onclick = function() {
    filtersList.classList.toggle('visually-hidden');
    filtersList.classList.toggle('visually-shown');
};