#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (err, res, body) => {
  if (err) { console.error(err); return; }
  const users = {};
  JSON.parse(body).forEach(task => {
    const id = task.userId;
    if (!users[id] && task.completed) { users[id] = 1; } else if (task.completed) { users[id] += 1; }
  });
  console.log(users);
});
