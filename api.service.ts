import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class APIService {

  url = 'http://127.0.0.1:5000/';

  constructor(private http: HttpClient) { }

  sendAbsense(absenseFile) {
    // const weatherFileReader = new FileReader();
    // weatherFileReader.readAsText(weatherFile);
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Access-Control-Allow-Origin': '*'
      })
    };
    const document = new HttpParams().set('document', absenseFile);
    // const data = new HttpParams().set('data', 'data');
    this.http.post(this.url + 'newAbsense', JSON.stringify(document), httpOptions).subscribe(res => {
      console.log('response from server: ' + res['Response']);
    });
  }

  sendWeather(weatherFile) {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Access-Control-Allow-Origin': '*'
      })
    };
    const document = new HttpParams().set('document', weatherFile);
    // const data = new HttpParams().set('data', 'data');
    this.http.post(this.url + 'newWeather', JSON.stringify(document), httpOptions).subscribe(res => {
      console.log('response from server: ' + res['Response']);
    });
  }

  sendTest() {
    this.http.get(this.url + 'test').subscribe(res => {
      console.log('Response from server: ' + res['TEST']);
    });
  }
}
