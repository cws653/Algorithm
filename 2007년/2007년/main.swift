//
//  main.swift
//  2007년
//
//  Created by 최원석 on 2020/11/23.
//

import Foundation

let line = readLine() ?? ""
let lineArr = line.split(separator: " ")
let x = Int(lineArr[0]) ?? 0
let y = Int(lineArr[1]) ?? 0
var diffDays = 0;

for index in 1..<x {
    if [1, 3, 5, 7, 8, 10, 12].contains(index) {
        diffDays += 31
    }
    if [4, 6, 9, 11].contains(index) {
        diffDays += 30
    }
    if index == 2 {
        diffDays += 28
    }
}

diffDays += y-1

switch (diffDays % 7) {
case 0: print("MON")
case 1: print("TUE")
case 2: print("WED")
case 3: print("THU")
case 4: print("FRI")
case 5: print("SAT")
case 6: print("SUN")
default: break
}
