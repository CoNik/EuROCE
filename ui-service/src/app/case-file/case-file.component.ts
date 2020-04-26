import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-case-file',
  templateUrl: './case-file.component.html',
  styleUrls: ['./case-file.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class CaseFileComponent implements OnInit {
  settings =   {
    "columns": {
      "ips": {
        "title": "IPs"
      },
      "serviceTypes": {
        "title": "Service Types"
      },
      "ports": {
        "title": "Ports"
      },
      "services": {
        "title": "Services"
      }
    },
    "delete": {
      "confirmDelete": true
    },
    "add": {
      "confirmCreate": true
    },
    "edit": {
      "confirmSave": true
    },
    "actions": {
      "add": true,
      "edit": true,
      "delete": true
    },
    "mode": "internal"
  };
  source =   [
    {
      "ips": 1,
      "serviceTypes": "Danielle Kennedy",
      "ports": "danielle.kennedy",
      "services": "danielle_91@example.com"
    },
    {
      "ips": 2,
      "serviceTypes": "Russell Payne",
      "ports": "russell.payne",
      "services": "russell_88@example.com"
    },
    {
      "ips": 3,
      "serviceTypes": "Brenda Hanson",
      "ports": "brenda.hanson",
      "services": "brenda97@example.com"
    },
    {
      "ips": 4,
      "serviceTypes": "Nathan Knight",
      "ports": "nathan.knight",
      "services": "nathan-85@example.com"
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
