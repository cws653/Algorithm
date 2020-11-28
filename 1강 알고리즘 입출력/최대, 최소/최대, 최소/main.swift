//
//  main.swift
//  최대, 최소
//
//  Created by 최원석 on 2020/11/24.
//

import Foundation

let N = Int(readLine()!)!

let input = readLine()!.split(separator: " ").map() { Int(String($0))! }

var min = 1000000
var max = -1000000

for i in input {
    
    if min > i {
        min = i
    }
    
    if max < i {
        max = i
    }
}

print("\(min) \(max)")

