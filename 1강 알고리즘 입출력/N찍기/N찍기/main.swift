//
//  main.swift
//  N찍기
//
//  Created by 최원석 on 2020/11/23.
//

import Foundation

let value = readLine()
if let changeValue = Int(value ?? "0") {
    for i in 0..<changeValue {
        print(i)
    }
}

