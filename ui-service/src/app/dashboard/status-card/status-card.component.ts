import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-status-card',
  templateUrl: './status-card.component.html',
  styleUrls: ['./status-card.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
// card with the user name and profil
export class StatusCardComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
