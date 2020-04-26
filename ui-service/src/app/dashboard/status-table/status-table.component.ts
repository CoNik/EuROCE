import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-status-table',
  templateUrl: './status-table.component.html',
  styleUrls: ['./status-table.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StatusTableComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
