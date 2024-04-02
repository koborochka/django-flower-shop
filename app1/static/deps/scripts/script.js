let personalCabinetButton = document.querySelector('.personal-cabinet__button');
let personalCabinetMenu = document.querySelector('.main-navigation__dropdown-menu');
personalCabinetButton.onclick = function() {
    console.log("d4lr")
    personalCabinetMenu.classList.toggle('visually-hidden');
    personalCabinetMenu.classList.toggle('visually-shown');

};
