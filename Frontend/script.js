// Modal and Auth Elements
const authModal = document.getElementById("authModal");
const getStartedBtns = document.querySelectorAll(".getStartedBtn, #getStartedBtn");
const closeModalBtn = document.getElementById("closeModal");
const loginLink = document.getElementById("loginLink");
const formTitle = document.getElementById("formTitle");
const authForm = document.getElementById("authForm");

// Hide "Get Started" buttons if user is logged in
if(localStorage.getItem("user")){
  getStartedBtns.forEach(btn => btn.style.display = "none");
}

// Open modal (Sign Up default)
getStartedBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    authModal.classList.remove("hidden");
    formTitle.textContent = "Sign Up";
    renderForm("signup");
  });
});

// Close modal
closeModalBtn.addEventListener("click", () => authModal.classList.add("hidden"));

// Switch form
if(loginLink){
  loginLink.addEventListener("click", e => {
    e.preventDefault();
    if(formTitle.textContent === "Sign Up") renderForm("login");
    else renderForm("signup");
  });
}

// Render form fields dynamically
function renderForm(mode){
  if(mode === "signup"){
    formTitle.textContent = "Sign Up";
    authForm.innerHTML = `
      <input type="text" id="username" placeholder="Username" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
      <input type="email" id="email" placeholder="Email" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
      <input type="password" id="password" placeholder="Password" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
      <button type="submit" class="gradient-btn py-2 rounded-lg font-bold mt-2">Register</button>
    `;
    if(loginLink) loginLink.textContent = "Log In";
  } else {
    formTitle.textContent = "Log In";
    authForm.innerHTML = `
      <input type="text" id="username" placeholder="Username" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
      <input type="password" id="password" placeholder="Password" class="p-2 rounded bg-[#211c27] border border-[#473b54]" required />
      <button type="submit" class="gradient-btn py-2 rounded-lg font-bold mt-2">Login</button>
    `;
    if(loginLink) loginLink.textContent = "Sign Up";
  }
}

// Handle form submission
authForm.addEventListener("submit", async e => {
  e.preventDefault();
  const isLogin = formTitle.textContent === "Log In";
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const email = !isLogin ? document.getElementById("email").value.trim() : undefined;

  try {
    const endpoint = isLogin ? "/login" : "/register";
    const res = await fetch(`http://127.0.0.1:8000${endpoint}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(isLogin ? { username, password } : { username, email, password })
    });

    const data = await res.json();

    if(res.ok){
      alert(data.message || "Success!");
      // Store user locally (for demo, store username/email)
      localStorage.setItem("user", JSON.stringify({ username, email }));
      authModal.classList.add("hidden");
      getStartedBtns.forEach(btn => btn.style.display = "none");
    } else {
      alert(data.detail || "Error occurred");
    }
  } catch(err){
    console.error(err);
    alert("Network error. Make sure your backend is running on localhost:8000");
  }
});
