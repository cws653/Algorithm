//
//  main.swift
//  기찍N
//
//  Created by 최원석 on 2020/11/23.
//

import Foundation

//if let a = readLine() {
//    if let b = Int(a) {
//        for i in (1...b).reversed() {
//            print(i)
//        }
//    }
//}

// stride 함수 : by의 값만큼 from ~ to 사이에서 루프를 돈다.
for i in stride(from: Int(readLine()!)!, to: 0, by: -1) {
    print(i)
}
