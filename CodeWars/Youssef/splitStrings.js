const solution = (str) => {
	const arr = str.split("");
	const isEven = str.length % 2 === 0 ? true : false;

	!isEven && arr.push("_");

	let newArr = [];

	for (let i = 0; i < arr.length; i += 2) {
		newArr.push(`${arr[i]}${arr[i + 1]}`);
	}

	return newArr;
};
