import { Component } from '@angular/core';

@Component({
  selector: 'ham-root',
  template: `
    <div class="content">
      <router-outlet></router-outlet>
    </div>`,
  styles: [],
})
export class AppComponent {
  title = 'covid-angular';
}
