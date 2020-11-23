//
//  main.swift
//  a+b
//
//  Created by 최원석 on 2020/11/23.
//

import Foundation

print("Hello, World!")

let a = readLine()


// readline 함수 : 키보드 입력값을 받아주는 함수
// components 함수 : string 형태를 구분자를 기준으로 쪼개어 배열에 담아주는 함수
if let a = a {
    var array = a.components(separatedBy: " ")
    let sol = Int(array[0])! + Int(array[1])!
    print(sol)
//    for i in 0..<array.count {
//        print(array[i])
//    }
}

