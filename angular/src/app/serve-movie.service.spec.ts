import { TestBed } from '@angular/core/testing';

import { ServeMovieService } from './serve-movie.service';

describe('ServeMovieService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ServeMovieService = TestBed.get(ServeMovieService);
    expect(service).toBeTruthy();
  });
});
