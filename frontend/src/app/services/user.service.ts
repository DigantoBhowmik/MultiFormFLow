import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { CreateUserDto } from "./user.model";

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private headers: HttpHeaders;
  private baseUrl: string = environment.apiUrl + "/user";

  constructor(private http: HttpClient) {
    this.headers = new HttpHeaders({
      "Content-Type": "application/json; charset=utf-8",
    });
  }

  public getUser(email: string) {
    return this.http.get(this.baseUrl + "/get/" + email + "/");
  }

  public createUser(data: CreateUserDto) {
    const formData = new FormData();
    for (const prop in data) {
      if (!data.hasOwnProperty(prop)) {
        continue;
      }
      formData.append(prop, data[prop]);
    }
    return this.http.post(this.baseUrl + "/create/", formData, {
      headers: new HttpHeaders({
        "Accept": "application/json",
      }),
    });
  }
}
