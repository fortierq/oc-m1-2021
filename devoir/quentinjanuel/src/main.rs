struct Object { wgt: i32, val: i32 }

struct Objects(Vec<Object>);

impl Objects {
    fn from(arr: &[(i32, i32)]) -> Self {
        let objects = arr
            .iter()
            .map(|(w, v)| Object {
                wgt: *w,
                val: *v,
            })
            .collect();
        Self(objects)
    }
    fn knapsack(&self, capacity: i32) -> i32 {
        let mut v = (0..=capacity)
            .map(|_| vec![0])
            .collect::<Vec<_>>();
        self.0.iter()
            .enumerate()
            .for_each(|(k, o)|
                (0..=capacity).for_each(|c| {
                    let a = v[c as usize][k];
                    let b = if c - o.wgt >= 0 {
                        v[(c - o.wgt) as usize][k] + o.val
                    } else {
                        0
                    };
                    v[c as usize].push(std::cmp::max(a, b));
                })
            );
        v.pop().unwrap().pop().unwrap()
    }
}

fn main() {
    let objects = Objects::from(&[
        (2,  1),
        (3,  7),
        (6, 10),
        (5, 10),
        (8, 13),
        (2,  1),
        (2,  1),
    ]);
    assert_eq!(objects.knapsack(10), 18);
}
