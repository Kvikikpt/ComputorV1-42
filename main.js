const validPrint = (str) => console.log(str);

function square(x) {
    let n = x;
    let result = x;
    let changed = x;
    while (result * result !== x) {
        result = (result + n/result) / 2;
        if (changed === result) break;
        changed = result;
    }
    return result;
}

function exec_square(a, b, c, precision, showProcess) {
    if (showProcess) validPrint(`a:${a} b:${b} c:${c}`);
    let disc = b ** 2 - (4 * a * c);
    if (showProcess) {
        validPrint(`Discriminant solution: ${b}^2 - (4 * ${a} * ${c})`);
        validPrint(`Discriminant: ${disc}`);
    }
    if (disc === 0) {
        let solution = ((b * -1) / (2 * a)).toPrecision(precision);
        validPrint(`Discriminant is 0, the only solution is:`);
        if (showProcess) validPrint(`Solution: (${b} * -1) / (2 * ${a})`);
        if (showProcess) validPrint(`Result: ${solution}`);
        else validPrint(solution);
        return;
    }
    if (disc < 0) {
        validPrint(`Discriminant is strictly negative, the two solutions are:`);
        let leftPart = (-1 * b) / (2 * a);
        let rightPart = square(-1 * disc) / (2 * a);
        if (showProcess) validPrint(`Solution: (-1 * ${b} +/- square(-1 * ${disc}) * i) / (2 * ${a})`);
        if (showProcess) validPrint(`Reduced solution: ((${(-1 * b) / (2 * a)}) +/- (${square(-1 * disc)} * i / ${2 * a}))`);
        if (showProcess) validPrint(`Result:`);
        validPrint(`${leftPart.toPrecision(precision)}` + ` - ` + `${rightPart.toPrecision(precision)} * i`);
        validPrint(`${leftPart.toPrecision(precision)}` + ` + ` + `${rightPart.toPrecision(precision)} * i`);
        return;
    }
    let xone = ((b * -1) - square(disc)) / (2 * a);
    let xtwo = ((b * -1) + square(disc)) / (2 * a);
    if (showProcess) validPrint(`Solution: ((${b} * -1) +/- (square(${disc})) / 2 * ${a}`);
    if (showProcess) validPrint(`Reduced solution: ((${b  * -1} +/- ${square(disc)}) / ${a * 2}`);
    xone = xone.toPrecision(precision);
    xtwo = xtwo.toPrecision(precision);
    if (xone === xtwo)
        validPrint(`Discriminant is strictly positive, the only solution is:\n${xone}`);
    else
        validPrint(`Discriminant is strictly positive, the two solutions are:\n${xone}\n${xtwo}`);
}

function exec_simple(a, b, precision, showProcess) {
    if (showProcess) validPrint(`Solution expression: (${b} * -1) / ${a}`);
    if (showProcess) validPrint(`Reduced: ${b * -1} / ${a}`);
    validPrint(`The solution is:\n${((b * -1) / a).toPrecision(precision)}`);
}

function validateXstring(string, expression) {
    string = string.trim();
    if (/^((\d*)|(\d*[\.,\,]\d*))$/.test(string)) string = `${string} * X^0`;
    if (/^[x,X]$/.test(string)) string = '1 * X^1';
    if (/^((\d*)|(\d*[\.,\,]\d*)) *\* *[x,X]$/.test(string)) string = `${string.split(/ *\* */)[0]} * X^1`;
    if (/^[x,X] *\* *((\d*)|(\d*[\.,\,]\d*))$/.test(string)) string = `${string.split(/ *\* */)[1]} * X^1`;
    if (/^[x,X]\^((\d*)|(\d*[\.,\,]\d*))$/.test(string)) string = `1 * ${string}`;
    if (/^[X,x]\^((\d*)|(\d*[\.,\,]\d*)) *\* *((\d*)|(\d*[\.,\,]\d*))$/.test(string))
        string = `${string.split(/ *\* */)[1]} * ${string.split(/ *\* */)[0]}`;
    if (/^((\d*)|(\d*[\.,\,]\d*))[x,X]$/.test(string)) string = `${string.split(/[x,X]/)[0]} * X^1`;
    if (/^((\d*)|(\d*[\.,\,]\d*))[x,X]\^\d*$/.test(string)) string = `${string.split(/[x,X]/)[0]} * X^${string.split(/\^/)[1]}`;
    if (!/^((\d*)|(\d*[\.,\,]\d*)) *\* *[X,x]\^((\d*)|(\d*[\.,\,]\d*))$/.test(string))
        throw new Error(`Validation error: ${expression.split(string)[0]}\x1b[41m${string}\x1b[0m${expression.split(string[1])}`);
    let [number, x] = string.split(/ *\* */);
    number = Number(number);
    if (Number.isInteger(number) && !Number.isSafeInteger(number))
        throw new Error(`Number is too big, the precision may be broken`);
    let xValue = x.split(/\^/)[1];
    return {number, xValue};
}

function arrayValidation(array, expression) {
    let xArrays = {};
    array.split(/ *\+ */)
        .map(splitted_plus => {
            let [plus, minus] = splitted_plus.split(/ *\- */);
            let validPlus = validateXstring(plus, expression);
            if (!xArrays[validPlus.xValue]) xArrays[validPlus.xValue] = [];
            xArrays[validPlus.xValue].push({
                value: validPlus.number,
                sign: true
            });
            if (minus) {
                let validMinus = validateXstring(minus, expression);
                if (!xArrays[validMinus.xValue]) xArrays[validMinus.xValue] = [];
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
    let prec;
    let showProcess = false;

    while (a < args.length) {
        if (args[a].indexOf('-p') !== -1) {
            prec = Number(args[a + 1]);
            if (isNaN(prec))
                throw new Error('Not right usage of prec flag.');
            if (prec < 1 || prec > 100) throw new Error("Invalid precision parameter, need 1 - 100");
            args.splice(a, 2);
            continue;
        }
        if (args[a].indexOf('-s') !== -1) {
            showProcess = true;
            args.splice(a, 1);
            continue;
        }
        a += 1;
    }

    if (args.length > 1) throw new Error('Too much params.');

    if (args.length === 1) {
        let expression = args[0];
        if (typeof expression !== "string") throw new Error('No expression passed.');
        let splitted = expression.split('=');
        if (splitted.length !== 2) throw new Error('Invalid expression passed.');
        const [left, right] = splitted.map(array => arrayValidation(array, expression))
        let xObj = {};
        for (let key in left) {
            if (!xObj[key]) xObj[key] = 0;
            left[key].map(item => {
                if (item.sign) xObj[key] += item.value;
                else xObj[key] -= item.value;
            })
            if (xObj[key] === 0) delete xObj[key];
        }
        for (let key in right) {
            if (!xObj[key]) xObj[key] = 0;
            right[key].map(item => {
                if (item.sign) xObj[key] -= item.value;
                else xObj[key] += item.value;
            })
            if (xObj[key] === 0) delete xObj[key];
        }
        let xKeys = Object.keys(xObj);
        if (xKeys.length === 0) return validPrint('Each real number is a solution.')
        let first = true;
        let reduced_str = `Reduced form: `
        for (let key of xKeys) {
            if (xObj[key] === 0) continue;
            if (!first) reduced_str += xObj[key] > 0 ? ' + ' : ' - ';
            reduced_str += (first ? xObj[key] : (xObj[key] > 0 ? xObj[key] : xObj[key] * -1))+' * X^' + key;
            first = false;
        }
        reduced_str += ' = 0';
        validPrint(reduced_str);
        const degree = xKeys[xKeys.length - 1]
        validPrint(`Polynomial degree: ${degree}`);
        if (degree > 2)
            throw new Error('The polynomial degree is strictly greater than 2, I can\'t solve.');
        if (degree === '0')
            throw new Error("There's no possible solutions.");
        if (degree === "2" && xKeys.length === 1) return validPrint('The only solution is 0.');
        if (degree === "1") return exec_simple(xObj['1'] || 0, xObj['0'] || 0,  prec, showProcess);
        return exec_square(xObj['2'] || 0, xObj['1'] || 0, xObj['0'] || 0, prec, showProcess);
    }
    else throw new Error('usage: [flags: -p + {1 - 100}]');
}

try {
    exec();
}
catch (e) {
    console.log(e.message || 'Unknown error');
}
