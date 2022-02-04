const MainLogBtn = document.querySelector('#main-log-btn');
const MainSignBtn = document.querySelector('#main-sign-btn');

function ShowLoginPage() {
    document.location.assign('login');
}

function ShowSignUpPage() {
    document.location.assign('signup');
}

MainLogBtn.onclick = ShowLoginPage;
MainSignBtn.onclick = ShowSignUpPage;