export class Signup {
	id?: string;
	name?: string;
	mail?: string;
	phone?: string;
	password?: string;
	checkpassword?: string;


	constructor(){
		this.name = null;
		this.mail = null;
		this.phone = null;
		this.password = null;
		this.checkpassword = null;
	}
}