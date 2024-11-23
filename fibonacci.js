function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

async function runExperiment() {
    const jsTimes = [];
    const nValues = Array.from({ length: 50 }, (_, i) => i + 1); // n from 1 to 50

    const start = performance.now(); // Start timing before loop
    for (let n of nValues) {
        fibonacci(n); // Call the function for each n
        const current = performance.now(); // Current time after computing fibonacci(n)
        
        const time = current - start; // Calculate cumulative time since start
        jsTimes.push({ n, time }); // Store n and cumulative time
    }

    console.log("JavaScript Cumulative Times:", JSON.stringify(jsTimes));
}

runExperiment();
