import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DashboardComponent implements OnInit {
  data =   [
    {
      "name": "First Dataset",
      "data": [
        [
          "January",
          -80
        ],
        [
          "February",
          30
        ],
        [
          "March",
          -43
        ],
        [
          "April",
          19
        ],
        [
          "May",
          -24
        ],
        [
          "June",
          -59
        ],
        [
          "July",
          50
        ]
      ]
    },
    {
      "name": "Second Dataset",
      "data": [
        [
          "January",
          -60
        ],
        [
          "February",
          -2
        ],
        [
          "March",
          -6
        ],
        [
          "April",
          7
        ],
        [
          "May",
          44
        ],
        [
          "June",
          -34
        ],
        [
          "July",
          -56
        ]
      ]
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
