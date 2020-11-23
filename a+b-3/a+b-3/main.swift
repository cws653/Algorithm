//
//  main.swift
//  a+b-3
//
//  Created by 최원석 on 2020/11/23.
//

import Foundation

print("Hello, World!")

let a = readLine()

if let a = a {
    var array = a.components(separatedBy: " ")
    let sol = Int(array[0])! + Int(array[1])! - 3
    print(sol)
}
