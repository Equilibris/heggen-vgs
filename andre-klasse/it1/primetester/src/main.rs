#![feature(portable_simd)]
use std::simd::u64x8;

fn main() {
    let mut input = String::new();

    std::io::stdin().read_line(&mut input).unwrap();

    let n: u64 = input.trim().parse().unwrap();

    let upper_bound = 4 + ((f64::sqrt(n as f64) / 8f64) as u64);

    let goal = u64x8::splat(n);
    let step = u64x8::splat(8);

    let mut base = u64x8::from_array([2u64, 3, 4, 5, 6, 7, 8, 9]);

    'a: for _ in 0..upper_bound {
        let res = goal % base;

        if res.horizontal_product() == 0 {
            let v = res.lanes_eq(u64x8::splat(0)).select(base, u64x8::splat(0));

            for i in v.to_array() {
                if i != 0 {
                    println!("{} {}", i, n / i);
                    break 'a;
                }
            }
        }

        base += step;
    }
}
