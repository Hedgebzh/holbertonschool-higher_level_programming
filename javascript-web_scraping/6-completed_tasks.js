#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const all = JSON.parse(body);
    const TaskCompleted = {};
    for (let i = 0; i < all.length; i++) {
      if (all[i].completed === true) {
        if (TaskCompleted[all[i].userId] === undefined) {
          TaskCompleted[all[i].userId] = 0;
        }
        TaskCompleted[all[i].userId]++;
      }
    }
    console.log(TaskCompleted);
  }
});