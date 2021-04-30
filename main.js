function validateXstring(string) {
    if (!/\d* *\* *[X,x]\^[0,1,2]/.test(string))
        throw new Error(`Validation error: ${string}`);
    let [number, x] = string.split(/ *\* */);
    number = Number(number);
    if (!Number.isSafeInteger(number))
        throw new Error(`Number is too big, the precision may be broken`);
    let xValue = x.split(/\^/)[1];
    return {number, xValue};
}

function arrayValidation(array) {
    let xArrays = {'0': [], '1': [], '2': []};
    array.split(/ *\+ */)
        .map(splitted_plus => {
            let [plus, minus] = splitted_plus.split(/ *\- */);
            let validPlus = validateXstring(plus);
            xArrays[validPlus.xValue].push({
                value: validPlus.number,
                sign: true
            });
            if (minus) {
                let validMinus = validateXstring(minus);
                xArrays[validMinus.xValue].push({
                    value: validMinus.number,
                    sign: false
                });
            }
        })
    return xArrays;
}

function exec() {
    if (process.argv.length < 2) throw new Error('Invalid arguments.')
    const args = process.argv.slice(2);

    let a = 0;
    let flag = 0;
    let prec = 6;

    while (a < args.length) {
        if (args[a].indexOf('-p') !== -1) {
            prec = Number(args[a + 1]);
            console.log(prec)
            if (isNaN(prec))
                throw new Error('Not right usage of prec flag.')
            flag += 2;
            a += 1;
        }
        a += 1;
    }

    if (args.length === 1 + flag) {
        let expression = args[flag];
        if (typeof expression !== "string") return;
        let splitted = expression.split(' = ');
        if (splitted.length !== 2) return;
        const [left, right] = splitted.map(array => arrayValidation(array))
        console.log(left);
        console.log(right);
        let x0 = 0, x1 = 0, x2 = 0;
        left["0"].map(item => {
            if (item.sign) x0 += item.value;
            else x0 -= item.value;
        })
        left["1"].map(item => {
            if (item.sign) x1 += item.value;
            else x1 -= item.value;
        })
        left["2"].map(item => {
            if (item.sign) x2 += item.value;
            else x2 -= item.value;
        })
        right["0"].map(item => {
            if (item.sign) x0 -= item.value;
            else x0 += item.value;
        })
        right["1"].map(item => {
            if (item.sign) x1 -= item.value;
            else x1 += item.value;
        })
        right["2"].map(item => {
            if (item.sign) x2 -= item.value;
            else x2 += item.value;
        })
        console.log(x0, x1, x2)
    }
    else {
        throw new Error('usage: [flags: -p] + [flags parameters if needed for: -p] [polynomial equation]');
    }
}

try {
    exec();
}
catch (e) {
    console.log(e.message || 'Unknown error');
    console.log(e);
}
