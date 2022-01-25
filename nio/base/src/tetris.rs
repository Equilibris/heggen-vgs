use std::io::stdin;

pub fn main() {
    let stdin = stdin();
    let mut s = String::new();

    stdin.read_line(&mut s).unwrap();

    let mut v = s.split(" ");
    let (n, size) = (
        v.next().unwrap().trim().parse::<usize>().unwrap(),
        v.next().unwrap().trim().parse::<usize>().unwrap(),
    );

    // let max_width: u32 = 1 << (size - 1);

    // let mut process: Vec<u32> = Vec::with_capacity(1024);

    let mut levels = [0usize; 10];

    let mut out = Vec::with_capacity(n);

    for _ in 0..n {
        let mut s = String::new();
        stdin.read_line(&mut s).unwrap();

        let mut v = s.split(" ");

        let (pos, size) = (
            v.next().unwrap().trim().parse::<usize>().unwrap(),
            v.next().unwrap().trim().parse::<usize>().unwrap(),
        );

        let mut slice = levels[pos..pos + size].into_iter();

        let mut max = slice.next().unwrap();
        for i in slice {
            max = max.max(i)
        }
        let h = 1 + *max;
        for i in pos..pos + size {
            levels[i] = h;
        }
        out.push(h);
    }
    for i in out {
        println!("{}", i);
    }
}

/*
8 10
0 3
    1
7 3
    1
2 6
    2
0 5
    3
0 1
    4
5 5
    3
0 7
    4
9 1
    4
*/
