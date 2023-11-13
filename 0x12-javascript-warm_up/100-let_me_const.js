logToConsole = console.log;
console.log = () => logToConsole(333);
