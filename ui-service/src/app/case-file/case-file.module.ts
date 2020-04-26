import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CaseFileRoutingModule } from './case-file-routing.module';
import { CaseFileComponent } from './case-file.component';
import { StatusCard2Component } from './status-card2/status-card2.component';
import { Space23Component } from './space23/space23.component';
import { Table1Component } from './table1/table1.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [CaseFileComponent, StatusCard2Component, Space23Component, Table1Component],
  imports: [
    CommonModule,
    CaseFileRoutingModule,
    SharedModule
  ]
})
export class CaseFileModule { }
