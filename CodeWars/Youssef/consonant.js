const letters = {
	// a: 1,
	b: 2,
	c: 3,
	d: 4,
	// e: 5,
	f: 6,
	g: 7,
	h: 8,
	// i: 9,
	j: 10,
	k: 11,
	l: 12,
	m: 13,
	n: 14,
	// o: 15,
	p: 16,
	q: 17,
	r: 18,
	s: 19,
	t: 20,
	// u: 21,
	v: 22,
	w: 23,
	x: 24,
	y: 25,
	z: 26,
};

const solve = (s = "") => {
	const noAs = s.split("a").join(" ");
	const noEs = noAs.split("e").join(" ");
	const noIs = noEs.split("i").join(" ");
	const noOs = noIs.split("o").join(" ");
	const noUs = noOs.split("u").join(" ");

	const noVowels = noUs.split(" ");

	const values = noVowels.map((str) =>
		str.split("").map((letter) => letters[letter]),
	);

	const total = values.map((numbers) => numbers.reduce((a, b) => a + b, 0), 0);

	const max = Math.max(...total);

	return max;
};

solve("abscdefagguk");
