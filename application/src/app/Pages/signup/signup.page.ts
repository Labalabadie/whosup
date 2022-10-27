import { Component, OnInit } from '@angular/core';
import {ErrorStateMatcher} from '@angular/material/core';
import {FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators} from '@angular/forms';
import {AuthService} from '../../Data(services)/auth.services';
import {Router} from '@angular/router';

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-register',
  templateUrl: './signup.page.html',
  styleUrls: ['./signup.page.scss']
})
export class SignupPage implements OnInit {

  registerForm: FormGroup;
  name = '';
  email = '';
  phone = '';
  password = '';
  checkpassword = '';
  isLoadingResults = false;
  matcher = new MyErrorStateMatcher();

  constructor(private authService: AuthService, private router: Router, private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      username : [null, Validators.required],
      email : [null, Validators.required],
      phone : [null, Validators.required],
      password : [null, Validators.required],
      checkpassword : [null, Validators.required]
      
    });
  }

  onFormSubmit(): void {
    this.isLoadingResults = true;
    this.authService.register(this.registerForm.value)
      .subscribe((res: any) => {
        this.isLoadingResults = false;
        this.router.navigate(['/login']).then(_ => console.log('You are registered now!'));
      }, (err: any) => {
        console.log(err);
        this.isLoadingResults = false;
      });
  }

}

 /* async Name(){
	  if(this.signupUser.name == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async Mail(){
	  if(this.signupUser.mail == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async Phone(){
	  if(this.signupUser.phone == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async Password(){
	  if(this.signupUser.password == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
  async checkPassword(){
	  if(this.signupUser.checkpassword == null){
		const alert = await this.alertController.create({
			header: 'Datos incompletos',
			message: 'Tienes que llenar todos los datos',
			buttons: ['Aceptar']
		  });

		  await alert.present();
	  }
  }
    async save(signupForm: NgForm){

      console.log(signupForm);
        if(signupForm.invalid){
          const alert = await this.alertController.create({
            header: 'Datos incompletos',
            message: 'Tienes que llenar todos los datos',
            buttons: ['Aceptar']
          });
    
          await alert.present();
          return;
        }
    
        const user = {
        name: signupForm.value.name,
        mail: signupForm.value.mail,
        phone: signupForm.value.phone,
        password: signupForm.value.password,
        checkpassword: signupForm.value.checkpassword
        };
    
      const key = 'user';
        Storage.set({ key, value: JSON.stringify(user) });
    
      const key2 = 'ingresado';
      const value = 'true';
      Storage.set({ key: key2, value });
        this.navCtrl.navigateRoot('home');
      }

     */ 
