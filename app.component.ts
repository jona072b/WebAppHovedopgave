import { Component, Input, Output, EventEmitter } from '@angular/core';
import { APIService } from './Services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'UploadWebApp';
  weatherFile: any;
  absenseFile: any;


  constructor(private apiService: APIService) {}

  uploadFile() {
    confirm('Er du sikker på at du vil uploade disse filer?'); {


      const weatherFileReader = new FileReader();
      const absenseFileReader = new FileReader();


       weatherFileReader.onload = (e) => {
          const dataFromWeatherFile = weatherFileReader.result.toString();
          // console.log(dataFromWeatherFile);
          this.apiService.sendWeather(dataFromWeatherFile);
       };
       absenseFileReader.onload = (e) => {
        const dataFromAbsenseFile = absenseFileReader.result.toString();
        this.apiService.sendAbsense(dataFromAbsenseFile);
       };
      weatherFileReader.readAsText(this.weatherFile);
      absenseFileReader.readAsText(this.absenseFile);

    }
  }

  weatherFileChanged(e) {
    this.weatherFile = e.target.files[0];
  }

  absenseFileChanged(e) {
    this.absenseFile = e.target.files[0];
  }

  test() {
    this.apiService.sendTest();
  }


}


