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


function openSignUp(garbage_collection_companyType){
	openModal('signUpModal');
}

function openSignInModal(garbage_collection_companyType){
	openModal('signInModal');
}

function openAcceptBook(){
	openModal('acceptBookModal');
}

function SignIn(){
	//logic to handle sign-in.
	closeModal('SignInModal');
}

function SignUp(){
	//logic to handle sign-up.
	closeModal('SignUpModal');
}

function acceptBook(){
	//logic to handle accepting bookings.
	closeModal('acceptBookModal');
}
