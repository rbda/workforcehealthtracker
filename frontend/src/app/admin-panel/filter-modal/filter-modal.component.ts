/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 *  Built and managed with Open Source Love by BeeHyv Software Solutions Pvt Ltd. Hyderabad
 *  www.beehyv.com
 */

import {AfterViewInit, ChangeDetectorRef, Component, EventEmitter, Inject, OnInit, QueryList, ViewChildren} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';
import {ENGLISH_CONSTANT} from '../../utils/language/english';
import {Options} from 'ng5-slider';
import {FormControl} from '@angular/forms';
import {Filter} from '../../utils/response';

@Component({
  selector: 'app-filter-modal',
  templateUrl: './filter-modal.component.html',
  styleUrls: ['./filter-modal.component.scss']
})
export class FilterModalComponent implements OnInit, AfterViewInit {
  language = ENGLISH_CONSTANT;
  groups = [];
  resultStatus = [];
  isImmunodeficiency = '';
  isChronicIllness = '';
  value: number = 30;
  highValue: number = 70;
  options: Options = {
    floor: 18,
    ceil: 120,
    step: 5,
    showTicks: true
  };
  isMobile = false;
  filter: Filter = new Filter();
  groupCtrl = new FormControl();
  statusCtrl = new FormControl();
  // testing slider issue
  manualRefresh: EventEmitter<void> = new EventEmitter<void>();
  @ViewChildren('slider') sliders: QueryList<any>;

  constructor(private dialogRef: MatDialogRef<FilterModalComponent>,
              @Inject(MAT_DIALOG_DATA) data, private changeDetRef: ChangeDetectorRef) {
    this.resultStatus = data.result_status;
    this.language = data.language;
    this.groups = data.groups;
    this.isMobile = data.isMobile;
  }

  ngOnInit(): void {
    // setTimeout(() => {
    //   this.manualRefresh.emit();
    //   this.changeDetRef.detectChanges();
    // });
  }
  ngAfterViewInit(): void {
    setTimeout(() => {
      this.manualRefresh.emit();
      this.changeDetRef.detectChanges();
    }, 400);
  }
  // ngAfterViewInit() {
  //   this.sliders.forEach(slider => {
  //     slider.init();
  //     slider.init = () => {};
  //   });
  //   this.changeDetRef.detectChanges();
  // }

  cancel(){
    this.dialogRef.close('cancel');
  }
  submitDetails(){
    this.filter.group = this.groupCtrl?.value?.toString();
    this.filter.result_status = this.statusCtrl.value;
    this.filter.isChronicIllness = this.isChronicIllness;
    this.filter.isImmunodeficiency = this.isImmunodeficiency;
    this.filter.min_age = this.value;
    this.filter.max_age = this.highValue;
    this.dialogRef.close(this.filter);
  }

}
