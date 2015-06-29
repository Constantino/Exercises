function validateEmail(email) {
	var regex_email = /^\w+([\.-]?\w+)*@\w+([a-z0-9]?\w+)*(\.\w{2,20})+$/

	alert(regex_email.test(email));

}