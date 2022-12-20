#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const all = JSON.parse(body);
    const TaskCompleted = {};
    for (let i = 0; i < todos.length; i++) {
      if (all[i].completed === true) {
        if (TaskCompleted[todos[i].userId] === undefined) {
          TaskCompleted[todos[i].userId] = 0;
        }
        TaskCompleted[all[i].userId]++;
      }
    }
    console.log(TaskCompleted);
  }
});