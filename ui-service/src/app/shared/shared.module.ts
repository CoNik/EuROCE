import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
    NbCardModule,
    NbIconModule,
    NbTooltipModule,
    NbButtonModule,
    NbCheckboxModule,
    NbInputModule,
    NbTabsetModule, NbAccordionModule,
} from '@nebular/theme';
import { MultipleBarChartComponent } from './components/multiple-bar-chart.component';
import { EchartsDirective } from './directives/echarts.directive';
import { NgxEchartsModule } from 'ngx-echarts';
import { MapComponent } from './components/map.component';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import { SmartTableComponent } from './components/smart-table.component';
import { Ng2SmartTableModule } from 'ng2-smart-table';

@NgModule({
    declarations: [MultipleBarChartComponent, EchartsDirective, MapComponent, SmartTableComponent],
    imports: [
        CommonModule,
        NbCardModule,
        NgxEchartsModule,
        NbTabsetModule,
        NbIconModule,
        NbTooltipModule,
        NbButtonModule,
        NbCheckboxModule,
        NbTabsetModule,
        NbAccordionModule,
        NbInputModule,
        LeafletModule,
        Ng2SmartTableModule,
    ],
    exports: [NbCardModule, MultipleBarChartComponent, EchartsDirective, NgxEchartsModule, NbIconModule, NbTooltipModule, NbButtonModule,
        NbCheckboxModule, NbTabsetModule, NbAccordionModule, NbInputModule, MapComponent, LeafletModule, SmartTableComponent,
        Ng2SmartTableModule],
})
export class SharedModule {
}
