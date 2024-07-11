const elderAge = (m, n, l, t) => {
	let lines = [];

	for (let i = 0; i < m; i++) {
		let row = [];

		for (let j = 0; j < n; j++) {
			let curr = i === j ? 0 : i % t ^ j % t;

			// Convert decimal to binary
			curr >= l ? row.push(curr - l) : null;
		}

		lines.push(
			// row,
			row.reduce(
				(accumulator, currentValue) => accumulator + currentValue,
				0,
			),
		);
	}

	const total = lines.reduce(
		(accumulator, currentValue) => accumulator + currentValue,
		0,
	);

	console.log(total % t);
	return total % t;
};

// elderAge(8,5,1,100) // 5
// elderAge(8, 8, 0, 100007); // 224
// elderAge(25, 31, 0, 100007); // 11925

// elderAge(5, 45, 3, 1000007); // 4323
// elderAge(31, 39, 7, 2345); // 1586
// elderAge(545, 435, 342, 1000007); // 808451s
elderAge(1000000, 1000000, 7109602, 13719506);
