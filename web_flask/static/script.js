//interactive logic


function openModal(modalId) {
	var modal = document.getElementById(modalId);
	modal.style.display = 'block';
}

function closeModal(modalId) {
	var modal = document.getElementById(modalId);
	modal.style.display = 'none';
}


function openSignUp(userType) {
	openModal('signUpModal');
}


function openSignIn(userType) {
	openModal('signInModal');
}


function openBookService() {
	openModal('bookServiceModal');
}


function signIn() {
	// logic to handle sign-in
	closeModal('signInModal');
}

function signUp() {
	//logic to handle sign-up
	closeModal('signUpModal');
}


function bookService() {
	//logic to handle booking service
	closeModal('bookServiceModal');
}


//Add similar functions for company sign in, sign up, and accepgbooking
