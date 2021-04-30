function exec() {
    if (process.argv.length < 2) return;
    const args = process.argv.slice(2);

    let a = 0;
    let flag = 0;
    let prec = 6;

    while (a < args.length) {
        if (args[a].indexOf('-p') !== -1) {
            prec = Number(args[a + 1]);
            console.log(prec)
            if (isNaN(prec)) {
                console.log('Not right usage of flag -p');
                return;
            }
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
        let left = splitted[0];
        let right = splitted[1];
        console.log(left);
        console.log(right);
    }
    else {
        console.log('usage: [flags: -p] + [flags parameters if needed for: -p] [polynomial equation]');
    }
}

try {
    exec();
}
catch (e) {
    console.log(e);
}
