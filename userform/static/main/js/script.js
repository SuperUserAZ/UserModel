const MainLogBtn = document.querySelector('#main-log-btn');
const MainSignBtn = document.querySelector('#main-sign-btn');
const LogBtn = document.querySelector('#log-btn');
const SignBtn = document.querySelector('#sign-btn');

function ShowMainPage() {
    document.location.assign('');
}

function ShowLoginPage() {
    document.location.assign('login');
}
function ShowSignUpPage() {
    document.location.assign('signup');
}

function ShowProfilePage() {
    document.location.assign('profile');
}
if (MainLogBtn) {
    MainLogBtn.onclick = ShowLoginPage;
}

if (MainSignBtn) {
    MainSignBtn.onclick = ShowSignUpPage;
}
else if (LogBtn) {
    LogBtn.onclick = ShowMainPage;
}
else if (SignBtn) {
    LogBtn.onclick = ShowProfilePage;
}

