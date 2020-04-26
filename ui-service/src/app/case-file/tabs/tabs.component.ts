import { Component, OnInit, ChangeDetectionStrategy } from '@angular/core';

@Component({
  selector: 'app-tabs',
  templateUrl: './tabs.component.html',
  styleUrls: ['./tabs.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TabsComponent implements OnInit {
  settings =   {
    "columns": {
      "id": {
        "title": "ID",
        "filter": true
      },
      "contentText": {
        "title": "Content Text"
      },
      "weblink": {
        "title": "Weblink"
      },
      "authorHandler": {
        "title": "Author Handler"
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
      "id": 1,
      "contentText": "Danielle Kennedy",
      "weblink": "danielle.kennedy",
      "authorHandler": "danielle_91@example.com"
    },
    {
      "id": 2,
      "contentText": "Russell Payne",
      "weblink": "russell.payne",
      "authorHandler": "russell_88@example.com"
    },
    {
      "id": 3,
      "contentText": "Brenda Hanson",
      "weblink": "brenda.hanson",
      "authorHandler": "brenda97@example.com"
    },
    {
      "id": 4,
      "contentText": "Nathan Knight",
      "weblink": "nathan.knight",
      "authorHandler": "nathan-85@example.com"
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
