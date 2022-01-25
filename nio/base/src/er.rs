use std::io::stdin;

#[derive(Eq, Debug)]
struct Candidate {
    id: usize,
    votes: usize,
}

impl PartialEq for Candidate {
    fn eq(&self, other: &Self) -> bool {
        self.id == other.id
    }
}

impl PartialOrd for Candidate {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Candidate {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.votes.cmp(&other.votes)
    }
}

impl Candidate {
    pub fn read(id: usize) -> Self {
        let stdin = stdin();
        let mut s = String::new();

        stdin.read_line(&mut s).unwrap();

        Self {
            id,
            votes: s.trim().parse().unwrap(),
        }
    }
}

pub fn main() {
    let stdin = stdin();
    let mut s = String::new();

    stdin.read_line(&mut s).unwrap();

    let mut v = s.split(" ");
    let (voties, candidates) = (
        v.next().unwrap().trim().parse::<usize>().unwrap(),
        v.next().unwrap().trim().parse::<usize>().unwrap(),
    );

    let mut heap = std::collections::BinaryHeap::with_capacity(candidates);

    let first = Candidate::read(0);

    let original_votes = first.votes;
    let mut fvotes = first.votes;

    heap.push(first);

    for id in 1..candidates {
        heap.push(Candidate::read(id))
    }

    loop {
        match heap.pop() {
            Some(Candidate { id: 0, votes }) => break,
            Some(Candidate { id, votes }) if votes == fvotes => break,
            Some(Candidate { id, votes }) => {
                let next = heap.peek().unwrap();
                let delta = (votes - next.votes) / 2;
                let delta = if delta > 0 { delta } else { 1 };

                fvotes += delta;

                heap.push(Candidate {
                    votes: fvotes,
                    id: 0,
                });
                heap.push(Candidate {
                    id,
                    votes: votes - delta,
                })
            }
            None => todo!(),
        }
    }

    println!("{}", fvotes - original_votes);
}
