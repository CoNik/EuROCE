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
      "vulnerabilityScans": {
        "title": "Vulnerability Scans"
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
      "serviceTypes": "N/A",
      "ports": "N/A",
      "vulnerabilityScans": "N/A"
    },
    {
      "ips": 2,
      "serviceTypes": "N/A",
      "ports": "N/A",
      "vulnerabilityScans": "N/A"
    },
    {
      "ips": 3,
      "serviceTypes": "N/A",
      "ports": "N/A",
      "vulnerabilityScans": "N/A"
    },
    {
      "ips": 4,
      "serviceTypes": "N/A",
      "ports": "N/A",
      "vulnerabilityScans": "N/A"
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
