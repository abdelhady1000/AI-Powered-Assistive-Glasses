// ===== AUTHENTICATION LOGIC =====

// Elements
const getStartedBtns = [
    document.getElementById('getStartedBtn'),
    document.getElementById('getStartedBtnNav'),
    document.getElementById('getStartedBtnHero')
].filter(btn => btn !== null);

const authModal = document.getElementById('authModal');
const closeModal = document.getElementById('closeModal');
const authForm = document.getElementById('authForm');
const formTitle = document.getElementById('formTitle');
const loginLink = document.getElementById('loginLink') || document.getElementById('switchToLogin');

// Backend URL
const API_URL = "http://127.0.0.1:8000"; // Change if backend is hosted elsewhere

// Check if user is logged in
let user = JSON.parse(localStorage.getItem('user'));
if(user){
    getStartedBtns.forEach(btn => btn.style.display = 'none');
    createLogoutButton();
}

// Show modal
function showModal() {
    authModal.classList.remove('hidden');
    showLoginForm(); // default to login form
}

// Hide modal
function hideModal() {
    authModal.classList.add('hidden');
}

// Show Register Form
function showRegisterForm() {
    formTitle.textContent = 'Register';
    authForm.innerHTML = `
        <input type="text" id="username" placeholder="Username" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
        <input type="email" id="email" placeholder="Email" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
        <input type="password" id="password" placeholder="Password" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
        <button type="submit" id="authSubmit" class="gradient-btn py-2 rounded-lg font-bold mt-2">Register</button>
    `;
    if(loginLink) loginLink.textContent = 'Already have an account? Login';
}

// Show Login Form
function showLoginForm() {
    formTitle.textContent = 'Login';
    authForm.innerHTML = `
        <input type="text" id="loginUsername" placeholder="Username" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
        <input type="password" id="loginPassword" placeholder="Password" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
        <button type="submit" id="authSubmit" class="gradient-btn py-2 rounded-lg font-bold mt-2">Login</button>
    `;
    if(loginLink) loginLink.textContent = "Don't have an account? Register";
}

// Open modal on button click
getStartedBtns.forEach(btn => {
    btn.addEventListener('click', showModal);
});

// Close modal
if(closeModal) closeModal.addEventListener('click', hideModal);

// Switch form
if(loginLink){
    loginLink.addEventListener('click', e => {
        e.preventDefault();
        if(formTitle.textContent === 'Register') showLoginForm();
        else showRegisterForm();
    });
}

// Handle form submit
if(authForm){
    authForm.addEventListener('submit', async e => {
        e.preventDefault();

        try {
            if(formTitle.textContent === 'Register'){
                // Get values
                const username = document.getElementById('username').value.trim();
                const email = document.getElementById('email').value.trim();
                const password = document.getElementById('password').value.trim();

                // Call backend
                const res = await fetch(`${API_URL}/register`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({username, email, password})
                });
                const data = await res.json();

                if(res.ok){
                    alert('Registered successfully!');
                    localStorage.setItem('user', JSON.stringify({username, email}));
                    hideModal();
                    getStartedBtns.forEach(btn => btn.style.display = 'none');
                    createLogoutButton();
                } else {
                    alert(data.detail || 'Registration failed');
                }

            } else {
                // Login
                const username = document.getElementById('loginUsername').value.trim();
                const password = document.getElementById('loginPassword').value.trim();

                const res = await fetch(`${API_URL}/login`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({username, password})
                });
                const data = await res.json();

                if(res.ok){
                    alert(data.message);
                    localStorage.setItem('user', JSON.stringify({username}));
                    hideModal();
                    getStartedBtns.forEach(btn => btn.style.display = 'none');
                    createLogoutButton();
                } else {
                    alert(data.detail || 'Login failed');
                }
            }
        } catch(err) {
            console.error(err);
            alert('Something went wrong. Please try again.');
        }
    });
}

// ===== LOGOUT BUTTON =====
function createLogoutButton(){
    if(document.getElementById('logoutBtn')) return;

    const navbar = document.querySelector('header');
    if(!navbar) return;

    const logoutBtn = document.createElement('button');
    logoutBtn.id = 'logoutBtn';
    logoutBtn.textContent = 'Logout';
    logoutBtn.className = 'gradient-btn px-4 py-2 rounded-lg font-bold ml-4';

    const lastGetStartedBtn = getStartedBtns[getStartedBtns.length - 1];
    if(lastGetStartedBtn && lastGetStartedBtn.parentNode === navbar){
        lastGetStartedBtn.insertAdjacentElement('afterend', logoutBtn);
    } else {
        navbar.appendChild(logoutBtn);
    }

    logoutBtn.addEventListener('click', () => {
        localStorage.removeItem('user');
        user = null;
        getStartedBtns.forEach(btn => btn.style.display = 'inline-block');
        logoutBtn.remove();
        alert('Logged out!');
    });
}
