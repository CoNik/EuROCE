import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-bookings',
  templateUrl: './bookings.component.html',
  styleUrls: ['./bookings.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class BookingsComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
