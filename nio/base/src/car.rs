use std::io::stdin;

pub fn main() {
    let stdin = stdin();
    let mut s = String::new();

    stdin.read_line(&mut s).unwrap();

    let mut v = s.split(" ");
    let (n_packages, capacity, home) = (
        v.next().unwrap().trim().parse::<usize>().unwrap(),
        v.next().unwrap().trim().parse::<usize>().unwrap(),
        v.next().unwrap().trim().parse::<i32>().unwrap(),
    );

    let mut left_queue = std::collections::BinaryHeap::new();
    let mut right_queue = std::collections::BinaryHeap::new();

    let mut drive_dst = 0;

    for i in 0..n_packages {
        let mut s = String::new();

        stdin.read_line(&mut s).unwrap();

        let dst = s.trim().parse::<i32>().unwrap() - home;

        if dst < 0 {
            left_queue.push(dst.abs());
        } else {
            right_queue.push(dst);
        }
    }

    while left_queue.len() > 0 {
        let greatest_dst = left_queue.pop().unwrap();

        for _ in 1..capacity {
            left_queue.pop();
        }
        drive_dst += greatest_dst * 2;
    }
    while right_queue.len() > 0 {
        let greatest_dst = right_queue.pop().unwrap();

        for _ in 1..capacity {
            right_queue.pop();
        }
        drive_dst += greatest_dst * 2;
    }

    println!("{}", drive_dst);
}
