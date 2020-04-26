import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-status-card1',
  templateUrl: './status-card1.component.html',
  styleUrls: ['./status-card1.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StatusCard1Component implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
