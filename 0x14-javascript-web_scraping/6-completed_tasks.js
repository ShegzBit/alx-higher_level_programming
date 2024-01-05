#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const len = itr => { return Array.from(itr).length; };

request.get(apiUrl, (err, res, body) => {
  if (err) { console.error(err); return; }
  const users = new Map();
  let i = 0;
  JSON.parse(body).forEach(task => {
    const id = task.userId;
    if (!users.has(id)) { users.set(id, 0); }
    if (task.completed) { users.set(id, users.get(id) + 1); }
  });
  process.stdout.write('{');
  users.forEach((value, key) => {
    (i === 0)
      ? console.log(` ${key}: ${value},`)
      : ((i < len(users.keys()) - 1)
          ? console.log(`  ${key}: ${value},`)
          : console.log(`  ${key}: ${value} }`)); i++;
  });
});
