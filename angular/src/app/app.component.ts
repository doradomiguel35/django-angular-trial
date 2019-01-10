import { Component } from '@angular/core';
import { ServeMovieService } from './serve-movie.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ServeMovieService]
})
export class AppComponent {
  title = 'angular';
  movies;

  constructor(private api: ServeMovieService) {
  	this.getMovies();
  }

  getMovies = () => {
  	this.api.getAllMovies().subscribe(
  		data => {
  			this.movies = data;
  		},
  		error => {
  			console.log(error);
  		}
  	);
  }
}
