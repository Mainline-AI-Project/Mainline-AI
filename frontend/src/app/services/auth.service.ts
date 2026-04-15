import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private API = 'http://localhost:8000/api/users';
  private TOKEN_KEY = 'token';
  private USER_KEY = 'user';

  constructor(private http: HttpClient, private router: Router) {}

//   signup(data: any) {
//     return this.http.post<any>(`${this.API}/signup/`, data);
//   }

//   login(data: any) {
//     return this.http.post<any>(`${this.API}/login/`, data);
//   }

signup(data: any) {
  return this.http.post<any>(`http://localhost:8000/api/users/signup/`, data);
}

login(data: any) {
  return this.http.post<any>(`http://localhost:8000/api/users/login/`, data);
}


  setSession(response: any) {
    localStorage.setItem(this.TOKEN_KEY, response.token);
    localStorage.setItem(this.USER_KEY, JSON.stringify(response.user));
  }

  getUser() {
    return JSON.parse(localStorage.getItem(this.USER_KEY) || '{}');
  }

  isAuthenticated(): boolean {
    return !!localStorage.getItem(this.TOKEN_KEY);
  }

  logout() {
    localStorage.clear();
    this.router.navigate(['/']);
  }

  googleLogin(token: string) {
  return this.http.post<any>('http://127.0.0.1:8000/api/google-auth/', { token });
  }

}
