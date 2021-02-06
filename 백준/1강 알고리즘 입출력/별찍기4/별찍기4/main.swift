//
//  main.swift
//  별찍기4
//
//  Created by 최원석 on 2020/11/24.
//

import Foundation

var input = Int(readLine()!)!


for i in 1...input {
    var string = ""
    for _ in 1..<i {
        string += " "
    }
    for _ in 0...input - i {
        string += "*"
    }
    print(string)
}




