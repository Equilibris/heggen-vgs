use std::io::stdin;

#[derive(Debug)]
enum Shape {
    Circle { x: f64, y: f64, r: f64 },
    Rect { x_0: f64, y_0: f64, x: f64, y: f64 },
}

impl Shape {
    pub fn new(str: String) -> Self {
        let mut values = str.split(" ");
        if let Some('c') = str.chars().nth(0) {
            let (x, y, r) = (
                values.next().unwrap().parse::<f64>().unwrap(),
                values.next().unwrap().parse::<f64>().unwrap(),
                values.next().unwrap().parse::<f64>().unwrap(),
            );

            Self::Circle { x, y, r }
        } else {
            let (x_0, y_0, x, y) = (
                values.next().unwrap().parse::<f64>().unwrap(),
                values.next().unwrap().parse::<f64>().unwrap(),
                values.next().unwrap().parse::<f64>().unwrap(),
                values.next().unwrap().parse::<f64>().unwrap(),
            );

            Self::Rect { x_0, y_0, x, y }
        }
    }
}

pub fn main() {
    let stdin = stdin();
    let mut s = String::new();

    stdin.read_line(&mut s).unwrap();

    let mut values = s.split(" ");
    let (size_x, size_y, n_img, n_building) = (
        values.next().unwrap().parse::<f64>().unwrap(),
        values.next().unwrap().parse::<f64>().unwrap(),
        values.next().unwrap().parse::<usize>().unwrap(),
        values.next().unwrap().parse::<usize>().unwrap(),
    );

    let mut imgs: Vec<Shape> = Vec::with_capacity(n_img);

    for i in 1..n_img {
        let mut s = String::new();

        stdin.read_line(&mut s).unwrap();

        imgs.push(Shape::new(s));
    }

    for i in 1..n_building {
        let mut s = String::new();

        stdin.read_line(&mut s).unwrap();

        let mut values = s.split(" ");
        let (x, y) = (
            values.next().unwrap().parse::<f64>().unwrap(),
            values.next().unwrap().parse::<f64>().unwrap(),
        );
    }
}
