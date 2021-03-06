import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CaseFileComponent } from './case-file.component';

const routes: Routes = [
  { path: '', component: CaseFileComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CaseFileRoutingModule { }
