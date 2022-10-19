import { Component, OnInit , NgZone} from '@angular/core';
import { UserCrudService } from '../../Data(services)/userCrud.services';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder } from "@angular/forms";

@Component({
  selector: 'app-signup',
  templateUrl: './signup.page.html',
  styleUrls: ['./signup.page.scss'],
})
export class SignupPage implements OnInit {

  userForm: FormGroup;


    constructor(
      private router: Router,
      public formBuilder: FormBuilder,
      private zone: NgZone,
      private userCrudService: UserCrudService    
    ) {
      this.userForm = this.formBuilder.group({
        id: 0,
        name: [''],
        phone: [],
        email: [''],
        password: [''],
        checkpassword: [''],
				created_at: [''],
				updated_at: ['']
      })
    }


  ngOnInit() {
  }
  onSubmit() {
    if (!this.userForm.valid) {
      return false;
    } else {
      this.userCrudService.createUser(this.userForm.value)
        .subscribe((response) => {
          this.zone.run(() => {
            this.userForm.reset();
            this.router.navigate(['/home']);
          })
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
    }
