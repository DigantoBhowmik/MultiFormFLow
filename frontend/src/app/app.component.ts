import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CreateUserDto, UserDto, UserService } from './services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  step = 1;
  form: FormGroup = new FormGroup({});
  instraFile: File = new File([], '');
  ytFile: File = new File([], '');
  ytcFile: File = new File([], '');
  user = {} as UserDto;
  public isNextClicked: boolean = false;

  isSubmitting = false;

  isInstraFileError = false;
  isYtFileError = false;
  isYtcFileError = false;
  errorMessage = '';

  isalreadyFillup = false;

  constructor(private fb: FormBuilder,
    private userService: UserService
    ) {
  }

  ngOnInit() {
    this.buildForm();
  }

  showStep(step: number) {
    this.step = step;
    // if(step == 2){
    //   this.userService.getUser(this.form.value.email).subscribe(x => {
    //     this.user = x as UserDto;
    //     console.log(this.user);
    //   });
    // }
    this.onSubmit();
  }

  onFileSelected(event: any, type: string) {
    if (type == 'instra') {
      this.instraFile = event.target.files[0];
      this.isInstraFileError = false;
      this.user.is_instra_ss = true;
      this.errorMessage = '';
    }
    if (type == 'ytc') {
      this.ytcFile = event.target.files[0];
      this.isYtcFileError = false;
      this.user.is_ytc_ss = true;
    }
  }

  buildForm() {
    this.form = this.fb.group({
      email: [this.user.email || '',[Validators.email, Validators.pattern('[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$'), Validators.required]],
      youtubeUserName: [this.user.yt_username || '', Validators.required],
      youtubeUrl: [this.user.yt_url || '', [Validators.required, Validators.pattern('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')]],
    });
  }

  get validData() { return this.form.controls; }

  back(){
    this.step--;
    this.instraFile = new File([], '');
    this.ytFile = new File([], '');
    this.ytcFile= new File([], '');
    this.isInstraFileError = false;
    this.isYtFileError = false;
    this.isYtcFileError = false;
    this.errorMessage = '';
  }

  onSubmit() {
    this.isNextClicked = true;
    if (this.validData['youtubeUserName'].valid && this.step == 3 ){
      this.errorMessage = '';
    }
    if(this.errorMessage != ''){
      return
    }
    if (this.validData['email'].invalid && this.step == 1) {
      return;
    }
    if (this.validData['youtubeUserName'].invalid && this.step == 3 && !this.user.yt_username) {
      return;
    }
    if (this.validData['youtubeUrl'].invalid && this.step == 5) {
      return;
    }
    if (!this.user.is_instra_ss && this.step == 2) {
      this.isInstraFileError = true;
      return;
    }
    if (!this.user.is_ytc_ss && this.step == 4) {
      this.isYtcFileError = true;
      return;
    }
    
    let object: CreateUserDto = {
      email: this.form.value.email,
      instraFile: this.instraFile,
      ytUsername: this.form.value.youtubeUserName,
      ytcFile: this.ytcFile,
      ytUrl: this.form.value.youtubeUrl
    }
    this.isSubmitting = true;
    this.userService.createUser(object).subscribe(result => {
      this.user = result as UserDto;
      let incresedStep = 1;
      if(this.step == 1){
        if(this.user.is_instra_ss){
          incresedStep++;
        }
        if(this.user.yt_username != null){
          incresedStep++;
        }
        if(this.user.is_ytc_ss){
          incresedStep++;
        }
        if(this.user.yt_url != null){
          this.isalreadyFillup = true;
          incresedStep++;
        }
      }
      this.step += incresedStep ;
      this.isNextClicked = false;
      this.instraFile = new File([], '');
      this.ytFile = new File([], '');
      this.ytcFile= new File([], '');
      this.buildForm();
      this.isSubmitting = false;
    }, error => {
      this.isSubmitting = false;
      this.isNextClicked = false;
      console.log(error.error['message'])
      alert(error.error['message']);
      this.errorMessage = error.error['message'];
      }
    );
  }
  
  resetForm() {
    this.form.reset();
  }
}

