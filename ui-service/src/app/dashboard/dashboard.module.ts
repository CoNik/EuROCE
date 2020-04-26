import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardRoutingModule } from './dashboard-routing.module';
import { DashboardComponent } from './dashboard.component';
import { StatusTableComponent } from './status-table/status-table.component';
import { BookingsComponent } from './bookings/bookings.component';
import { ArrivingComponent } from './arriving/arriving.component';
import { TableComponent } from './table/table.component';
import { StatusCardComponent } from './status-card/status-card.component';
import { Space28Component } from './space28/space28.component';
import { StatusCard1Component } from './status-card1/status-card1.component';
import { Space32Component } from './space32/space32.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [DashboardComponent, StatusTableComponent, BookingsComponent, ArrivingComponent, TableComponent, StatusCardComponent, Space28Component, StatusCard1Component, Space32Component],
  imports: [
    CommonModule,
    DashboardRoutingModule,
    SharedModule
  ]
})
export class DashboardModule { }
